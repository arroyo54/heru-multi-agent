"""
Servidor FastAPI para el sistema multi-agente de heru.app.
Expone los agentes como endpoints REST.

Uso:
    uvicorn api.server:app --reload --port 8000
"""
import asyncio
import json
import os
import re
import time
import uuid
from contextlib import asynccontextmanager
from datetime import datetime
from pathlib import Path

from typing import List, Optional, Tuple

import anthropic
import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from agents.lead_qualifier.agent import LeadQualifierAgent
from agents.copywriter.agent import CopywriterAgent
from agents.graphic_designer.agent import GraphicDesignerAgent
from agents.social_listener.agent import SocialListenerAgent
from agents.performance_ads.agent import PerformanceAdsAgent
from agents.business_analyst.agent import BusinessAnalystAgent
from agents.sat_intelligence.agent import SATIntelligenceAgent
from api.schemas import ErrorResponse, LeadInput, QualificationResponse
from api.chat_bot import detect_agent, clean_mention, format_response, help_message
from core.connectors.apify import ApifyConnector
from core.scheduler import start_scheduler

# ─── Bootstrap ───────────────────────────────────────────────────────────────

# Carga .env solo si existe (desarrollo local). En Railway las variables
# se inyectan directamente en os.environ — load_dotenv no es necesario.
_env_file = Path(__file__).parent.parent / ".env"
if _env_file.exists():
    load_dotenv(dotenv_path=_env_file, override=False)

# Estado global del servidor (inicializado en lifespan)
_state: dict = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Inicializa los agentes una sola vez al arrancar el servidor."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError(
            "ANTHROPIC_API_KEY no encontrada en las variables de entorno. "
            "En Railway: agrégala en el dashboard → Variables. "
            "En local: crea un archivo .env con ANTHROPIC_API_KEY=sk-ant-..."
        )

    model = os.environ.get("MODEL", "claude-opus-4-6")
    client = anthropic.Anthropic(api_key=api_key)

    # Inicializar todos los agentes (modelo principal para la API REST)
    _state["client"] = client
    _state["model"]  = model
    _state["qualifier"]   = LeadQualifierAgent(client=client,   model=model, verbose=False)
    _state["copywriter"]  = CopywriterAgent(client=client,      model=model, verbose=False)
    _state["designer"]    = GraphicDesignerAgent(client=client,  model=model, verbose=False)
    _state["social"]      = SocialListenerAgent(client=client,   model=model, verbose=False)
    _state["performance"] = PerformanceAdsAgent(client=client,   model=model, verbose=False)
    _state["analyst"]     = BusinessAnalystAgent(client=client,  model=model, verbose=False)
    _state["sat"]         = SATIntelligenceAgent(client=client,  model=model, verbose=False)

    # Agentes rápidos para Google Chat (haiku, max 1500 tokens — responde en ~3-5s)
    chat_model = os.environ.get("CHAT_MODEL", "claude-haiku-4-5-20251001")
    _state["chat_qualifier"]   = LeadQualifierAgent(client=client,   model=chat_model, verbose=False, max_tokens=1500)
    _state["chat_copywriter"]  = CopywriterAgent(client=client,      model=chat_model, verbose=False, max_tokens=1500)
    _state["chat_designer"]    = GraphicDesignerAgent(client=client,  model=chat_model, verbose=False, max_tokens=1500)
    _state["chat_social"]      = SocialListenerAgent(client=client,   model=chat_model, verbose=False, max_tokens=1500)
    _state["chat_performance"] = PerformanceAdsAgent(client=client,   model=chat_model, verbose=False, max_tokens=1500)
    _state["chat_analyst"]     = BusinessAnalystAgent(client=client,  model=chat_model, verbose=False, max_tokens=1500)
    _state["chat_sat"]         = SATIntelligenceAgent(client=client,  model=chat_model, verbose=False, max_tokens=1500)

    print(f"✅ 7 agentes inicializados (api: {model} | chat: {chat_model})")
    _sa = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", "")
    print(f"[STARTUP] SA_JSON={'SET len=' + str(len(_sa)) if _sa else 'NOT SET / EMPTY'}")

    # Scheduler del Social Listener — solo si Apify está configurado
    if ApifyConnector.is_available():
        from scripts.weekly_report import run_weekly_report, run_quora_report
        _state["scheduler"] = start_scheduler(
            weekly_report_fn=run_weekly_report,
            quora_report_fn=run_quora_report,
        )
    else:
        print("ℹ️  APIFY_API_TOKEN no configurada — scheduler de Social Listener inactivo")

    yield

    # Cleanup al detener el servidor
    if "scheduler" in _state:
        _state["scheduler"].shutdown(wait=False)
    _state.clear()


# ─── App ─────────────────────────────────────────────────────────────────────

app = FastAPI(
    title="heru Multi-Agent API",
    description=(
        "API REST para el sistema multi-agente de heru.app. "
        "Expone agentes especializados en calificación de leads, "
        "creación de contenido, social listening y performance de ads."
    ),
    version="1.0.0",
    lifespan=lifespan,
)


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _format_lead(lead: LeadInput) -> str:
    """Convierte el LeadInput en el texto que recibe el agente."""
    rfc_line = f"RFC: {lead.rfc}" if lead.rfc else "RFC: No proporcionado / sin RFC registrado"
    phone_line = f"Teléfono: {lead.phone}" if lead.phone else ""
    accountant = "Sí tiene contador o servicio contable actual" if lead.has_accountant else "No tiene contador ni servicio contable"

    parts = [
        f"Nombre: {lead.name}",
        f"Email: {lead.email}",
        phone_line,
        rfc_line,
        f"Actividad económica: {lead.economic_activity}",
        f"Situación / relación con el SAT: {lead.sat_reaction}",
        f"Contador: {accountant}",
        f"Necesidad fiscal principal: {lead.tax_need}",
    ]
    return "\n".join(line for line in parts if line)


def _parse_score(analysis: str) -> Tuple[Optional[int], Optional[str]]:
    """
    Extrae el lead score y clasificación del texto del agente.
    Retorna (score, classification) o (None, None) si no se puede parsear.
    """
    score = None
    classification = None

    # Buscar patrones como "TOTAL: 74/100" o "Lead Score: 74" o "Score: 74"
    score_match = re.search(
        r"(?:TOTAL|Score|LEAD SCORE)[:\s]+(\d{1,3})\s*(?:/\s*100)?",
        analysis,
        re.IGNORECASE,
    )
    if score_match:
        candidate = int(score_match.group(1))
        if 0 <= candidate <= 100:
            score = candidate

    # Buscar clasificación HOT / WARM / COLD
    class_match = re.search(r"\b(HOT|WARM|COLD)\b", analysis, re.IGNORECASE)
    if class_match:
        classification = class_match.group(1).upper()

    return score, classification


def _extract_section(analysis: str, header: str) -> str:
    """Extrae el contenido de texto plano que sigue a un encabezado del análisis."""
    pattern = rf"\*{{0,2}}{re.escape(header)}\*{{0,2}}\s*\n+(.*?)(?=\n\s*(?:\*{{1,2}}|\#{1,3}|\Z))"
    match = re.search(pattern, analysis, re.IGNORECASE | re.DOTALL)
    if not match:
        return ""
    content = match.group(1).strip()
    content = re.sub(r"\*+", "", content)        # quitar negritas/cursivas
    content = re.sub(r"#+\s*", "", content)       # quitar encabezados markdown
    content = re.sub(r"-\s+", "", content)        # quitar viñetas
    content = re.sub(r"\s+", " ", content)        # colapsar espacios y saltos
    return content.strip()[:220]


def _build_plan_recommendation(
    analysis: str,
    lead: LeadInput,
) -> Tuple[Optional[str], Optional[str], bool, Optional[str]]:
    """
    Extrae o infiere el plan recomendado, régimen y flags adicionales.

    Prioridad:
    1. Lo que el agente escribió en su análisis (fuente de verdad)
    2. Inferencia por palabras clave como fallback

    Returns:
        (plan_recomendado, regimen_fiscal, incluye_regularizacion, nota_declaracion_anual)
    """
    # ── 1. Extraer lo que dijo el agente ────────────────────────────────────
    plan_del_agente = _extract_section(analysis, "PLAN RECOMENDADO")
    regimen_del_agente = _extract_section(analysis, "RÉGIMEN FISCAL")
    regularizacion_texto = _extract_section(analysis, "REGULARIZACIÓN")
    declaracion_texto = _extract_section(analysis, "DECLARACIÓN ANUAL")

    # ── 2. Normalizar plan ────────────────────────────────────────────────────
    plan: Optional[str] = None
    plan_lower = plan_del_agente.lower()

    if "plataforma" in plan_lower:
        plan = "Plan Plataformas"
    elif "freelancer" in plan_lower or "resico" in plan_lower:
        plan = "Plan Freelancer"
    elif "empresarial" in plan_lower:
        plan = "Plan Empresarial"
    elif plan_del_agente:
        plan = plan_del_agente  # texto literal del agente si no matcheó ninguno

    # ── 3. Fallback por keywords si el agente no fue explícito ───────────────
    if not plan:
        corpus = f"{lead.economic_activity} {lead.sat_reaction} {lead.tax_need}".lower()

        plataformas = ["uber", "didi", "rappi", "indrive", "cabify", "beat",
                       "uber eats", "didi food", "amazon flex", "conductor",
                       "repartidor", "delivery", "plataforma tecnologica"]
        resico = ["resico", "régimen simplificado", "regimen simplificado"]
        empresarial = ["actividad empresarial", "servicios profesionales",
                       "honorarios", "persona moral"]

        if any(s in corpus for s in plataformas):
            plan = "Plan Plataformas"
        elif any(s in corpus for s in resico):
            plan = "Plan Freelancer"
        elif any(s in corpus for s in empresarial):
            plan = "Plan Empresarial"
        else:
            plan = "Régimen por confirmar"

    # ── 4. Regularización ─────────────────────────────────────────────────────
    regularizacion_positiva = any(
        w in regularizacion_texto.lower()
        for w in ["sí", "si aplica", "aplica", "necesita", "requiere"]
    )
    # Fallback: señales en el input del lead
    if not regularizacion_positiva:
        corpus_reg = f"{lead.sat_reaction} {lead.tax_need} {analysis}".lower()
        señales_reg = ["atrasado", "sin declarar", "nunca he declarado",
                       "nunca declaré", "varios años", "rezago", "multa",
                       "notificaci", "carta del sat", "requerimiento",
                       "no he declarado", "ponerse al corriente", "al corriente",
                       "periodos anteriores", "años sin"]
        regularizacion_positiva = any(s in corpus_reg for s in señales_reg)

    # ── 5. Declaración anual ──────────────────────────────────────────────────
    nota_declaracion: Optional[str] = None
    if declaracion_texto:
        nota_declaracion = "El lead preguntó por declaración anual — verificar elegibilidad antes de ofrecer"

    return plan, regimen_del_agente or None, regularizacion_positiva, nota_declaracion


_EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F9FF"  # símbolos, pictogramas, emojis generales
    "\U00002700-\U000027BF"  # dingbats
    "\U0001FA00-\U0001FA9F"  # símbolos adicionales
    "\u2600-\u26FF"          # misceláneos
    "\u2700-\u27BF"
    "]+",
    flags=re.UNICODE,
)


def _clean(text: str) -> str:
    """Elimina emojis, markdown y caracteres de control. Devuelve texto plano limpio."""
    text = _EMOJI_RE.sub("", text)
    text = re.sub(r"\*+|#+|`+|>+", "", text)   # negrita, headers, code, citas
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # links markdown
    text = re.sub(r"[-•]\s+", "", text)          # viñetas
    text = re.sub(r"\s+", " ", text)             # espacios múltiples y saltos
    return text.strip()


def _first_sentence(text: str, max_chars: int = 180) -> str:
    """Toma la primera oración significativa de un bloque de texto."""
    sentence = re.split(r"(?<=[.!?])\s+", text.strip())[0]
    return sentence[:max_chars]


def _build_summary(
    analysis: str,
    lead: LeadInput,
    score: Optional[int],
    classification: Optional[str],
    plan: Optional[str],
    incluye_regularizacion: bool,
    nota_declaracion: Optional[str],
) -> str:
    """
    Resumen ejecutivo de 6 líneas en texto plano, listo para pegar en Google Chat.
    Sin markdown, sin tablas, sin emojis.
    Líneas: Score | Clasificación | Segmento | Pain point | Plan | Next step
    """
    score_str   = f"{score}/100" if score is not None else "N/D"
    class_str   = classification or "N/D"

    # Segmento — buscar en el perfil del lead que generó el agente
    segmento_raw = (
        _extract_section(analysis, "Segmento")
        or _extract_section(analysis, "SEGMENTO")
        or lead.economic_activity
    )
    segmento = _clean(segmento_raw)

    # Pain point — primera oración del bloque correspondiente
    pain_raw = (
        _extract_section(analysis, "PAIN POINT PRINCIPAL")
        or _extract_section(analysis, "PAIN POINT")
        or lead.sat_reaction
    )
    pain_point = _first_sentence(_clean(pain_raw))

    # Plan
    plan_str = plan or "Regimen por confirmar"
    if incluye_regularizacion:
        plan_str += " + Regularizacion"
    if nota_declaracion:
        plan_str += " | Declaracion anual: verificar"

    # Next step — primera oración del bloque correspondiente
    next_raw = (
        _extract_section(analysis, "NEXT STEP RECOMENDADO")
        or _extract_section(analysis, "NEXT STEP")
        or ""
    )
    next_step = _first_sentence(_clean(next_raw)) if next_raw else "Revisar analisis completo"

    lines = [
        f"Score: {score_str}",
        f"Clasificacion: {class_str}",
        f"Segmento: {segmento}",
        f"Pain point: {pain_point}",
        f"Plan: {plan_str}",
        f"Next step: {next_step}",
    ]
    return "\n".join(lines)


# ─── Endpoints ───────────────────────────────────────────────────────────────

@app.get("/", tags=["health"])
async def health():
    """Health check — verifica que el servidor y los agentes están activos."""
    return {
        "status": "ok",
        "service": "heru-multi-agent-api",
        "agents_loaded": list(_state.keys()),
        "timestamp": datetime.utcnow().isoformat(),
    }


@app.post(
    "/qualify-lead",
    response_model=QualificationResponse,
    responses={500: {"model": ErrorResponse}},
    tags=["leads"],
    summary="Califica un lead con el agente especializado de heru",
    description=(
        "Recibe los datos de un lead, los procesa con el LeadQualifierAgent "
        "y devuelve un análisis completo con score (0-100), clasificación "
        "(HOT/WARM/COLD), plan recomendado y next step sugerido."
    ),
)
async def qualify_lead(lead: LeadInput) -> QualificationResponse:
    qualifier: LeadQualifierAgent = _state.get("qualifier")
    if not qualifier:
        raise HTTPException(status_code=503, detail="LeadQualifierAgent no disponible")

    lead_text = _format_lead(lead)

    try:
        analysis = qualifier.qualify_lead(lead_text)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Error al procesar el lead: {exc}")

    score, classification = _parse_score(analysis)
    plan, regimen, incluye_regularizacion, nota_declaracion = _build_plan_recommendation(analysis, lead)
    summary = _build_summary(analysis, lead, score, classification, plan, incluye_regularizacion, nota_declaracion)

    return QualificationResponse(
        lead_id=str(uuid.uuid4()),
        analysis=analysis,
        lead_score=score,
        classification=classification,
        plan_recomendado=plan,
        regimen_fiscal=regimen,
        incluye_regularizacion=incluye_regularizacion,
        nota_declaracion_anual=nota_declaracion,
        summary=summary,
        timestamp=datetime.utcnow().isoformat(),
    )


# ─── Google Chat REST API ────────────────────────────────────────────────────

async def _post_to_chat_rest_api(space: str, thread: str, text: str) -> bool:
    """
    Publica un mensaje en Google Chat via REST API usando service account.
    Necesario cuando el app está configurado como Google Workspace Add-on
    (gcp-sa-gsuiteaddons), donde las respuestas HTTP síncronas son ignoradas.
    """
    sa_json_str = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
    if not sa_json_str:
        return False

    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import Request as GoogleAuthRequest

        sa_info = json.loads(sa_json_str)
        creds = service_account.Credentials.from_service_account_info(
            sa_info,
            scopes=["https://www.googleapis.com/auth/chat.bot"],
        )
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, lambda: creds.refresh(GoogleAuthRequest()))

        payload: dict = {"text": text}
        if thread:
            payload["thread"] = {"name": thread}
            payload["messageReplyOption"] = "REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD"

        async with httpx.AsyncClient(timeout=15.0) as client:
            r = await client.post(
                f"https://chat.googleapis.com/v1/{space}/messages",
                headers={"Authorization": f"Bearer {creds.token}"},
                json=payload,
            )
            print(f"[CHAT REST] status={r.status_code} body={r.text[:300]}")
            return r.status_code == 200
    except Exception as e:
        print(f"[CHAT REST ERROR] {e}")
        return False


# ─── Google Chat Bot ──────────────────────────────────────────────────────────

@app.post(
    "/chat/webhook",
    tags=["chat-bot"],
    summary="Webhook para el bot de Google Chat",
    description="Google Chat envía aquí los mensajes del equipo. El bot los rutea al agente correcto y responde en el mismo hilo.",
)
async def chat_webhook(request: Request):
    """
    Recibe eventos de Google Chat y responde con el agente correcto.

    Tipos de evento que maneja:
    - MESSAGE: mensaje directo o @mention al bot
    - ADDED_TO_SPACE: el bot fue agregado al espacio
    - REMOVED_FROM_SPACE: el bot fue eliminado (no requiere respuesta)
    """
    t0 = time.time()
    try:
        body = await request.json()
    except Exception:
        return JSONResponse({"text": "Error al leer el mensaje."}, status_code=400)

    print(f"[CHAT DEBUG] body={body}")

    # Google Chat usa estructura: chat.messagePayload.message
    chat_data       = body.get("chat", {})
    message_payload = chat_data.get("messagePayload", {})
    message         = message_payload.get("message", {})
    sender          = chat_data.get("user", {}).get("displayName", "equipo")

    # Nombres de espacio y hilo para REST API
    space_name  = message.get("space", {}).get("name", "")
    thread_name = message.get("thread", {}).get("name", "")

    # Modo de respuesta: REST API (Add-on) o HTTP síncrono (Bot)
    _sa_val = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", "")
    use_rest_api = bool(_sa_val)

    # argumentText ya tiene el @mention eliminado; fallback a text
    raw_text = message.get("argumentText", message.get("text", "")).strip()

    _sa_status = f"len={len(_sa_val)} starts={_sa_val[:15]!r}" if _sa_val else "EMPTY"
    print(f"[CHAT DEBUG] sender={sender!r} raw_text={raw_text!r} rest_api={use_rest_api} SA_JSON={_sa_status}")

    async def send(text_reply: str):
        """Envía la respuesta por REST API o HTTP según configuración."""
        if use_rest_api:
            asyncio.create_task(
                _post_to_chat_rest_api(space_name, thread_name, text_reply)
            )
            return JSONResponse({})          # 200 vacío — REST API postea la respuesta
        return JSONResponse({"text": text_reply})

    if not raw_text:
        return await send("Hola! Escribe *@growth-agents ayuda* para ver los comandos disponibles.")

    text = clean_mention(raw_text)

    # Ping de diagnóstico — respuesta instantánea
    if text.lower() in ("ping", "test", "prueba", "hola"):
        return await send("pong — bot activo")

    # Comando de ayuda
    if text.lower() in ("ayuda", "help", "?", ""):
        return await send(help_message())

    # Detectar agente
    agent_key, hint = detect_agent(text)
    print(f"[CHAT DEBUG] agent_key={agent_key!r} elapsed={time.time()-t0:.1f}s")

    # Ejecutar el agente con timeout de 25 segundos
    loop = asyncio.get_event_loop()
    try:
        response = await asyncio.wait_for(
            loop.run_in_executor(None, _run_agent, agent_key, text),
            timeout=25.0,
        )
    except asyncio.TimeoutError:
        print(f"[CHAT DEBUG] TIMEOUT — agent_key={agent_key!r}")
        return await send(
            f"⏳ El agente {agent_key} está tardando más de lo esperado. "
            "Intenta con una solicitud más corta."
        )
    except Exception as e:
        print(f"[CHAT DEBUG] ERROR agent_key={agent_key!r} err={e}")
        return await send(f"⚠️ Error: {str(e)[:200]}")

    print(f"[CHAT DEBUG] OK elapsed={time.time()-t0:.1f}s")

    reply = format_response(agent_key, response, sender)
    if hint:
        reply += f"\n\n_{hint}_"

    print(f"[CHAT DEBUG] response_len={len(reply)} preview={reply[:120]!r}")
    return await send(reply)


def _run_agent(agent_key: str, text: str) -> str:
    """Despacha el texto al agente chat (haiku) correcto y retorna la respuesta."""
    # Usa los agentes rápidos (haiku) dedicados al chat
    a = _state

    if agent_key == "qualifier":
        return a["chat_qualifier"].qualify_lead(text)

    if agent_key == "sat":
        return a["chat_sat"].analyze_sat_update(text)

    if agent_key == "copywriter":
        return a["chat_copywriter"].run(
            f"El equipo de heru te pide lo siguiente:\n\n{text}"
        )

    if agent_key == "designer":
        # Chat: prompt directo y conciso — create_visual_concept genera demasiado output
        return a["chat_designer"].run(
            f"Eres un director creativo de heru.app. El equipo pide:\n\n{text}\n\n"
            "Responde en máximo 350 palabras. Incluye: concepto creativo, "
            "composición/estructura, y un prompt en inglés listo para Midjourney o Stable Diffusion."
        )

    if agent_key == "performance":
        from core.connectors.google_ads import GoogleAdsConnector
        connector = GoogleAdsConnector(force_demo=True)
        metrics   = connector.format_for_agent(period_days=7)
        return a["chat_performance"].generate_report(
            report_type="weekly",
            metrics_data=metrics,
            platform="all",
        )

    if agent_key == "social":
        return a["chat_social"].run(
            f"El equipo pregunta sobre social listening:\n\n{text}"
        )

    if agent_key == "analyst":
        return a["chat_analyst"].run(
            f"El equipo solicita un análisis:\n\n{text}"
        )

    # Fallback: copywriter
    return a["chat_copywriter"].run(text)


@app.get(
    "/chat/setup",
    tags=["chat-bot"],
    summary="Instrucciones para conectar el bot a Google Chat",
)
async def chat_setup():
    """Devuelve las instrucciones paso a paso para configurar el Google Chat App."""
    base_url = os.environ.get("RAILWAY_PUBLIC_DOMAIN", "TU_URL_DE_RAILWAY")
    webhook  = f"https://{base_url}/chat/webhook"
    return {
        "webhook_url": webhook,
        "instrucciones": [
            "1. Ve a console.cloud.google.com → proyecto auditor-ventas-heru",
            "2. APIs y servicios → Biblioteca → habilita 'Google Chat API'",
            "3. APIs y servicios → Google Chat API → Configuración",
            "4. Nombre del bot: heru-bot",
            "5. URL del endpoint: " + webhook,
            "6. En 'Funciones': activa Mensajes directos y Menciones en espacios",
            "7. Guarda y publica el bot (estado: Activo)",
            "8. En tu espacio de Google Chat → Agregar personas y bots → busca 'heru-bot'",
            "9. Escribe '@heru-bot ayuda' para probar",
        ],
        "comandos_ejemplo": [
            "@heru-bot ayuda",
            "@heru-bot califica este lead: conductor de Uber CDMX, tiene RFC, nunca ha declarado",
            "@heru-bot el SAT cambió las reglas de RESICO esta semana",
            "@heru-bot escribe un post de TikTok sobre el miedo al SAT",
            "@heru-bot cómo van las campañas esta semana",
        ],
    }
