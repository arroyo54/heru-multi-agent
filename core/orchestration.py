"""
Motor de orquestación del sistema multi-agente de heru.app.
Coordina la comunicación entre agentes y gestiona el flujo de trabajo.
"""
import anthropic
from pathlib import Path
from typing import Dict, Any, Optional, List, Callable
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

from .base_agent import BaseAgent
from .models import AgentRole, Task, TaskStatus, OrchestrationPlan


console = Console()


class AgentRegistry:
    """Registro central de todos los agentes del sistema."""

    def __init__(self):
        self._agents: Dict[AgentRole, BaseAgent] = {}

    def register(self, role: AgentRole, agent: BaseAgent):
        self._agents[role] = agent
        console.print(f"[blue]→[/blue] Registrado: [bold]{agent.name}[/bold] como [italic]{role.value}[/italic]")

    def get(self, role: AgentRole) -> Optional[BaseAgent]:
        return self._agents.get(role)

    def list_agents(self) -> List[str]:
        return [f"{role.value}: {agent.name}" for role, agent in self._agents.items()]

    def __contains__(self, role: AgentRole) -> bool:
        return role in self._agents


class TaskQueue:
    """Cola simple de tareas para el orquestador."""

    def __init__(self):
        self._tasks: List[Task] = []

    def add(self, task: Task):
        self._tasks.append(task)

    def get_pending(self) -> List[Task]:
        return [t for t in self._tasks if t.status == TaskStatus.PENDING]

    def get_by_id(self, task_id: str) -> Optional[Task]:
        return next((t for t in self._tasks if t.id == task_id), None)

    def complete(self, task_id: str, result: Any):
        task = self.get_by_id(task_id)
        if task:
            from datetime import datetime
            task.status = TaskStatus.COMPLETED
            task.result = result
            task.completed_at = datetime.now().isoformat()

    def fail(self, task_id: str, error: str):
        task = self.get_by_id(task_id)
        if task:
            task.status = TaskStatus.FAILED
            task.error = error

    def summary(self) -> Dict[str, int]:
        statuses = [t.status for t in self._tasks]
        return {
            "total": len(self._tasks),
            "pending": statuses.count(TaskStatus.PENDING),
            "in_progress": statuses.count(TaskStatus.IN_PROGRESS),
            "completed": statuses.count(TaskStatus.COMPLETED),
            "failed": statuses.count(TaskStatus.FAILED),
        }


class Orchestrator:
    """
    Orquestador principal del sistema multi-agente de heru.app.

    Responsabilidades:
    - Analizar solicitudes y determinar qué agentes involucrar
    - Delegar tareas a los agentes correctos
    - Coordinar flujos secuenciales y paralelos
    - Sintetizar resultados de múltiples agentes
    """

    def __init__(self, client: anthropic.Anthropic, verbose: bool = True):
        self.client = client
        self.verbose = verbose
        self.registry = AgentRegistry()
        self.task_queue = TaskQueue()
        self._orchestrator_agent: Optional[BaseAgent] = None

        console.print(
            Panel(
                "[bold green]Sistema Multi-Agente heru.app[/bold green]\nInicializando orquestador...",
                border_style="green",
            )
        )

    def setup_orchestrator_agent(self, config_path: str):
        """Inicializa el agente orquestador con su configuración."""
        self._orchestrator_agent = BaseAgent(
            config_path=config_path,
            client=self.client,
            verbose=False,
        )

    def register_agent(self, role: AgentRole, agent: BaseAgent):
        """Registra un agente especializado en el sistema."""
        self.registry.register(role, agent)

    # ──────────────────────────── Core Methods ──────────────────────────────

    def gather_clarifications(
        self,
        request: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, List[str]]:
        """
        Crea el plan y le pregunta a cada agente qué dudas tiene antes de ejecutar.
        Devuelve dict {nombre_agente: [pregunta1, pregunta2, ...]}
        Solo incluye agentes que tengan al menos una pregunta.
        """
        plan = self._create_plan(request, context)
        all_questions: Dict[str, List[str]] = {}

        for step in plan.steps:
            agent = self.registry.get(step["agent"])
            if not agent:
                continue
            questions = agent.ask_clarifications(step.get("task", request))
            if questions:
                all_questions[step["agent_name"]] = questions

        return all_questions

    def process(self, request: str, context: Optional[Dict[str, Any]] = None) -> str:
        """
        Punto de entrada principal. Recibe una solicitud, analiza,
        delega a los agentes correctos y devuelve el resultado.
        """
        if self.verbose:
            console.print(
                Panel(
                    f"[bold]Solicitud recibida:[/bold]\n{request}",
                    title="[cyan]Orquestador[/cyan]",
                    border_style="cyan",
                )
            )

        # 1. Analizar la solicitud y crear un plan
        plan = self._create_plan(request, context)

        if self.verbose:
            self._display_plan(plan)

        # 2. Ejecutar el plan
        results = self._execute_plan(plan)

        # 3. Sintetizar resultados
        final_response = self._synthesize_results(request, plan, results)

        return final_response

    def delegate(
        self,
        role: AgentRole,
        task: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> str:
        """
        Delega una tarea directamente a un agente específico.
        Útil para llamadas directas sin necesidad de orquestación compleja.
        """
        agent = self.registry.get(role)
        if not agent:
            return f"Error: No hay agente registrado para el rol '{role.value}'"

        if self.verbose:
            console.print(f"[blue]→ Delegando a {agent.name}...[/blue]")

        return agent.run(task, context)

    # ────────────────────────── Plan Creation ───────────────────────────────

    def _create_plan(
        self,
        request: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> OrchestrationPlan:
        """
        Usa el agente orquestador para analizar la solicitud y crear un plan.
        Si no hay agente orquestador, usa lógica de routing por palabras clave.
        """
        if self._orchestrator_agent:
            return self._ai_driven_plan(request, context)
        else:
            return self._keyword_routing_plan(request)

    def _ai_driven_plan(
        self,
        request: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> OrchestrationPlan:
        """Genera un plan usando el agente orquestador con IA."""
        import json as _json
        import re as _re

        agents_list = "\n".join(self.registry.list_agents())

        analysis_prompt = f"""Analiza esta solicitud y devuelve un plan de orquestación en formato JSON estricto.

SOLICITUD: {request}

AGENTES DISPONIBLES:
{agents_list}

ROLES VÁLIDOS (usa exactamente estos valores):
- lead_qualifier
- copywriter
- graphic_designer
- social_listener
- performance_ads
- business_analyst
- sat_intelligence

REGLAS DE PIPELINE:
- Si se pide copy + visual/imagen: primero copywriter, luego graphic_designer (el diseñador usa el copy del paso anterior)
- Si se pide campaña completa: copywriter → graphic_designer → performance_ads
- Si es un lead o prospecto: solo lead_qualifier
- Si son métricas, campañas o ads: solo performance_ads
- Si es monitoreo o menciones: solo social_listener
- Si es análisis de datos de negocio: solo business_analyst
- Si es cambio del SAT o fiscal: solo sat_intelligence
- Activa SOLO los agentes estrictamente necesarios

Responde ÚNICAMENTE con este JSON sin texto adicional:
{{
  "analysis": "una línea explicando qué se necesita",
  "steps": [
    {{
      "step": 1,
      "role": "nombre_del_rol",
      "task": "instrucción específica para este agente"
    }}
  ]
}}"""

        raw = self._orchestrator_agent.run(analysis_prompt, context, maintain_history=False)

        agents_involved = []
        steps = []
        analysis_text = raw

        try:
            json_match = _re.search(r'\{[\s\S]*\}', raw)
            if json_match:
                plan_data = _json.loads(json_match.group())
                analysis_text = plan_data.get("analysis", raw)
                role_map = {r.value: r for r in AgentRole}
                for step_data in plan_data.get("steps", []):
                    role_str = step_data.get("role", "")
                    role = role_map.get(role_str)
                    if role and role != AgentRole.ORCHESTRATOR:
                        agent = self.registry.get(role)
                        agent_name = agent.name if agent else role_str
                        agents_involved.append(role)
                        steps.append({
                            "step": step_data.get("step", len(steps) + 1),
                            "agent": role,
                            "agent_name": agent_name,
                            "task": step_data.get("task", request),
                        })
        except Exception:
            pass

        # Fallback si el JSON falló
        if not steps:
            return self._keyword_routing_plan(request)

        return OrchestrationPlan(
            original_request=request,
            analysis=analysis_text,
            steps=steps,
            agents_involved=agents_involved,
            execution_order="sequential",
        )

    def _keyword_routing_plan(self, request: str) -> OrchestrationPlan:
        """Routing basado en palabras clave cuando no hay agente orquestador."""
        request_lower = request.lower()

        copy_kw    = ["post", "contenido", "copy", "texto", "instagram", "facebook", "tiktok", "linkedin", "email", "anuncio", "publicación", "guión", "caption", "redacta", "escribe"]
        design_kw  = ["imagen", "diseño", "visual", "banner", "creativo", "brief", "prompt", "ilustración", "gráfico", "carrusel"]
        lead_kw    = ["lead", "prospecto", "calificar", "cliente potencial", "score", "interesado"]
        social_kw  = ["menciones", "monitoreo", "sentimiento", "escuchar", "trending", "quejas", "reputación"]
        ads_kw     = ["ads", "campañas", "roas", "cac", "cpl", "cpa", "performance", "presupuesto", "métricas de campaña", "facebook ads", "google ads"]
        analyst_kw = ["análisis de datos", "reporte cruzado", "insight de negocio", "correlación"]
        sat_kw     = ["sat", "resico", "régimen fiscal", "declaración anual", "impuesto", "rfc"]

        wants_copy   = any(kw in request_lower for kw in copy_kw)
        wants_design = any(kw in request_lower for kw in design_kw)

        def _agent(role: AgentRole):
            a = self.registry.get(role)
            return a.name if a else role.value

        steps = []

        # Pipeline copy → diseño: el diseñador trabaja sobre el copy generado
        if wants_copy and wants_design:
            steps = [
                {"step": 1, "agent": AgentRole.COPYWRITER,      "agent_name": _agent(AgentRole.COPYWRITER),      "task": request},
                {"step": 2, "agent": AgentRole.GRAPHIC_DESIGNER, "agent_name": _agent(AgentRole.GRAPHIC_DESIGNER), "task": "Crea el concepto visual y prompt de IA usando el copy del agente anterior como base."},
            ]
        elif wants_copy:
            steps = [{"step": 1, "agent": AgentRole.COPYWRITER,       "agent_name": _agent(AgentRole.COPYWRITER),       "task": request}]
        elif wants_design:
            steps = [{"step": 1, "agent": AgentRole.GRAPHIC_DESIGNER,  "agent_name": _agent(AgentRole.GRAPHIC_DESIGNER),  "task": request}]
        elif any(kw in request_lower for kw in lead_kw):
            steps = [{"step": 1, "agent": AgentRole.LEAD_QUALIFIER,    "agent_name": _agent(AgentRole.LEAD_QUALIFIER),    "task": request}]
        elif any(kw in request_lower for kw in ads_kw):
            steps = [{"step": 1, "agent": AgentRole.PERFORMANCE_ADS,   "agent_name": _agent(AgentRole.PERFORMANCE_ADS),   "task": request}]
        elif any(kw in request_lower for kw in social_kw):
            steps = [{"step": 1, "agent": AgentRole.SOCIAL_LISTENER,   "agent_name": _agent(AgentRole.SOCIAL_LISTENER),   "task": request}]
        elif any(kw in request_lower for kw in analyst_kw):
            steps = [{"step": 1, "agent": AgentRole.BUSINESS_ANALYST,  "agent_name": _agent(AgentRole.BUSINESS_ANALYST),  "task": request}]
        elif any(kw in request_lower for kw in sat_kw):
            steps = [{"step": 1, "agent": AgentRole.SAT_INTELLIGENCE,  "agent_name": _agent(AgentRole.SAT_INTELLIGENCE),  "task": request}]
        else:
            steps = [{"step": 1, "agent": AgentRole.COPYWRITER,        "agent_name": _agent(AgentRole.COPYWRITER),        "task": request}]

        agents_involved = [s["agent"] for s in steps]
        return OrchestrationPlan(
            original_request=request,
            analysis=f"Routing hacia: {[r.value for r in agents_involved]}",
            steps=steps,
            agents_involved=agents_involved,
        )

    # ─────────────────────────── Plan Execution ─────────────────────────────

    def _execute_plan(self, plan: OrchestrationPlan) -> Dict[str, str]:
        """Ejecuta el plan en secuencia, pasando el output de cada agente al siguiente."""
        results: Dict[str, str] = {}
        previous_output: Optional[str] = None

        for step in plan.steps:
            agent_role = step["agent"]
            agent = self.registry.get(agent_role)

            if not agent:
                console.print(f"[yellow]⚠ Agente {agent_role.value} no disponible, saltando...[/yellow]")
                continue

            # Si hay output del agente anterior, construir tarea encadenada
            if previous_output and len(plan.steps) > 1:
                task_description = (
                    f"SOLICITUD ORIGINAL: {plan.original_request}\n\n"
                    f"OUTPUT DEL AGENTE ANTERIOR ({list(results.keys())[-1]}):\n{previous_output}\n\n"
                    f"TU TAREA: {step.get('task', plan.original_request)}"
                )
            else:
                task_description = step.get("task", plan.original_request)

            with Progress(
                SpinnerColumn(),
                TextColumn(f"[bold]{agent.name}[/bold] trabajando..."),
                transient=True,
                console=console,
            ) as progress:
                progress.add_task("", total=None)
                result = agent.run(task_description, {"original_request": plan.original_request})

            results[agent_role.value] = result
            previous_output = result

            if self.verbose:
                console.print(f"[green]✓[/green] {agent.name} completado")

        return results

    def _synthesize_results(
        self,
        original_request: str,
        plan: OrchestrationPlan,
        results: Dict[str, str],
    ) -> str:
        """Sintetiza los resultados de múltiples agentes en una respuesta cohesiva."""
        if len(results) == 1:
            # Un solo agente, devolver directamente
            return list(results.values())[0]

        # Múltiples agentes: sintetizar
        if self._orchestrator_agent:
            results_str = "\n\n".join(
                f"### {role}:\n{result}"
                for role, result in results.items()
            )

            synthesis_prompt = f"""Se han obtenido resultados de múltiples agentes para esta solicitud:

SOLICITUD ORIGINAL: {original_request}

RESULTADOS DE AGENTES:
{results_str}

Por favor:
1. Integra los resultados de forma coherente y útil
2. Elimina redundancias
3. Resalta los puntos más importantes
4. Proporciona próximos pasos claros
5. Mantén un tono consistente con la marca heru"""

            return self._orchestrator_agent.run(synthesis_prompt, maintain_history=False)
        else:
            # Sin orquestador IA: concatenar con separadores
            parts = [f"## Resultado del Sistema Multi-Agente heru\n\n**Solicitud:** {original_request}\n"]
            for role, result in results.items():
                parts.append(f"---\n### {role.replace('_', ' ').title()}\n{result}")
            return "\n\n".join(parts)

    # ──────────────────────────── Display Utils ─────────────────────────────

    def _display_plan(self, plan: OrchestrationPlan):
        table = Table(title="Plan de Orquestación", border_style="cyan")
        table.add_column("Paso", style="bold", width=6)
        table.add_column("Agente", style="green")
        table.add_column("Acción")

        for step in plan.steps:
            table.add_row(
                str(step.get("step", "-")),
                step.get("agent_name", str(step.get("agent", ""))),
                step.get("task", "")[:80] + ("..." if len(step.get("task", "")) > 80 else ""),
            )

        console.print(table)

    def status(self):
        """Muestra el estado del sistema."""
        console.print("\n[bold cyan]Estado del Sistema Multi-Agente heru[/bold cyan]")
        console.print(f"Agentes registrados: {len(self.registry.list_agents())}")
        for agent_info in self.registry.list_agents():
            console.print(f"  [green]•[/green] {agent_info}")

        summary = self.task_queue.summary()
        console.print(f"\nTareas: {summary}")
