"""
Agente Diseñador Gráfico de heru.app
"""
from pathlib import Path
from typing import Optional, List
import anthropic

from core.base_agent import BaseAgent


CONFIG_PATH = Path(__file__).parent / "config.yaml"


class GraphicDesignerAgent(BaseAgent):
    """
    Agente especializado en conceptualizar y describir assets visuales
    para heru.app. Genera prompts de IA, briefs de diseño y guiones visuales.
    """

    def __init__(self, client: anthropic.Anthropic, **kwargs):
        super().__init__(
            config_path=str(CONFIG_PATH),
            client=client,
            **kwargs,
        )

    def create_visual_concept(
        self,
        piece_type: str,
        platform: str,
        copy: Optional[str] = None,
        objective: str = "engagement",
        additional_requirements: Optional[str] = None,
    ) -> str:
        """
        Crea un concepto visual completo con brief y prompt de IA.

        Args:
            piece_type: carrusel, post, story, banner, ad, reel_thumbnail, etc.
            platform: instagram, facebook, tiktok, linkedin
            copy: El texto que acompañará la imagen
            objective: engagement, conversión, educativo, awareness
        """
        context_parts = []
        if copy:
            context_parts.append(f"COPY QUE ACOMPAÑARÁ:\n{copy}")
        if additional_requirements:
            context_parts.append(f"REQUISITOS ESPECIALES:\n{additional_requirements}")

        prompt = f"""Crea un concepto visual completo para heru.app:

TIPO DE PIEZA: {piece_type}
PLATAFORMA: {platform}
OBJETIVO: {objective}
{chr(10).join(context_parts)}

Entrega:

## 🎨 CONCEPTO VISUAL

**CONCEPTO CREATIVO:**
[Descripción del concepto e idea central]

**COMPOSICIÓN:**
[Cómo se organiza el espacio visual]

**PERSONAJE/SUJETO PRINCIPAL:**
[Descripción detallada si hay persona/personaje]

---

## 📐 ESPECIFICACIONES TÉCNICAS
- Formato: [dimensiones específicas]
- Ratio: [aspecto]
- Modo color: RGB, 72dpi para digital

---

## 🤖 PROMPT PARA IA (DALL-E / Midjourney / Stable Diffusion)

```
[Prompt en inglés, muy detallado, listo para usar]
```

**Versión negativa/exclusiones:**
```
[Lo que debe excluirse: --no ...]
```

---

## 📋 BRIEF PARA DISEÑADOR HUMANO

**Objetivo visual:** [Qué debe comunicar la imagen]
**Estilo de referencia:** [Referencias de estilo o marcas similares]
**Elementos obligatorios:** [Logo, colores de marca, textos fijos]
**Elementos opcionales:** [Lo que puede variar]
**Entregables esperados:** [Formatos y versiones]
**Deadline sugerido:** [Según urgencia]

---

## 🔄 VARIANTE B
[Segundo concepto alternativo con su propio prompt]"""

        return self.run(prompt)

    def create_carousel_storyboard(
        self,
        topic: str,
        num_slides: int = 7,
        copy_per_slide: Optional[List[str]] = None,
    ) -> str:
        """
        Crea un storyboard completo para un carrusel de Instagram/LinkedIn.
        """
        slides_info = ""
        if copy_per_slide:
            slides_info = "\n".join(
                f"Slide {i+1}: {text}" for i, text in enumerate(copy_per_slide)
            )

        prompt = f"""Crea un storyboard detallado para un carrusel de {num_slides} slides:

TEMA: {topic}
{"COPY POR SLIDE:" + chr(10) + slides_info if slides_info else ""}

Para CADA slide entrega:

---
**SLIDE [N]** {"(Cover)" if "1" else ""}
- **Texto:** [El copy del slide]
- **Visual principal:** [Descripción del elemento visual dominante]
- **Composición:** [Layout y distribución de elementos]
- **Fondo:** [Color, textura, patrón]
- **Iconos/Ilustraciones:** [Elementos decorativos]
- **Tipografía:** [Tamaño relativo, peso, color]
- **Prompt IA:** [Prompt específico para este slide]

Al final incluye:
**COHESIÓN VISUAL DEL CARRUSEL:**
[Cómo mantener coherencia visual entre todos los slides]

**PALETA DE COLORES UNIFICADA:**
[Colores hex específicos para toda la serie]"""

        return self.run(prompt)

    def generate_image_prompt(
        self,
        description: str,
        style: str = "flat illustration",
        platform: Optional[str] = None,
        mood: str = "empowering and friendly",
    ) -> str:
        """
        Genera un prompt optimizado para herramientas de generación de imágenes con IA.
        """
        prompt = f"""Genera un prompt profesional para generación de imagen con IA:

DESCRIPCIÓN DE LO QUE NECESITO:
{description}

ESTILO: {style}
{"PLATAFORMA: " + platform if platform else ""}
MOOD: {mood}

Entrega:

**PROMPT PRINCIPAL (inglés, para DALL-E 3 / Midjourney):**
```
[Prompt muy detallado: sujeto, acción, ambiente, iluminación, estilo, colores, mood]
```

**PROMPT MIDJOURNEY CON PARÁMETROS:**
```
[prompt] --ar [ratio] --style raw --v 6 --no [exclusiones]
```

**PROMPT STABLE DIFFUSION:**
```
[Positive prompt]
Negative prompt: [Negative prompt]
```

**TIPS DE USO:**
- Semilla sugerida: random / fija para consistencia
- Iteraciones recomendadas: X
- Ajustes si el resultado no es satisfactorio:"""

        return self.run(prompt)

    def create_ad_creative_brief(
        self,
        campaign: str,
        platform: str,
        objective: str,
        variants: int = 3,
    ) -> str:
        """
        Crea un brief completo de creativos para una campaña de ads.
        """
        creatives_section = "\n".join(
            f"### CREATIVO {i+1}\n"
            "**Concepto:** [Idea central]\n"
            "**Formato:** [dimensiones]\n"
            "**Imagen/Video:** [Descripción visual detallada]\n"
            "**Headline:**\n"
            "**Texto del anuncio:**\n"
            "**CTA:**\n"
            "**Prompt IA:**\n"
            "```\n[prompt]\n```\n---"
            for i in range(variants)
        )

        prompt = f"""Crea un brief completo de creativos para una campaña de ads de heru:

CAMPAÑA: {campaign}
PLATAFORMA: {platform}
OBJETIVO: {objective}
NÚMERO DE VARIANTES: {variants}

Entrega:

## BRIEF CREATIVO: {campaign}

**Objetivo de comunicación:**
**KPI principal:**
**Audiencia objetivo:**
**Mensaje clave:**
**Tono:**

---

{creatives_section}

**REGLAS DE MARCA PARA ESTA CAMPAÑA:**
- Logo: [Posición y tamaño]
- Colores obligatorios: #00C48C, #1A1D3B
- Disclaimer si aplica:
- Qué NO hacer:"""

        return self.run(prompt)

    def create_video_storyboard(
        self,
        script: str,
        platform: str = "tiktok",
        duration: str = "30-60 segundos",
    ) -> str:
        """
        Crea un storyboard visual para un video/Reel.
        """
        prompt = f"""Crea un storyboard visual detallado para este video de {platform}:

GUIÓN:
{script}

DURACIÓN: {duration}

Para cada escena entrega:

| # | Tiempo | Descripción Visual | Encuadre | Texto en Pantalla | Movimiento/Efecto |
|---|--------|-------------------|----------|-------------------|-------------------|

Luego, para las 3 escenas más importantes, entrega descripción visual completa
y prompt de IA para generar el frame o thumbnail representativo.

**ESTILO DE PRODUCCIÓN RECOMENDADO:**
**MÚSICA/AUDIO SUGERIDO:**
**EFECTOS DE EDICIÓN:**
**THUMBNAIL RECOMENDADO:**"""

        return self.run(prompt)
