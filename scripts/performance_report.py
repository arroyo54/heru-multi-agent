"""
Reporte semanal de Performance Ads de heru.app.

Estructura:
  Google Chat → Resumen ejecutivo corto (semáforo KPIs + top alerta)
  Google Sheets → Reporte completo con métricas, análisis y recomendaciones
  Local → output/reports/performance_report_YYYYMMDD.md

Uso:
  python scripts/performance_report.py             # modo demo, no manda a Chat
  python scripts/performance_report.py --send      # manda a Google Chat
  python scripts/performance_report.py --real      # usa Google Ads API real
  python scripts/performance_report.py --days 30   # período de 30 días (default: 7)
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
from agents.performance_ads.agent import PerformanceAdsAgent
from core.connectors.google_ads import GoogleAdsConnector, is_configured
from core.google_chat import send_message
from core.google_sheets import upload_weekly_report, is_available as sheets_available


# ─── Resumen ejecutivo para Google Chat ──────────────────────────────────────

def build_chat_summary(analysis: str, metrics_raw: dict, demo_mode: bool) -> str:
    """Construye el mensaje corto para Google Chat (máx ~700 chars)."""
    s = metrics_raw.get("summary", {})
    period = metrics_raw.get("period", {})
    alerts = metrics_raw.get("alerts", [])

    spend  = f"${s.get('total_spend_mxn', 0):,.0f}"
    cpl    = f"${s.get('cpl_mxn', 0)} MXN"
    roas   = f"{s.get('roas', 'N/A')}x"
    cac    = f"${s.get('cac_mxn', 0)} MXN" if s.get('cac_mxn') else "N/A"

    # Semáforo automático
    cpl_val  = s.get("cpl_mxn", 0)
    roas_val = s.get("roas",    0)
    cac_val  = s.get("cac_mxn", 0)

    cpl_icon  = "✅" if cpl_val  < 150 else ("⚠️" if cpl_val  < 280 else "🔴")
    roas_icon = "✅" if roas_val > 4   else ("⚠️" if roas_val > 2   else "🔴")
    cac_icon  = "✅" if cac_val  < 350 else ("⚠️" if cac_val  < 600 else "🔴")

    top_alert = ""
    if alerts:
        critica = next((a for a in alerts if "CRÍTICA" in a.get("severity", "")), None)
        a = critica or alerts[0]
        top_alert = f"\n\n*⚠️ TOP ALERTA:* {a['campaign']}\n_{a['issue'][:120]}_"

    demo_label = " _(DEMO)_" if demo_mode else ""

    msg = (
        f"📈 *PERFORMANCE ADS heru*{demo_label} | {period.get('end', datetime.now().strftime('%d/%m/%Y'))}\n"
        f"_{period.get('start')} → {period.get('end')} ({period.get('days', 7)} días)_\n\n"
        f"*KPIs PRINCIPALES*\n"
        f"{cac_icon} CAC: *{cac}*  (objetivo <$350)\n"
        f"{cpl_icon} CPL: *{cpl}*  (objetivo <$150)\n"
        f"{roas_icon} ROAS: *{roas}*  (objetivo >4x)\n"
        f"💰 Inversión: *{spend} MXN*"
        f"{top_alert}"
    )
    return msg


# ─── Reporte principal ────────────────────────────────────────────────────────

def run_performance_report(demo_mode: bool = True, send_to_chat: bool = False, period_days: int = 7):
    now = datetime.now()
    print(f"\n{'='*55}")
    print(f"📈 REPORTE PERFORMANCE heru — {now.strftime('%A %d/%m/%Y %H:%M')}")
    if demo_mode:
        print("   ⚠️  MODO DEMO — datos de ejemplo (no reales)")
    print("=" * 55)

    # 1. Jalar métricas
    print("\n[1/4] Jalando métricas de Google Ads...")
    connector = GoogleAdsConnector(force_demo=demo_mode)
    metrics_text = connector.format_for_agent(period_days=period_days)
    metrics_raw  = connector.get_metrics(period_days=period_days)
    print(f"  ✅ {len(metrics_raw['campaigns'])} campañas | {len(metrics_raw.get('alerts', []))} alertas")

    # 2. Analizar con Claude
    print("\n[2/4] Analizando con Performance Agent...")
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    client  = anthropic.Anthropic(api_key=api_key)
    agent   = PerformanceAdsAgent(client=client, model="claude-opus-4-6", verbose=False)

    period_label = f"{metrics_raw['period']['start']} al {metrics_raw['period']['end']}"
    analysis = agent.generate_report(
        report_type="weekly",
        metrics_data=metrics_text,
        platform="google",
        period=period_label,
        include_forecast=True,
    )

    # 3. Guardar localmente
    print("\n[3/4] Guardando reporte local...")
    reports_dir = Path("output/reports")
    reports_dir.mkdir(parents=True, exist_ok=True)
    date_slug   = now.strftime("%Y%m%d")
    demo_suffix = "_DEMO" if demo_mode else ""

    full_report  = f"# PERFORMANCE ADS heru — {period_label}{' [DEMO]' if demo_mode else ''}\n\n"
    full_report += f"## MÉTRICAS RAW\n\n```\n{metrics_text}\n```\n\n"
    full_report += f"## ANÁLISIS\n\n{analysis}\n"

    report_path = reports_dir / f"performance_report_{date_slug}{demo_suffix}.md"
    report_path.write_text(full_report, encoding="utf-8")
    print(f"  💾 Guardado en: {report_path}")

    # 4. Construir y mostrar resumen
    print("\n[4/4] Construyendo resumen ejecutivo...")
    chat_msg = build_chat_summary(analysis, metrics_raw, demo_mode)

    print(f"\n{'─'*55}")
    print("RESUMEN PARA GOOGLE CHAT:")
    print("─" * 55)
    print(chat_msg)
    print("─" * 55)

    print("\n--- ANÁLISIS COMPLETO (primeras 1500 chars) ---")
    print(analysis[:1500])
    if len(analysis) > 1500:
        print(f"\n... [{len(analysis)-1500} chars más en {report_path}]")

    if send_to_chat:
        ok = send_message(chat_msg)
        print("\n✅ Enviado a Google Chat." if ok else "\n⚠️  Error enviando a Google Chat.")
    else:
        print("\n[MODO PREVIEW] No se envió a Google Chat.")
        print("Para enviarlo: python scripts/performance_report.py --send")

    print(f"\n✅ Reporte completado")
    print("=" * 55)


# ─── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--send",  action="store_true", help="Manda el resumen a Google Chat")
    parser.add_argument("--real",  action="store_true", help="Usa la API real de Google Ads")
    parser.add_argument("--days",  type=int, default=7, help="Días del período (default: 7)")
    args = parser.parse_args()

    if args.real and not is_configured():
        print("⚠️  Credenciales de Google Ads no configuradas en .env")
        print("   Variables requeridas:")
        print("   GOOGLE_ADS_DEVELOPER_TOKEN, GOOGLE_ADS_CLIENT_ID,")
        print("   GOOGLE_ADS_CLIENT_SECRET, GOOGLE_ADS_REFRESH_TOKEN,")
        print("   GOOGLE_ADS_CUSTOMER_ID")
        sys.exit(1)

    run_performance_report(
        demo_mode=not args.real,
        send_to_chat=args.send,
        period_days=args.days,
    )
