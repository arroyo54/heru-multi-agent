"""
Google Chat Bot — heru Multi-Agent
Recibe mensajes del equipo en Google Chat y los rutea al agente correcto.

Flujo:
  Equipo escribe "@heru-bot [mensaje]" en Google Chat
  → Google Chat hace POST a /chat/webhook
  → Se detecta el agente por palabras clave
  → El agente procesa y responde en el mismo hilo

Setup (una sola vez):
  Ver instrucciones en: /chat/setup
"""
import re
import os
from typing import Optional, Tuple


# ─── Routing por palabras clave ───────────────────────────────────────────────

ROUTES = [
    {
        "agent":    "qualifier",
        "keywords": ["califica", "lead", "prospecto", "calificación", "scoring",
                     "cliente potencial", "nuevo contacto"],
        "hint":     "💡 Incluye los datos del prospecto (actividad, RFC, situación fiscal)",
    },
    {
        "agent":    "sat",
        "keywords": ["sat cambió", "nuevo sat", "cambio sat", "alerta fiscal",
                     "cambio resico", "nueva regla", "obligación fiscal",
                     "fecha límite", "declaración vence", "reforma fiscal",
                     "resolución miscelánea"],
        "hint":     None,
    },
    {
        "agent":    "copywriter",
        "keywords": ["escribe", "redacta", "post", "contenido", "copy",
                     "caption", "tiktok", "instagram", "guion", "email",
                     "campaña de contenido", "calendario"],
        "hint":     None,
    },
    {
        "agent":    "designer",
        "keywords": ["diseño", "visual", "imagen", "brief visual", "prompt",
                     "concepto visual", "storyboard", "banner", "creativo"],
        "hint":     None,
    },
    {
        "agent":    "performance",
        "keywords": ["campaña", "ads", "performance", "métricas", "roas",
                     "cpl", "cac", "google ads", "meta ads", "presupuesto ads",
                     "cómo van los anuncios", "resultados campaña"],
        "hint":     None,
    },
    {
        "agent":    "social",
        "keywords": ["social", "menciones", "listener", "reporte social",
                     "qué dicen de heru", "twitter", "reddit", "tendencias",
                     "sentimiento", "redes sociales"],
        "hint":     None,
    },
    {
        "agent":    "analyst",
        "keywords": ["analiza", "cruza", "análisis", "correlación", "insight",
                     "reporte ejecutivo", "resumen semanal", "datos negocio"],
        "hint":     None,
    },
]

AGENT_LABELS = {
    "qualifier":  "🎯 Lead Qualifier",
    "sat":        "🏛 SAT Intelligence",
    "copywriter": "✍️ Copywriter",
    "designer":   "🎨 Graphic Designer",
    "performance":"📈 Performance Ads",
    "social":     "👂 Social Listener",
    "analyst":    "📊 Business Analyst",
}


def detect_agent(text: str) -> Tuple[str, Optional[str]]:
    """
    Detecta qué agente debe responder según el mensaje.
    Retorna (agent_key, hint) donde hint puede ser None.
    Usa word-boundary para keywords de una sola palabra para evitar
    falsos positivos (ej: "lead" no debe matchear "leads").
    """
    clean = text.lower()
    # Quitar el @mention si viene (ej: "@heru-bot califica...")
    clean = re.sub(r"@\S+\s*", "", clean).strip()

    for route in ROUTES:
        for kw in route["keywords"]:
            if " " in kw:
                # Frase multi-palabra: buscar como substring exacto
                if kw in clean:
                    return route["agent"], route["hint"]
            else:
                # Palabra sola: usar word boundary para evitar falsos positivos
                if re.search(r"\b" + re.escape(kw) + r"\b", clean):
                    return route["agent"], route["hint"]

    return "orchestrator", None


def clean_mention(text: str) -> str:
    """Quita el @mention del inicio del mensaje."""
    return re.sub(r"^@\S+\s*", "", text).strip()


def format_response(agent_key: str, response: str, sender: str) -> str:
    """
    Formatea la respuesta para Google Chat.
    Google Chat soporta texto plano con *negrita* y _cursiva_.
    """
    label = AGENT_LABELS.get(agent_key, "🤖 heru-bot")
    header = f"*{label}* — respuesta para {sender}\n{'─'*40}\n"
    # Truncar si es muy largo para Chat (límite ~4000 chars)
    body = response if len(response) <= 3800 else response[:3800] + "\n\n_[Respuesta truncada — ver reporte completo en Sheets]_"
    return header + body


def help_message() -> str:
    return (
        "*🤖 heru-bot — Comandos disponibles*\n\n"
        "*🎯 Calificar lead*\n"
        "`@heru-bot califica este lead: [datos del prospecto]`\n\n"
        "*🏛 Alerta fiscal SAT*\n"
        "`@heru-bot el SAT cambió [descripción del cambio]`\n\n"
        "*✍️ Crear contenido*\n"
        "`@heru-bot escribe un post de Instagram sobre [tema]`\n\n"
        "*🎨 Concepto visual*\n"
        "`@heru-bot diseño para campaña de [objetivo]`\n\n"
        "*📈 Performance de campañas*\n"
        "`@heru-bot cómo van las campañas esta semana`\n\n"
        "*👂 Social listening*\n"
        "`@heru-bot qué dicen de heru en redes sociales`\n\n"
        "*📊 Análisis de negocio*\n"
        "`@heru-bot analiza [datos o contexto]`\n\n"
        "_Tip: No necesitas ser exacto — el bot detecta la intención automáticamente._"
    )
