"""
Schemas de request/response para la API REST de heru multi-agente.
"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
import uuid


class LeadInput(BaseModel):
    name: str = Field(..., description="Nombre completo del lead")
    email: EmailStr = Field(..., description="Correo electrónico")
    phone: Optional[str] = Field(None, description="Teléfono (opcional)")
    rfc: Optional[str] = Field(None, description="RFC del lead si ya tiene")
    economic_activity: str = Field(
        ...,
        description="Actividad económica principal. Ej: 'Conductor de Uber', 'Diseñador freelance'",
    )
    sat_reaction: str = Field(
        ...,
        description="Situación o sentimiento actual respecto al SAT. "
                    "Ej: 'Recibí una notificación y no sé qué hacer', 'Nunca he declarado'",
    )
    has_accountant: bool = Field(
        ...,
        description="¿Actualmente tiene contador o servicio contable?",
    )
    tax_need: str = Field(
        ...,
        description="Necesidad fiscal principal que expresó el lead. "
                    "Ej: 'Quiero facturar a mis clientes', 'Ponerme al corriente con el SAT'",
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Carlos Mendoza",
                "email": "carlos@example.com",
                "phone": "+52 55 1234 5678",
                "rfc": "MEMC890312AB1",
                "economic_activity": "Conductor de Uber (tiempo completo, 3 años)",
                "sat_reaction": "Recibí un correo del SAT hace 2 semanas y no sé qué hacer",
                "has_accountant": False,
                "tax_need": "Ponerme al corriente con mis declaraciones y evitar multas",
            }
        }
    }


class QualificationResponse(BaseModel):
    lead_id: str = Field(description="ID único de esta calificación")
    agent: str = Field(default="lead_qualifier")
    analysis: str = Field(description="Análisis completo del agente en markdown")
    lead_score: Optional[int] = Field(
        None,
        description="Score extraído del análisis (0-100). None si no fue posible parsearlo.",
        ge=0,
        le=100,
    )
    classification: Optional[str] = Field(
        None,
        description="Clasificación del lead: HOT / WARM / COLD",
    )
    plan_recomendado: Optional[str] = Field(
        None,
        description=(
            "Plan heru según el régimen fiscal del lead: "
            "'Plan Plataformas', 'Plan Freelancer', 'Plan Empresarial' "
            "o 'Régimen por confirmar' si no fue posible determinarlo."
        ),
    )
    incluye_regularizacion: bool = Field(
        default=False,
        description="True si el lead muestra señales de rezago fiscal y aplica Regularización.",
    )
    nota_declaracion_anual: Optional[str] = Field(
        None,
        description=(
            "Presente solo si el lead mencionó la declaración anual explícitamente. "
            "Indica que debe verificarse elegibilidad, no es una recomendación directa."
        ),
    )
    regimen_fiscal: Optional[str] = Field(
        None,
        description="Régimen fiscal identificado o inferido del lead.",
    )
    summary: str = Field(
        description=(
            "Resumen ejecutivo en texto plano (4 líneas), listo para pegar en Google Chat. "
            "Incluye: score, clasificación, pain point y plan recomendado."
        )
    )
    timestamp: str = Field(description="ISO 8601 timestamp de la calificación")


class ErrorResponse(BaseModel):
    detail: str
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
