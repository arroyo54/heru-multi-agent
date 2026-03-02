"""
Envía mensajes al webhook de Google Chat para heru.app.
Maneja el límite de 4,000 caracteres por mensaje automáticamente.
"""
import os
import requests
from typing import Optional

CHUNK_SIZE = 3800  # Google Chat limit es ~4096, dejamos margen


def send_message(text: str, webhook_url: Optional[str] = None) -> bool:
    """Envía un mensaje de texto al canal de Google Chat."""
    url = webhook_url or os.environ.get("GOOGLE_CHAT_WEBHOOK_URL")
    if not url:
        print("⚠️  GOOGLE_CHAT_WEBHOOK_URL no configurada")
        return False
    try:
        response = requests.post(url, json={"text": text}, timeout=10)
        return response.status_code == 200
    except Exception as e:
        print(f"⚠️  Error enviando a Google Chat: {e}")
        return False


def send_report(
    full_report: str,
    title: str = "REPORTE SEMANAL SOCIAL LISTENER heru",
    date_str: str = "",
    webhook_url: Optional[str] = None,
) -> None:
    """
    Envía el reporte semanal al Google Chat.
    - Mensaje 1: Header con título y resumen ejecutivo (primeras 8 líneas)
    - Mensajes siguientes: Reporte completo en chunks si supera el límite
    """
    url = webhook_url or os.environ.get("GOOGLE_CHAT_WEBHOOK_URL")
    if not url:
        print("⚠️  GOOGLE_CHAT_WEBHOOK_URL no configurada — reporte no enviado")
        return

    # Extraer resumen ejecutivo (primeras líneas no vacías)
    summary_lines = [l for l in full_report.split("\n") if l.strip()][:8]
    summary = "\n".join(summary_lines)

    # Mensaje 1: Header
    header = f"📊 *{title}*"
    if date_str:
        header += f" — {date_str}"
    header += f"\n\n{summary}"
    send_message(header, url)

    # Mensajes siguientes: reporte completo en chunks
    chunks = [full_report[i:i + CHUNK_SIZE] for i in range(0, len(full_report), CHUNK_SIZE)]
    total = len(chunks)
    for i, chunk in enumerate(chunks):
        prefix = f"_{i + 1}/{total}_\n" if total > 1 else ""
        send_message(f"{prefix}{chunk}", url)

    print(f"  ✅ Enviado a Google Chat ({total + 1} mensaje(s))")
