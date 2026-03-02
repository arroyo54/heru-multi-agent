"""
Reporte semanal del Social Listener de heru.app.

Estructura:
  Google Chat → Resumen ejecutivo corto (menciones heru + top insights ecosistema)
  Google Sheets → Reporte completo con análisis, raw data y dashboard

Uso:
  python scripts/weekly_report.py            # corre y manda todo
  python scripts/weekly_report.py --preview  # muestra el resumen aquí, NO manda a Chat
  python scripts/weekly_report.py --quora    # corre solo el reporte quincenal de Quora
"""
import os
import sys
import argparse
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv
if Path(".env").exists():
    load_dotenv()

import anthropic
from typing import Optional
from agents.social_listener.agent import SocialListenerAgent
from core.connectors.apify import (
    ApifyConnector, BRAND_QUERIES, ECOSYSTEM_QUERIES,
    extract_text, extract_author, scrape_reddit, scrape_youtube,
)
from core.google_chat import send_message
from core.google_sheets import upload_weekly_report, is_available as sheets_available


# ─── Formateo de menciones para Claude ───────────────────────────────────────

def format_mentions(data: dict) -> str:
    LABELS = {
        "twitter": "TWITTER/X", "tiktok": "TIKTOK", "instagram": "INSTAGRAM",
        "facebook": "FACEBOOK GRUPOS", "youtube": "YOUTUBE",
        "reddit": "REDDIT", "quora": "QUORA",
    }
    sections = []
    for platform, items in data.items():
        if not items:
            continue
        label = LABELS.get(platform, platform.upper())
        sections.append(f"=== {label} ({len(items)} menciones) ===")
        for item in items[:20]:
            text = extract_text(item, platform)
            author = extract_author(item)
            sections.append(f"- @{author}: {text}")
        sections.append("")
    return "\n".join(sections)


# ─── Resumen ejecutivo para Google Chat ──────────────────────────────────────

def build_chat_summary(
    brand_analysis: str,
    ecosystem_analysis: str,
    total: int,
    heru_count: int,
    sheets_url: Optional[str] = None,
) -> str:
    """Construye el mensaje corto para Google Chat (máx ~700 chars)."""
    from typing import Optional

    week = datetime.now().strftime("%d/%m/%Y")

    # Extraer top 3 insights del análisis de ecosistema
    insights = []
    capture = False
    for line in ecosystem_analysis.split("\n"):
        if "INSIGHTS CLAVE" in line.upper():
            capture = True
            continue
        if capture and line.strip().startswith(("1.", "2.", "3.", "-", "•")):
            clean = line.strip().lstrip("123.-•• ").strip()
            if clean:
                insights.append(clean[:100])
        if len(insights) >= 3:
            break

    insights_text = "\n".join(f"• {i}" for i in insights) if insights else "• Ver Sheets para análisis completo"

    sov = f"{round(heru_count / total * 100, 1)}%" if total > 0 else "0%"

    msg = (
        f"📊 *SOCIAL LISTENING heru* | {week}\n\n"
        f"*🏷️ MENCIONES HERU*\n"
        f"• {heru_count} menciones directas | Share of voice: {sov}\n\n"
        f"*🔍 TOP INSIGHTS DEL ECOSISTEMA*\n"
        f"{insights_text}\n\n"
        f"*Total menciones analizadas:* {total}"
    )

    if sheets_url:
        msg += f"\n\n📊 *Reporte completo →* {sheets_url}"

    return msg


# ─── Recolección de datos ─────────────────────────────────────────────────────

def collect_data() -> tuple:
    """
    Retorna (brand_data, ecosystem_data) — dos dicts separados.
    brand_data: menciones directas de heru
    ecosystem_data: conversaciones del ecosistema
    """
    connector = ApifyConnector()
    brand_data = {}
    ecosystem_data = {}

    # ── TRACK A: Brand ────────────────────────────────────────────────────────
    print("\n  [Brand monitoring]")

    print("    📡 Twitter/X (heru)...", end=" ", flush=True)
    brand_data["twitter"] = connector.scrape_twitter(BRAND_QUERIES["twitter"], max_items=30)
    print(len(brand_data["twitter"]))

    print("    📡 TikTok (heru)...", end=" ", flush=True)
    brand_data["tiktok"] = connector.scrape_tiktok(BRAND_QUERIES["tiktok"], max_items=20)
    print(len(brand_data["tiktok"]))

    print("    📡 Instagram (heru)...", end=" ", flush=True)
    brand_data["instagram"] = connector.scrape_instagram(BRAND_QUERIES["instagram"], max_items=20)
    print(len(brand_data["instagram"]))

    # ── TRACK B: Ecosystem ────────────────────────────────────────────────────
    print("\n  [Ecosystem listening]")

    print("    📡 Reddit...", end=" ", flush=True)
    ecosystem_data["reddit"] = scrape_reddit(
        ECOSYSTEM_QUERIES["reddit_subreddits"],
        ECOSYSTEM_QUERIES["reddit_keywords"],
        max_posts=30,
    )
    print(len(ecosystem_data["reddit"]))

    print("    📡 YouTube (Data API gratis)...", end=" ", flush=True)
    ecosystem_data["youtube"] = scrape_youtube(ECOSYSTEM_QUERIES["youtube"], max_results=20)
    print(len(ecosystem_data["youtube"]))

    print("    📡 TikTok (ecosistema)...", end=" ", flush=True)
    ecosystem_data["tiktok"] = connector.scrape_tiktok(ECOSYSTEM_QUERIES["tiktok"], max_items=40)
    print(len(ecosystem_data["tiktok"]))

    print("    📡 Facebook grupos...", end=" ", flush=True)
    ecosystem_data["facebook"] = connector.scrape_facebook_groups(
        ECOSYSTEM_QUERIES["facebook_groups"], max_posts=25
    )
    print(len(ecosystem_data["facebook"]))

    print("    📡 Twitter/X (ecosistema)...", end=" ", flush=True)
    ecosystem_data["twitter"] = connector.scrape_twitter(ECOSYSTEM_QUERIES["twitter"], max_items=40)
    print(len(ecosystem_data["twitter"]))

    return brand_data, ecosystem_data


# ─── Reporte principal ────────────────────────────────────────────────────────

def run_weekly_report(preview: bool = False):
    """
    preview=True → muestra el resumen en consola, NO envía a Google Chat.
    preview=False → envía a Google Chat (solo cuando el usuario lo indique).
    """
    now = datetime.now()
    week_label = now.strftime("semana del %d de %B %Y")

    print(f"\n{'='*55}")
    print(f"🚀 REPORTE SEMANAL heru — {now.strftime('%A %d/%m/%Y %H:%M')}")
    print('='*55)

    # 1. Recolectar
    print("\n[1/5] Recopilando menciones...")
    brand_data, ecosystem_data = collect_data()

    heru_count = sum(len(v) for v in brand_data.values())
    eco_count = sum(len(v) for v in ecosystem_data.values())
    total = heru_count + eco_count
    print(f"\n  ✅ heru: {heru_count} menciones | Ecosistema: {eco_count} menciones\n")

    # 2. Analizar con Claude
    print("[2/5] Analizando con Social Listener Agent...")
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    client = anthropic.Anthropic(api_key=api_key)
    agent = SocialListenerAgent(client=client, model="claude-opus-4-6", verbose=False)

    brand_text = format_mentions(brand_data)
    eco_text = format_mentions(ecosystem_data)

    brand_analysis = (
        agent.analyze_brand_mentions(brand_text, week_label)
        if heru_count > 0
        else "Sin menciones directas de heru esta semana."
    )
    ecosystem_analysis = agent.analyze_ecosystem_insights(eco_text, week_label)

    # 3. Guardar localmente
    print("[3/5] Guardando reporte local...")
    reports_dir = Path("output/reports")
    reports_dir.mkdir(parents=True, exist_ok=True)
    date_slug = now.strftime("%Y%m%d")

    full_report = f"# SOCIAL LISTENING heru — {week_label}\n\n"
    full_report += f"## MENCIONES DE HERU\n\n{brand_analysis}\n\n"
    full_report += f"## INSIGHTS DEL ECOSISTEMA\n\n{ecosystem_analysis}\n"

    report_path = reports_dir / f"social_report_{date_slug}.md"
    report_path.write_text(full_report, encoding="utf-8")
    print(f"  💾 Guardado en: {report_path}")

    # 4. Subir a Google Sheets
    print("[4/5] Subiendo a Google Sheets...")
    all_raw = {**brand_data, **ecosystem_data}
    sheets_url = upload_weekly_report(
        date_str=now.strftime("%d/%m/%Y"),
        brand_analysis=brand_analysis,
        ecosystem_analysis=ecosystem_analysis,
        raw_data=all_raw,
        total_mentions=total,
        heru_mentions=heru_count,
    )

    # 5. Construir resumen para Chat
    print("[5/5] Construyendo resumen ejecutivo...")
    chat_msg = build_chat_summary(
        brand_analysis=brand_analysis,
        ecosystem_analysis=ecosystem_analysis,
        total=total,
        heru_count=heru_count,
        sheets_url=sheets_url,
    )

    print(f"\n{'─'*55}")
    print("RESUMEN EJECUTIVO PARA GOOGLE CHAT:")
    print('─'*55)
    print(chat_msg)
    print('─'*55)

    if preview:
        print("\n[MODO PREVIEW] No se envió a Google Chat.")
        print("Cuando quieras mandarlo: python scripts/weekly_report.py --send")
    else:
        ok = send_message(chat_msg)
        print("✅ Enviado a Google Chat." if ok else "⚠️  Error enviando a Google Chat.")

    print(f"\n✅ Reporte completado — {total} menciones analizadas")
    print('='*55)


def run_quora_report(preview: bool = False):
    """Reporte quincenal de Quora."""
    now = datetime.now()
    print(f"\n{'='*55}")
    print(f"🔍 REPORTE QUORA heru — {now.strftime('%d/%m/%Y')}")

    connector = ApifyConnector()
    print("  📡 Quora...", end=" ", flush=True)
    items = connector.scrape_quora(ECOSYSTEM_QUERIES["quora_topics"], max_items=15)
    print(f"{len(items)} respuestas")

    if not items:
        print("  ⚠️  Sin resultados en Quora esta quincena.")
        return

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    client = anthropic.Anthropic(api_key=api_key)
    agent = SocialListenerAgent(client=client, model="claude-opus-4-6", verbose=False)

    mentions_text = format_mentions({"quora": items})
    analysis = agent.analyze_ecosystem_insights(mentions_text, "últimas 2 semanas — Quora")

    reports_dir = Path("output/reports")
    reports_dir.mkdir(parents=True, exist_ok=True)
    path = reports_dir / f"quora_report_{now.strftime('%Y%m%d')}.md"
    path.write_text(analysis, encoding="utf-8")

    print(f"\n{analysis[:800]}\n...")
    print(f"💾 Reporte completo: {path}")

    if not preview:
        chat_msg = f"🔍 *QUORA QUINCENAL heru* | {now.strftime('%d/%m/%Y')}\n\n{analysis[:600]}"
        send_message(chat_msg)


# ─── Entry point ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--preview", action="store_true", help="Muestra el resumen aquí, no manda a Google Chat")
    parser.add_argument("--send",    action="store_true", help="Manda el último resumen a Google Chat")
    parser.add_argument("--quora",   action="store_true", help="Corre solo el reporte quincenal de Quora")
    args = parser.parse_args()

    if args.quora:
        run_quora_report(preview=args.preview)
    else:
        run_weekly_report(preview=not args.send)
