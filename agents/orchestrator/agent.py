"""
Agente Orquestador Principal de heru.app
"""
from pathlib import Path
import anthropic
from core.base_agent import BaseAgent


CONFIG_PATH = Path(__file__).parent / "config.yaml"


class OrchestratorAgent(BaseAgent):
    """
    Orquestador principal que analiza solicitudes, crea planes de ejecución
    y coordina la delegación entre agentes especializados.
    """

    def __init__(self, client: anthropic.Anthropic, **kwargs):
        super().__init__(
            config_path=str(CONFIG_PATH),
            client=client,
            **kwargs,
        )

    def analyze_and_route(self, request: str) -> dict:
        """
        Analiza una solicitud y devuelve un plan de routing estructurado.

        Returns:
            dict con keys: analysis, agents_to_use, execution_order, instructions
        """
        prompt = f"""Analiza esta solicitud del equipo de heru y crea un plan detallado:

SOLICITUD: {request}

Responde en este formato exacto:

**ANÁLISIS**
[Tu análisis de qué se necesita]

**AGENTES A USAR**
[Lista los agentes necesarios: lead_qualifier / copywriter / graphic_designer / social_listener / performance_ads]

**ORDEN DE EJECUCIÓN**
[sequential o parallel, y por qué]

**INSTRUCCIONES POR AGENTE**
[Para cada agente, qué debe hacer específicamente]

**CRITERIOS DE ÉXITO**
[Cómo saber si la tarea fue completada exitosamente]"""

        return self.run(prompt)

    def synthesize(self, original_request: str, agent_results: dict) -> str:
        """
        Sintetiza resultados de múltiples agentes en una respuesta cohesiva.

        Args:
            original_request: La solicitud original del usuario
            agent_results: Dict {agent_name: result_string}
        """
        results_formatted = "\n\n".join(
            f"### {name.replace('_', ' ').upper()}\n{result}"
            for name, result in agent_results.items()
        )

        prompt = f"""El equipo de agentes procesó esta solicitud y produjo los siguientes resultados.
Intégralos en una respuesta final cohesiva y accionable.

SOLICITUD ORIGINAL: {original_request}

RESULTADOS DE AGENTES:
{results_formatted}

Crea una respuesta integrada que:
1. Elimine redundancias
2. Conecte los outputs de forma lógica
3. Destaque los puntos más importantes
4. Termine con próximos pasos claros y numerados
5. Use el tono de heru: cercano, empoderador, directo"""

        return self.run(prompt)

    def prioritize_tasks(self, tasks: list) -> str:
        """Prioriza una lista de tareas según el impacto en el negocio de heru."""
        tasks_str = "\n".join(f"- {t}" for t in tasks)
        prompt = f"""Prioriza estas tareas para el equipo de marketing/ventas de heru.app
según su impacto potencial en las métricas clave del negocio (CAC, conversiones, retención):

TAREAS:
{tasks_str}

Ordénalas de mayor a menor impacto y justifica brevemente cada decisión."""
        return self.run(prompt)
