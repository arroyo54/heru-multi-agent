"""
Clase base para todos los agentes del sistema multi-agente de heru.app
"""
import yaml
import anthropic
from pathlib import Path
from typing import List, Dict, Any, Optional
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

from .models import AgentRole, AgentMessage, Task

console = Console()


class BaseAgent:
    """
    Clase base que todos los agentes especializados heredan.
    Gestiona la conexión con Claude, el historial de conversación,
    y la carga de configuración desde archivos YAML.
    """

    def __init__(
        self,
        config_path: str,
        client: anthropic.Anthropic,
        model: str = "claude-opus-4-6",
        max_tokens: int = 4096,
        verbose: bool = True,
    ):
        self.client = client
        self.model = model
        self.max_tokens = max_tokens
        self.verbose = verbose

        self.config = self._load_config(config_path)
        self.name: str = self.config["name"]
        self.role: str = self.config["role"]
        self.system_prompt: str = self._build_system_prompt()
        self.conversation_history: List[Dict[str, str]] = []

        if self.verbose:
            console.print(f"[green]✓[/green] Agente inicializado: [bold]{self.name}[/bold]")

    # ─────────────────────────── Config & Prompt ────────────────────────────

    def _load_config(self, config_path: str) -> dict:
        config_file = Path(config_path)
        if not config_file.exists():
            raise FileNotFoundError(f"Config no encontrado: {config_path}")
        with open(config_file, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def _load_heru_context(self) -> str:
        context_path = Path(__file__).parent.parent / "config" / "heru_context.yaml"
        with open(context_path, "r", encoding="utf-8") as f:
            ctx = yaml.safe_load(f)
        return ctx.get("summary", "heru.app - plataforma fiscal para trabajadores independientes de México")

    def _build_system_prompt(self) -> str:
        cfg = self.config
        heru_ctx = self._load_heru_context()

        objectives_str = "\n".join(f"  • {obj}" for obj in cfg.get("objectives", []))
        behavior = cfg.get("behavior_instructions", "")

        prompt = f"""# Agente: {cfg["name"]}

## Tu Rol
{cfg.get("role_description", "")}

## Tu Personalidad
{cfg.get("personality", "")}

## Contexto de heru.app
{heru_ctx}

## Tus Objetivos
{objectives_str}

## Instrucciones de Comportamiento
{behavior}

---
Siempre responde en español latinoamericano (mexicano). Sé conciso, directo y útil.
Nunca inventes datos, métricas o información que no hayas recibido en el contexto.
IMPORTANTE: Durante la ejecución NUNCA hagas preguntas. Trabaja con la información disponible y entrega el mejor resultado posible. Las dudas ya fueron resueltas antes de llegar aquí.
"""
        return prompt

    # ──────────────────────────── Core Methods ──────────────────────────────

    def run(
        self,
        task: str,
        context: Optional[Dict[str, Any]] = None,
        maintain_history: bool = False,
    ) -> str:
        """
        Ejecuta una tarea y devuelve la respuesta del agente.

        Args:
            task: La tarea o pregunta para el agente
            context: Contexto adicional (diccionario)
            maintain_history: Si True, mantiene el historial de la conversación
        """
        if not maintain_history:
            messages = []
        else:
            messages = self.conversation_history.copy()

        user_content = task
        if context:
            context_str = "\n".join(f"  - {k}: {v}" for k, v in context.items())
            user_content = f"{task}\n\n**Contexto adicional:**\n{context_str}"

        messages.append({"role": "user", "content": user_content})

        if self.verbose:
            console.print(
                Panel(
                    f"[bold yellow]{self.name}[/bold yellow] procesando tarea...",
                    border_style="yellow",
                    padding=(0, 1),
                )
            )

        response = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=self.system_prompt,
            messages=messages,
        )

        assistant_message = response.content[0].text

        if maintain_history:
            self.conversation_history.append({"role": "user", "content": user_content})
            self.conversation_history.append({"role": "assistant", "content": assistant_message})

        if self.verbose:
            console.print(
                Panel(
                    Markdown(assistant_message),
                    title=f"[bold green]{self.name}[/bold green]",
                    border_style="green",
                    padding=(1, 2),
                )
            )

        return assistant_message

    def run_with_tools(
        self,
        task: str,
        tools: List[Dict[str, Any]],
        context: Optional[Dict[str, Any]] = None,
    ) -> str:
        """
        Ejecuta una tarea con tool use de Claude.
        Maneja el loop de herramientas automáticamente.

        Args:
            task: La tarea para el agente
            tools: Lista de herramientas disponibles (formato Anthropic)
            context: Contexto adicional
        """
        user_content = task
        if context:
            context_str = "\n".join(f"  - {k}: {v}" for k, v in context.items())
            user_content = f"{task}\n\n**Contexto adicional:**\n{context_str}"

        messages = [{"role": "user", "content": user_content}]
        final_response = ""

        while True:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                system=self.system_prompt,
                tools=tools,
                messages=messages,
            )

            # Si no hay más tool use, obtener la respuesta final
            if response.stop_reason == "end_turn":
                for block in response.content:
                    if hasattr(block, "text"):
                        final_response = block.text
                break

            # Procesar tool use
            if response.stop_reason == "tool_use":
                messages.append({"role": "assistant", "content": response.content})
                tool_results = []

                for block in response.content:
                    if block.type == "tool_use":
                        tool_result = self._execute_tool(block.name, block.input)
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": str(tool_result),
                        })

                messages.append({"role": "user", "content": tool_results})
            else:
                # Stop inesperado
                break

        return final_response

    def _execute_tool(self, tool_name: str, tool_input: Dict[str, Any]) -> Any:
        """
        Ejecuta una herramienta. Las subclases deben sobrescribir este método.
        """
        return f"Tool '{tool_name}' no implementado en este agente."

    # ──────────────────────────── Conversation ──────────────────────────────

    def ask_clarifications(
        self,
        task: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> List[str]:
        """
        Pregunta al agente qué dudas tiene antes de ejecutar la tarea.
        Devuelve lista de preguntas (máx 3). Lista vacía = sin dudas.
        """
        prompt = f"""Antes de ejecutar la siguiente tarea, identifica qué información adicional necesitas para hacerlo bien.

TAREA: {task}

Responde ÚNICAMENTE con una lista numerada de preguntas concretas (máximo 3).
Si tienes suficiente información para ejecutar la tarea, responde exactamente: SIN DUDAS

No hagas preguntas genéricas. Solo pregunta lo que realmente cambia el resultado."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=512,
            system=self.system_prompt,
            messages=[{"role": "user", "content": prompt}],
        )
        text = response.content[0].text.strip()

        if "SIN DUDAS" in text.upper():
            return []

        import re
        questions = re.findall(r'\d+\.\s*(.+)', text)
        return [q.strip() for q in questions[:3] if q.strip()]

    def chat(self, user_message: str) -> str:
        """Modo conversacional: mantiene el historial automáticamente."""
        return self.run(user_message, maintain_history=True)

    def reset_conversation(self):
        """Limpia el historial de conversación."""
        self.conversation_history = []
        if self.verbose:
            console.print(f"[dim]{self.name}: historial de conversación limpiado[/dim]")

    # ────────────────────────────── Utils ───────────────────────────────────

    def get_info(self) -> Dict[str, Any]:
        """Devuelve información sobre el agente."""
        return {
            "name": self.name,
            "role": self.role,
            "model": self.model,
            "conversation_turns": len(self.conversation_history) // 2,
        }

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name='{self.name}' role='{self.role}'>"
