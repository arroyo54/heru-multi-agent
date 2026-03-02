"""
Integración con Google Sheets para el reporte semanal del Social Listener.

Setup requerido (una sola vez):
1. Ve a console.cloud.google.com
2. Crea un Service Account (IAM → Service Accounts → Create)
3. Descarga el JSON de credenciales
4. Guárdalo como credentials/google_sheets.json en el proyecto
5. En tu Google Sheet → Compartir → agrega el email del service account como Editor
6. Copia el ID del Sheet (la parte larga en la URL) al .env como GOOGLE_SHEETS_ID

Alternativa: si tienes GOOGLE_API_KEY ya configurada, puedes activar Sheets API
en el mismo proyecto y usar esa key (solo lectura pública).
"""
import os
import json
from pathlib import Path
from datetime import datetime
from typing import Optional

try:
    import gspread
    from google.oauth2.service_account import Credentials
    GSPREAD_AVAILABLE = True
except ImportError:
    GSPREAD_AVAILABLE = False


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]

CREDENTIALS_PATH = Path("credentials/google_sheets.json")

# Nombres de las pestañas
TAB_DASHBOARD   = "Dashboard"
TAB_BRAND       = "Menciones heru"
TAB_ECOSYSTEM   = "Insights Ecosistema"
TAB_CONTENT     = "Oportunidades Contenido"
TAB_RAW         = "Raw Data"


def is_available() -> bool:
    """True si gspread está instalado, hay credenciales y GOOGLE_SHEETS_ID."""
    return (
        GSPREAD_AVAILABLE
        and CREDENTIALS_PATH.exists()
        and bool(os.environ.get("GOOGLE_SHEETS_ID"))
    )


def _get_client():
    creds = Credentials.from_service_account_file(str(CREDENTIALS_PATH), scopes=SCOPES)
    return gspread.authorize(creds)


def _get_or_create_tab(sheet, title: str, headers: list) -> gspread.Worksheet:
    """Obtiene la pestaña o la crea con headers si no existe."""
    try:
        return sheet.worksheet(title)
    except gspread.WorksheetNotFound:
        ws = sheet.add_worksheet(title=title, rows=1000, cols=20)
        ws.append_row(headers, value_input_option="USER_ENTERED")
        return ws


def upload_weekly_report(
    date_str: str,
    brand_analysis: str,
    ecosystem_analysis: str,
    raw_data: dict,
    total_mentions: int,
    heru_mentions: int,
    sheets_id: Optional[str] = None,
) -> Optional[str]:
    """
    Sube el reporte semanal completo a Google Sheets.

    Returns:
        URL del Sheet si fue exitoso, None si falló o no está configurado.
    """
    if not is_available():
        print("  ⚠️  Google Sheets no configurado — reporte guardado solo localmente")
        return None

    sid = sheets_id or os.environ.get("GOOGLE_SHEETS_ID")

    try:
        gc = _get_client()
        sheet = gc.open_by_key(sid)
        week = datetime.now().strftime("%d/%m/%Y")

        # ── Tab Dashboard: una fila por semana ───────────────────────────────
        dashboard = _get_or_create_tab(sheet, TAB_DASHBOARD, [
            "Semana", "Total menciones", "Menciones heru", "Share of voice %",
            "Plataformas activas", "Top insight"
        ])
        platforms_active = ", ".join(k for k, v in raw_data.items() if v)
        top_insight = ecosystem_analysis.split("\n")[0][:120] if ecosystem_analysis else ""
        sov = round((heru_mentions / total_mentions * 100), 1) if total_mentions > 0 else 0
        dashboard.append_row(
            [week, total_mentions, heru_mentions, f"{sov}%", platforms_active, top_insight],
            value_input_option="USER_ENTERED",
        )

        # ── Tab Menciones heru ────────────────────────────────────────────────
        brand_ws = _get_or_create_tab(sheet, TAB_BRAND, ["Semana", "Análisis"])
        brand_ws.append_row([week, brand_analysis], value_input_option="USER_ENTERED")

        # ── Tab Insights Ecosistema ───────────────────────────────────────────
        eco_ws = _get_or_create_tab(sheet, TAB_ECOSYSTEM, ["Semana", "Análisis"])
        eco_ws.append_row([week, ecosystem_analysis], value_input_option="USER_ENTERED")

        # ── Tab Raw Data: menciones brutas ────────────────────────────────────
        raw_ws = _get_or_create_tab(sheet, TAB_RAW, ["Semana", "Plataforma", "Autor", "Texto"])
        rows = []
        for platform, items in raw_data.items():
            for item in items[:30]:
                from core.connectors.apify import extract_text, extract_author
                text = extract_text(item, platform)
                author = extract_author(item)
                rows.append([week, platform, author, text])
        if rows:
            raw_ws.append_rows(rows, value_input_option="USER_ENTERED")

        url = f"https://docs.google.com/spreadsheets/d/{sid}"
        print(f"  ✅ Subido a Google Sheets: {url}")
        return url

    except Exception as e:
        print(f"  ⚠️  Error subiendo a Sheets: {e}")
        return None
