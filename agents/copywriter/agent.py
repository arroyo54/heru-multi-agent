"""
Agente Copywriter de Contenido para heru.app
"""
from pathlib import Path
from typing import Optional, Literal
import anthropic

from core.base_agent import BaseAgent
from core.models import ContentRequest


CONFIG_PATH = Path(__file__).parent / "config.yaml"

Platform = Literal["instagram", "facebook", "tiktok", "linkedin", "email", "ads"]
ContentType = Literal["educativo", "pain_point", "social_proof", "producto", "temporada", "meme"]


class CopywriterAgent(BaseAgent):
    """
    Agente especializado en crear copy y contenido para redes sociales,
    campañas de email y publicidad pagada de heru.app.
    """

    def __init__(self, client: anthropic.Anthropic, **kwargs):
        super().__init__(
            config_path=str(CONFIG_PATH),
            client=client,
            **kwargs,
        )

    def create_post(
        self,
        platform: Platform,
        topic: str,
        content_type: ContentType = "educativo",
        objective: str = "engagement",
        target_segment: Optional[str] = None,
        special_instructions: Optional[str] = None,
    ) -> str:
        """
        Crea un post completo para una plataforma específica.
        """
        context_parts = [f"Plataforma objetivo: {platform}"]
        if target_segment:
            context_parts.append(f"Segmento de audiencia: {target_segment}")
        if special_instructions:
            context_parts.append(f"Instrucciones especiales: {special_instructions}")

        prompt = f"""Crea un post para {platform.upper()} con estas especificaciones:

TEMA: {topic}
TIPO DE CONTENIDO: {content_type}
OBJETIVO: {objective}
{chr(10).join(context_parts)}

Entrega:

**📱 PLATAFORMA:** {platform.upper()}
**📌 TIPO:** {content_type}
**🎯 OBJETIVO:** {objective}

---

**COPY COMPLETO:**
[El texto completo del post, listo para publicar]

---

**HASHTAGS:**
[Si aplica para la plataforma]

---

**NOTAS PARA DISEÑO:**
[Descripción de qué imagen/video acompañaría este post]

---

**VARIANTE A/B:**
[Una versión alternativa con diferente hook o ángulo]"""

        return self.run(prompt)

    def create_content_calendar(
        self,
        week_number: int,
        platforms: list,
        campaign_theme: Optional[str] = None,
    ) -> str:
        """
        Crea un calendario de contenido para una semana.
        """
        platforms_str = ", ".join(platforms)
        theme_str = f"\nTEMA DE CAMPAÑA: {campaign_theme}" if campaign_theme else ""

        prompt = f"""Crea un calendario de contenido para la SEMANA {week_number} de heru.app:

PLATAFORMAS: {platforms_str}{theme_str}

Crea una tabla con:
| Día | Plataforma | Tipo | Tema | Hook principal | Objetivo |

Luego, para cada pieza, escribe el copy completo.
Asegúrate de:
1. Variedad de tipos de contenido (educativo, pain_point, producto, social_proof)
2. Consistencia en el mensaje de marca
3. Considerar el contexto fiscal del momento (fechas SAT relevantes)
4. Balance entre contenido de valor y contenido de conversión (70/30)"""

        return self.run(prompt)

    def create_ad_copy(
        self,
        platform: Literal["google", "meta", "tiktok"],
        campaign_objective: str,
        target_segment: str,
        budget_signal: Optional[str] = None,
    ) -> str:
        """
        Crea copy para campañas de publicidad pagada.
        """
        prompt = f"""Crea copy para un anuncio pagado en {platform.upper()}:

OBJETIVO DE CAMPAÑA: {campaign_objective}
SEGMENTO OBJETIVO: {target_segment}
{"PRESUPUESTO/CONTEXTO: " + budget_signal if budget_signal else ""}

Para {platform.upper()}, entrega:

**ANUNCIO 1 (Variante Principal)**
- Headline 1 (30 chars máx):
- Headline 2 (30 chars máx):
- Headline 3 (30 chars máx):
- Descripción 1 (90 chars máx):
- Descripción 2 (90 chars máx):
- CTA:
- URL display:

**ANUNCIO 2 (Variante A/B)**
[Mismo formato, ángulo diferente]

**ANUNCIO 3 (Variante Urgencia/FOMO)**
[Mismo formato, enfocado en urgencia]

**NOTAS DE TARGETING:**
[Sugerencias de keywords negativas, audiencias excluir, etc.]"""

        return self.run(prompt)

    def create_email_sequence(
        self,
        sequence_type: Literal["welcome", "nurturing", "re-engagement", "upsell"],
        num_emails: int = 3,
        target_segment: Optional[str] = None,
    ) -> str:
        """
        Crea una secuencia de emails de marketing.
        """
        prompt = f"""Crea una secuencia de {num_emails} emails de {sequence_type} para heru.app:

TIPO: {sequence_type}
NÚMERO DE EMAILS: {num_emails}
{"SEGMENTO: " + target_segment if target_segment else ""}

Para cada email entrega:

**EMAIL #X**
- Asunto principal:
- Asunto alternativo (A/B):
- Preview text:
- Cuerpo del email (HTML-friendly, con placeholders como {{nombre}}):
- CTA principal:
- CTA secundario (si aplica):
- Timing: (ej: Día 0, Día 3, Día 7)

Considera:
1. Progresión lógica del storytelling
2. Cada email debe tener un objetivo único
3. No ser spam: aportar valor en cada email
4. Personalización con el nombre del usuario"""

        return self.run(prompt)

    def create_tiktok_script(self, topic: str, target_segment: Optional[str] = None) -> str:
        """
        Crea un guión completo para un video de TikTok.
        """
        prompt = f"""Crea un guión para un TikTok de heru.app:

TEMA: {topic}
{"AUDIENCIA: " + target_segment if target_segment else ""}

Entrega el guión en este formato:

**TÍTULO DEL VIDEO:**
**DURACIÓN ESTIMADA:** [X segundos]
**HOOK VISUAL (0-3s):** [Qué se ve en pantalla]

---
GUIÓN COMPLETO:

[00:00-00:03] HOOK
Voz: "..."
Visual: [descripción]
Texto en pantalla: "..."

[00:03-00:20] DESARROLLO
Voz: "..."
Visual: [descripción]
Texto en pantalla: "..."

[00:20-00:45] SOLUCIÓN/VALOR
Voz: "..."
Visual: [descripción]
Texto en pantalla: "..."

[00:45-00:60] CTA
Voz: "..."
Visual: [descripción]
Texto en pantalla: "..."

---
**DESCRIPCIÓN DEL VIDEO:** [Para el caption de TikTok]
**HASHTAGS:** [10-15 hashtags relevantes]
**MÚSICA SUGERIDA:** [Tipo de música o trending sound]
**EFECTOS/TRANSICIONES:** [Sugerencias de edición]"""

        return self.run(prompt)

    def adapt_content(self, original_content: str, target_platform: Platform) -> str:
        """
        Adapta contenido existente para otra plataforma.
        """
        prompt = f"""Adapta este contenido para {target_platform.upper()}:

CONTENIDO ORIGINAL:
{original_content}

Adapta respetando:
1. Las convenciones de formato de {target_platform}
2. La longitud óptima para la plataforma
3. El tono apropiado para la audiencia de {target_platform}
4. Añadir o quitar hashtags según corresponda
5. Ajustar el CTA para el canal

Entrega el contenido adaptado listo para publicar."""

        return self.run(prompt)
