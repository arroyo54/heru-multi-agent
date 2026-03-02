"""
Sistema Multi-Agente heru.app
Punto de entrada principal del sistema.

Uso:
    python main.py                    # Modo interactivo (chat con orquestador)
    python main.py --demo             # Ejecuta demos de todos los agentes
    python main.py --agent <nombre>   # Habla directamente con un agente
"""
import os
import sys
import argparse
from pathlib import Path
from dotenv import load_dotenv
import anthropic
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown

# ─── Setup ───────────────────────────────────────────────────────────────────

load_dotenv()
console = Console()

# ─── Agent imports ───────────────────────────────────────────────────────────

from core.orchestration import Orchestrator
from core.models import AgentRole
from core.image_generator import ImageGenerator
from agents.orchestrator.agent import OrchestratorAgent
from agents.lead_qualifier.agent import LeadQualifierAgent
from agents.copywriter.agent import CopywriterAgent
from agents.graphic_designer.agent import GraphicDesignerAgent
from agents.social_listener.agent import SocialListenerAgent
from agents.performance_ads.agent import PerformanceAdsAgent
from agents.business_analyst.agent import BusinessAnalystAgent
from agents.sat_intelligence.agent import SATIntelligenceAgent


# ─── System Builder ──────────────────────────────────────────────────────────

def build_system(verbose: bool = True) -> Orchestrator:
    """
    Construye e inicializa el sistema completo de agentes.
    Retorna el Orchestrator listo para usar.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        console.print("[red]❌ Error: ANTHROPIC_API_KEY no encontrada en .env[/red]")
        console.print("Copia .env.example a .env y agrega tu API key")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    model = os.getenv("MODEL", "claude-opus-4-6")

    # Imagen 3 (Google) — opcional, solo si hay GOOGLE_API_KEY
    imagen = None
    if ImageGenerator.is_available():
        try:
            imagen = ImageGenerator()
            console.print("[green]✓ Google Imagen 3 conectado — el agente de diseño generará imágenes automáticamente[/green]")
        except Exception as e:
            console.print(f"[yellow]⚠ Imagen 3 no disponible: {e}[/yellow]")
    else:
        console.print("[dim]ℹ GOOGLE_API_KEY no configurada — el agente de diseño generará solo briefs de texto[/dim]")

    console.print(
        Panel(
            f"[bold green]🚀 Sistema Multi-Agente heru.app[/bold green]\n"
            f"Modelo: [cyan]{model}[/cyan]",
            border_style="green",
        )
    )

    # Inicializar orquestador
    orchestrator = Orchestrator(client=client, verbose=verbose)

    # Inicializar y registrar todos los agentes
    agents = {
        AgentRole.ORCHESTRATOR: OrchestratorAgent(client=client, model=model, verbose=False),
        AgentRole.LEAD_QUALIFIER: LeadQualifierAgent(client=client, model=model, verbose=verbose),
        AgentRole.COPYWRITER: CopywriterAgent(client=client, model=model, verbose=verbose),
        AgentRole.GRAPHIC_DESIGNER: GraphicDesignerAgent(client=client, model=model, verbose=verbose, image_generator=imagen),
        AgentRole.SOCIAL_LISTENER: SocialListenerAgent(client=client, model=model, verbose=verbose),
        AgentRole.PERFORMANCE_ADS: PerformanceAdsAgent(client=client, model=model, verbose=verbose),
        AgentRole.BUSINESS_ANALYST: BusinessAnalystAgent(client=client, model=model, verbose=verbose),
        AgentRole.SAT_INTELLIGENCE: SATIntelligenceAgent(client=client, model=model, verbose=verbose),
    }

    for role, agent in agents.items():
        orchestrator.register_agent(role, agent)

    # Setup del agente orquestador de IA
    orchestrator_config = Path("agents/orchestrator/config.yaml")
    if orchestrator_config.exists():
        orchestrator.setup_orchestrator_agent(str(orchestrator_config))

    orchestrator.status()
    return orchestrator


# ─── Demo Functions ──────────────────────────────────────────────────────────

def run_demos(orchestrator: Orchestrator):
    """Ejecuta demos de cada agente para verificar que el sistema funciona."""

    demos = [
        {
            "title": "DEMO 1: Lead Qualifier",
            "agent": AgentRole.LEAD_QUALIFIER,
            "task": """Califica este lead:
Nombre: Carlos Mendoza
Ocupación: Conductor de Uber (tiempo completo, 3 años)
Ingresos aproximados: $18,000 MXN/mes
RFC: Dice que tiene pero nunca ha declarado
Situación: Recibió un correo del SAT hace 2 semanas que lo asustó
Canal: Instagram DM, preguntó "¿heru me puede ayudar con el SAT?"
""",
        },
        {
            "title": "DEMO 2: Copywriter",
            "agent": AgentRole.COPYWRITER,
            "task": """Crea un post para Instagram sobre el siguiente tema:
La declaración anual del SAT vence en abril y muchos freelancers la están
dejando para el último momento. Necesitamos un post que genere urgencia
sin asustar, para la audiencia de diseñadores y creativos freelance.""",
        },
        {
            "title": "DEMO 3: Graphic Designer",
            "agent": AgentRole.GRAPHIC_DESIGNER,
            "task": """Crea el concepto visual y prompt de IA para este post de Instagram:
Es un post educativo sobre "5 deducciones fiscales que los freelancers nunca usan".
El copy menciona laptop, celular, internet, café de trabajo y suscripciones digitales.
Necesito una imagen principal para el carrusel (slide 1/5).""",
        },
        {
            "title": "DEMO 4: Social Listener",
            "agent": AgentRole.SOCIAL_LISTENER,
            "task": """Analiza estas menciones recientes de heru.app:

Tweet 1: "@heru_app me salvaron la vida! llevaba 2 años sin declarar y ahora estoy al corriente 🙌 #freelancer"
Tweet 2: "¿alguien ha usado heru? vi un anuncio pero no sé si vale la pena vs mi contador"
Facebook post: "Tiene alguien experiencia con heru.app? mi esposo maneja uber y le llegó carta del sat"
Twitter: "heru tardó 3 días en responderme por chat, eso no está bien para una app de tecnología 😤"
Instagram comment: "yo llevo 6 meses con heru y cero problemas, super recomendada!"
Reddit r/mexico: "¿qué tan confiable es heru para declarar? o mejor busco contador"

Período: últimas 48 horas | Plataforma: múltiples""",
        },
        {
            "title": "DEMO 5: Performance Ads",
            "agent": AgentRole.PERFORMANCE_ADS,
            "task": """Genera un análisis de performance basado en estos datos ficticios:

SEMANA: 17-23 Feb 2026
Google Ads:
- Gasto: $45,000 MXN
- Impresiones: 380,000
- Clics: 9,500 (CTR: 2.5%)
- Conversiones (registros): 180
- CPL: $250 MXN
- Quality Score promedio: 6.8

Meta Ads:
- Gasto: $38,000 MXN
- Alcance: 280,000
- Clics: 7,200 (CTR: 2.1%)
- Leads formulario: 220
- CPL: $173 MXN
- Frequency: 3.2

Total: Inversión $83,000 | Leads: 400 | CPL promedio: $207.5 MXN
Clientes de pago esta semana: 48 | CAC: $1,729 MXN
Revenue nuevos clientes: $280,000 MXN | ROAS: 3.37x""",
        },
    ]

    for demo in demos:
        console.print(f"\n[bold cyan]{'='*60}[/bold cyan]")
        console.print(f"[bold yellow]{demo['title']}[/bold yellow]")
        console.print(f"[bold cyan]{'='*60}[/bold cyan]\n")

        result = orchestrator.delegate(
            role=demo["agent"],
            task=demo["task"],
        )

        input("\n[Presiona Enter para continuar al siguiente demo...]")


# ─── Interactive Mode ─────────────────────────────────────────────────────────

def run_interactive(orchestrator: Orchestrator):
    """Modo interactivo: el usuario escribe solicitudes y el orquestador las procesa."""

    console.print(
        Panel(
            "[bold]Modo Interactivo del Sistema Multi-Agente heru.app[/bold]\n\n"
            "Escribe cualquier solicitud y el sistema la delegará al agente correcto.\n"
            "Comandos especiales:\n"
            "  /status  → Ver estado del sistema\n"
            "  /agente <nombre> <tarea>  → Hablar directamente con un agente\n"
            "     Agentes: leads, copy, diseno, social, ads, analyst, sat, fiscal\n"
            "  /demo    → Ejecutar demos\n"
            "  /salir   → Cerrar el sistema",
            border_style="cyan",
        )
    )

    agent_map = {
        "leads": AgentRole.LEAD_QUALIFIER,
        "lead": AgentRole.LEAD_QUALIFIER,
        "qualifier": AgentRole.LEAD_QUALIFIER,
        "copy": AgentRole.COPYWRITER,
        "copywriter": AgentRole.COPYWRITER,
        "diseno": AgentRole.GRAPHIC_DESIGNER,
        "diseño": AgentRole.GRAPHIC_DESIGNER,
        "designer": AgentRole.GRAPHIC_DESIGNER,
        "social": AgentRole.SOCIAL_LISTENER,
        "listener": AgentRole.SOCIAL_LISTENER,
        "ads": AgentRole.PERFORMANCE_ADS,
        "performance": AgentRole.PERFORMANCE_ADS,
        "analyst": AgentRole.BUSINESS_ANALYST,
        "ba": AgentRole.BUSINESS_ANALYST,
        "business": AgentRole.BUSINESS_ANALYST,
        "sat": AgentRole.SAT_INTELLIGENCE,
        "fiscal": AgentRole.SAT_INTELLIGENCE,
        "inteligencia": AgentRole.SAT_INTELLIGENCE,
    }

    while True:
        try:
            user_input = Prompt.ask("\n[bold cyan]heru[/bold cyan]").strip()

            if not user_input:
                continue

            if user_input.lower() in ["/salir", "/exit", "/quit", "q"]:
                console.print("[yellow]Hasta luego! 👋[/yellow]")
                break

            elif user_input.lower() == "/status":
                orchestrator.status()

            elif user_input.lower() == "/demo":
                run_demos(orchestrator)

            elif user_input.lower().startswith("/agente "):
                parts = user_input[8:].strip().split(" ", 1)
                if len(parts) < 2:
                    console.print("[red]Uso: /agente <nombre> <tarea>[/red]")
                    continue
                agent_key, task = parts[0].lower(), parts[1]
                if agent_key not in agent_map:
                    console.print(f"[red]Agente no reconocido. Opciones: {', '.join(agent_map.keys())}[/red]")
                    continue
                result = orchestrator.delegate(agent_map[agent_key], task)

            else:
                # Orquestación completa
                result = orchestrator.process(user_input)

        except KeyboardInterrupt:
            console.print("\n[yellow]Interrumpido. Escribe /salir para cerrar.[/yellow]")
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")


# ─── CLI Entry Point ──────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Sistema Multi-Agente heru.app",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python main.py                    Modo interactivo
  python main.py --demo             Ejecutar todos los demos
  python main.py --agent leads      Hablar directamente con el Lead Qualifier
  python main.py --agent analyst    Hablar directamente con el Business Analyst
  python main.py --agent sat        Hablar directamente con el SAT Intelligence
  python main.py --quiet            Reducir output verbose
        """,
    )
    parser.add_argument("--demo", action="store_true", help="Ejecutar demos de todos los agentes")
    parser.add_argument(
        "--agent",
        choices=["leads", "copy", "diseno", "social", "ads", "analyst", "sat"],
        help="Hablar directamente con un agente específico",
    )
    parser.add_argument("--quiet", action="store_true", help="Reducir output verbose")
    args = parser.parse_args()

    verbose = not args.quiet
    orchestrator = build_system(verbose=verbose)

    if args.demo:
        run_demos(orchestrator)
    elif args.agent:
        agent_map = {
            "leads": AgentRole.LEAD_QUALIFIER,
            "copy": AgentRole.COPYWRITER,
            "diseno": AgentRole.GRAPHIC_DESIGNER,
            "social": AgentRole.SOCIAL_LISTENER,
            "ads": AgentRole.PERFORMANCE_ADS,
            "analyst": AgentRole.BUSINESS_ANALYST,
            "sat": AgentRole.SAT_INTELLIGENCE,
        }
        role = agent_map[args.agent]
        console.print(f"[bold]Modo directo: {role.value}[/bold]")
        console.print("Escribe 'salir' para terminar.\n")
        while True:
            task = Prompt.ask("Tu tarea").strip()
            if task.lower() in ["salir", "exit", "q"]:
                break
            orchestrator.delegate(role, task)
    else:
        run_interactive(orchestrator)


if __name__ == "__main__":
    main()
