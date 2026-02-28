"""
Servidor FastAPI para el sistema multi-agente de heru.app.
Expone los agentes como endpoints REST.

Uso:
    uvicorn api.server:app --reload --port 8000
"""
import os
import re
import uuid
from contextlib import asynccontextmanager
from datetime import datetime
from pathlib import Path

from typing import Optional, Tuple

import anthropic
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from agents.lead_qualifier.agent import LeadQualifierAgent
from api.schemas import ErrorResponse, LeadInput, QualificationResponse

# ─── Bootstrap ───────────────────────────────────────────────────────────────

load_dotenv()

# Estado global del servidor (inicializado en lifespan)
_state: dict = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Inicializa los agentes una sola vez al arrancar el servidor."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY no encontrada en .env")

    model = os.getenv("MODEL", "claude-opus-4-6")
    client = anthropic.Anthropic(api_key=api_key)

    config_path = Path(__file__).parent.parent / "agents" / "lead_qualifier" / "config.yaml"
    _state["qualifier"] = LeadQualifierAgent(
        client=client,
        model=model,
        verbose=False,
    )

    print(f"✅ LeadQualifierAgent inicializado (modelo: {model})")
    yield
    # Cleanup al detener el servidor
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

    return QualificationResponse(
        lead_id=str(uuid.uuid4()),
        analysis=analysis,
        lead_score=score,
        classification=classification,
        timestamp=datetime.utcnow().isoformat(),
    )
