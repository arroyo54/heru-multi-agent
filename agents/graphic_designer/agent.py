"""
Agente Diseñador Gráfico de heru.app
Genera conceptos visuales, prompts de IA y — si hay GOOGLE_API_KEY —
produce las imágenes directamente con Google Imagen 3.
"""
from pathlib import Path
from typing import Optional, List
import anthropic

from core.base_agent import BaseAgent
from core.image_generator import ImageGenerator


CONFIG_PATH = Path(__file__).parent / "config.yaml"


class GraphicDesignerAgent(BaseAgent):
    """
    Agente especializado en conceptualizar y describir assets visuales
    para heru.app. Si se le pasa un ImageGenerator, también genera las
    imágenes directamente con Google Imagen 3 y las guarda en output/images/.
    """

    def __init__(
        self,
        client: anthropic.Anthropic,
        image_generator: Optional[ImageGenerator] = None,
        **kwargs,
    ):
        super().__init__(
            config_path=str(CONFIG_PATH),
            client=client,
            **kwargs,
        )
        self.imagen = image_generator

    def create_visual_concept(
        self,
        piece_type: str,
        platform: str,
        copy: Optional[str] = None,
        objective: str = "engagement",
        additional_requirements: Optional[str] = None,
        generate_image: bool = True,
    ) -> str:
        """
        Crea un concepto visual completo con brief y prompt de IA.
        Si hay un ImageGenerator configurado y generate_image=True,
        también genera la imagen con Imagen 3 y la guarda en output/images/.

        Args:
            piece_type: carrusel, post, story, banner, ad, reel_thumbnail, etc.
            platform: instagram, facebook, tiktok, linkedin
            copy: El texto que acompañará la imagen
            objective: engagement, conversión, educativo, awareness
            generate_image: Si True y hay ImageGenerator, genera la imagen automáticamente
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

## 🤖 PROMPT PARA IA (Imagen 3 / Midjourney / Stable Diffusion)

```
[Prompt en inglés, muy detallado, optimizado para Imagen 3 de Google. Incluir: sujeto, acción, ambiente, iluminación, estilo fotográfico o ilustración, colores de marca (#1790EC azul heru, #0C3961 azul oscuro), mood empoderador y cercano]
```

**Versión negativa/exclusiones:**
```
[Lo que debe excluirse: texto, watermarks, distorsiones, colores fuera de marca]
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

        brief = self.run(prompt)

        # Generar imagen con Imagen 3 si está disponible
        if generate_image and self.imagen:
            imagen_prompt = ImageGenerator.extract_prompt(brief)
            if imagen_prompt:
                filename = f"{platform}_{piece_type}".replace(" ", "_").lower()
                try:
                    paths = self.imagen.generate(
                        prompt=imagen_prompt,
                        filename=filename,
                        platform=platform,
                    )
                    paths_str = "\n".join(f"  - {p}" for p in paths)
                    brief += f"\n\n---\n\n## 🖼️ IMAGEN GENERADA CON IMAGEN 3\n{paths_str}"
                except Exception as e:
                    brief += f"\n\n---\n\n⚠️ **Imagen no generada:** {e}"

        return brief

    def generate_image(
        self,
        prompt: str,
        platform: str = "instagram",
        filename: Optional[str] = None,
        number_of_images: int = 1,
    ) -> str:
        """
        Genera una imagen directamente con Imagen 3 a partir de un prompt.
        No necesita pasar por el brief de Claude.

        Args:
            prompt: Prompt en inglés para Imagen 3
            platform: instagram, facebook, tiktok, linkedin, story, banner
            filename: Nombre base del archivo (sin extensión)
            number_of_images: Cuántas variantes generar (1-4)

        Returns:
            String con los paths de las imágenes generadas.
        """
        if not self.imagen:
            return "⚠️ ImageGenerator no configurado. Agrega GOOGLE_API_KEY al .env."

        try:
            paths = self.imagen.generate(
                prompt=prompt,
                filename=filename,
                platform=platform,
                number_of_images=number_of_images,
            )
            paths_str = "\n".join(f"  - {p}" for p in paths)
            return f"## 🖼️ Imagen(s) generada(s) con Imagen 3\n{paths_str}"
        except Exception as e:
            return f"⚠️ Error generando imagen: {e}"

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
