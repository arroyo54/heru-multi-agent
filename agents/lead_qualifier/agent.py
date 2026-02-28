"""
Agente Qualifier de Leads de heru.app
"""
from pathlib import Path
from typing import Optional
import anthropic

from core.base_agent import BaseAgent
from core.models import LeadProfile


CONFIG_PATH = Path(__file__).parent / "config.yaml"


class LeadQualifierAgent(BaseAgent):
    """
    Agente especializado en calificar leads de ventas para heru.app.
    Analiza perfiles, asigna lead scores y define próximos pasos.
    """

    def __init__(self, client: anthropic.Anthropic, **kwargs):
        super().__init__(
            config_path=str(CONFIG_PATH),
            client=client,
            **kwargs,
        )

    def qualify_lead(self, lead_info: str, additional_context: Optional[str] = None) -> str:
        """
        Califica un lead basándose en la información proporcionada.

        Args:
            lead_info: Descripción o datos del lead
            additional_context: Canal de origen, interacciones previas, etc.
        """
        context = {}
        if additional_context:
            context["contexto_adicional"] = additional_context

        prompt = f"""Califica este lead para heru.app:

INFORMACIÓN DEL LEAD:
{lead_info}

Proporciona:

**PERFIL DEL LEAD**
- Nombre/ID:
- Segmento: (conductor/freelancer/profesionista/comerciante/otro)
- Actividad:
- Ingresos estimados:
- Situación fiscal actual:

**LEAD SCORE: [0-100]**
Desglose:
- Necesidad fiscal (40pts máx): X/40
- Fit con producto (30pts máx): X/30
- Urgencia (20pts máx): X/20
- Capacidad de pago (10pts máx): X/10
TOTAL: X/100

**CLASIFICACIÓN**
🔥 HOT (70-100) / ⚡ WARM (40-69) / ❄️ COLD (0-39)

**PAIN POINT PRINCIPAL**
[El problema más urgente que tiene]

**PLAN RECOMENDADO**
[Plan heru más adecuado y por qué]

**OBJECIONES PROBABLES**
[1-3 objeciones que puede tener]

**NEXT STEP RECOMENDADO**
[Acción específica: llamada, demo, registro directo, nurturing]

**MENSAJE PERSONALIZADO SUGERIDO**
[Draft de primer mensaje para este lead]"""

        return self.run(prompt, context if context else None)

    def qualify_from_conversation(self, conversation: str) -> str:
        """
        Califica un lead basándose en una conversación o chat.

        Args:
            conversation: Transcripción de la conversación con el lead
        """
        prompt = f"""Analiza esta conversación con un prospecto de heru y califica el lead:

CONVERSACIÓN:
{conversation}

Extrae la información relevante de la conversación y aplica el framework de calificación
completo. Si falta información crítica para la calificación, indícala y sugiere
preguntas de seguimiento."""

        return self.run(prompt)

    def generate_follow_up_questions(self, partial_profile: str) -> str:
        """
        Genera preguntas de seguimiento para completar la calificación de un lead.
        """
        prompt = f"""Basándote en esta información parcial de un prospecto, genera las preguntas
de seguimiento más importantes para completar la calificación:

INFORMACIÓN DISPONIBLE:
{partial_profile}

Genera máximo 4 preguntas:
1. Ordenadas por importancia para la calificación
2. En tono conversacional y no intimidante
3. Diseñadas para no asustar al prospecto con terminología fiscal
4. Con el objetivo de determinar su urgencia y fit con heru"""

        return self.run(prompt)

    def batch_score_leads(self, leads: list) -> str:
        """
        Califica múltiples leads y los ordena por prioridad.

        Args:
            leads: Lista de strings con información de cada lead
        """
        leads_formatted = "\n---\n".join(
            f"LEAD #{i+1}:\n{lead}" for i, lead in enumerate(leads)
        )

        prompt = f"""Califica y prioriza estos {len(leads)} leads para el equipo de ventas de heru:

{leads_formatted}

Para cada lead, proporciona:
1. Score (0-100)
2. Clasificación (HOT/WARM/COLD)
3. Razón principal del score
4. Next step

Al final, ordénalos de mayor a menor prioridad con justificación."""

        return self.run(prompt)

    def handle_objection(self, objection: str, lead_context: Optional[str] = None) -> str:
        """
        Genera una respuesta para manejar una objeción específica de un lead.
        """
        context = {}
        if lead_context:
            context["perfil_lead"] = lead_context

        prompt = f"""Un prospecto de heru tiene esta objeción:

OBJECIÓN: "{objection}"

Genera una respuesta que:
1. Valide el sentimiento del prospecto (sin invalidar su objeción)
2. Reencuadre la objeción desde el valor de heru
3. Use datos o casos concretos si es posible
4. Termine con una pregunta que avance la conversación
5. Sea en tono conversacional, no de vendedor"""

        return self.run(prompt, context if context else None)
