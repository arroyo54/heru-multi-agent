"""
Generador de imágenes usando Gemini Flash Image Generation de Google.
Usa gemini-2.0-flash-exp-image-generation (disponible en free tier).
"""
import re
import os
from pathlib import Path
from datetime import datetime
from typing import Optional

try:
    from google import genai
    from google.genai import types
    _GENAI_AVAILABLE = True
except ImportError:
    _GENAI_AVAILABLE = False


# Aspect ratio hints para incluir en el prompt (Gemini no acepta parámetro directo)
PLATFORM_RATIO_HINTS = {
    "instagram": "square 1:1 aspect ratio",
    "facebook": "landscape 4:3 aspect ratio",
    "linkedin": "landscape 4:3 aspect ratio",
    "tiktok": "vertical 9:16 aspect ratio",
    "story": "vertical 9:16 aspect ratio",
    "instagram_story": "vertical 9:16 aspect ratio",
    "banner": "wide landscape 16:9 aspect ratio",
    "youtube": "wide landscape 16:9 aspect ratio",
    "default": "square 1:1 aspect ratio",
}

# Modelo principal — gemini-2.0-flash-exp-image-generation (free tier)
MODEL = "gemini-2.0-flash-exp-image-generation"


class ImageGenerator:
    """
    Genera imágenes con Gemini Flash Image Generation y las guarda en output/images/.
    Compatible con el free tier de Google AI Studio.
    """

    OUTPUT_DIR = Path("output/images")

    def __init__(self, api_key: Optional[str] = None):
        key = api_key or os.environ.get("GOOGLE_API_KEY")
        if not key:
            raise ValueError(
                "GOOGLE_API_KEY no encontrada. Agrégala al .env o como variable de entorno."
            )
        self.client = genai.Client(api_key=key)

    def generate(
        self,
        prompt: str,
        filename: Optional[str] = None,
        platform: str = "default",
        number_of_images: int = 1,
    ) -> list:
        """
        Genera imágenes con Gemini Flash y las guarda en output/images/.

        Args:
            prompt: Prompt en inglés para el modelo
            filename: Nombre base del archivo (sin extensión). Si no se da, usa timestamp.
            platform: instagram, facebook, tiktok, linkedin, story, banner.
            number_of_images: Cuántas variantes generar (cada una es una llamada separada)

        Returns:
            Lista de Path con las imágenes guardadas.
        """
        self.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        ratio_hint = PLATFORM_RATIO_HINTS.get(platform.lower(), PLATFORM_RATIO_HINTS["default"])
        full_prompt = f"{prompt}, {ratio_hint}"

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = filename or timestamp
        saved = []

        for i in range(number_of_images):
            response = self.client.models.generate_content(
                model=MODEL,
                contents=full_prompt,
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE", "TEXT"],
                ),
            )

            for part in response.candidates[0].content.parts:
                if part.inline_data and part.inline_data.data:
                    suffix = f"_{i+1}" if number_of_images > 1 else ""
                    path = self.OUTPUT_DIR / f"{base_name}{suffix}.png"
                    path.write_bytes(part.inline_data.data)
                    saved.append(path)
                    break

        return saved

    @staticmethod
    def extract_prompt(brief_text: str) -> Optional[str]:
        """
        Extrae el primer prompt de IA del texto generado por GraphicDesignerAgent.
        Busca el contenido dentro del primer bloque de código (```).
        """
        # Intenta encontrar el bloque de código después de secciones de prompt
        pattern = (
            r"(?:PROMPT PARA IA|PROMPT PRINCIPAL|PROMPT IMAGEN|PROMPT.*?IA)"
            r"[^\n]*\n```[^\n]*\n(.*?)```"
        )
        match = re.search(pattern, brief_text, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(1).strip()

        # Fallback: primer bloque de código disponible
        fallback = re.search(r"```[^\n]*\n(.*?)```", brief_text, re.DOTALL)
        if fallback:
            return fallback.group(1).strip()

        return None

    @staticmethod
    def is_available() -> bool:
        """Retorna True si GOOGLE_API_KEY está configurada y google-genai instalado."""
        return _GENAI_AVAILABLE and bool(os.environ.get("GOOGLE_API_KEY"))
