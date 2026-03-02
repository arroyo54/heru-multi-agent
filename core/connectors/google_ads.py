"""
Conector de Google Ads para el agente de Performance de heru.app.

Modos de operación:
  - DEMO: genera datos realistas de ejemplo (sin credenciales)
  - REAL: se conecta a la API de Google Ads con credenciales reales

Setup para modo REAL (una sola vez):
1. Google Ads → Herramientas → Centro de la API → solicitar Developer Token
2. Google Cloud → Credenciales → OAuth 2.0 → crear Web Application credentials
3. Ejecutar: python scripts/google_ads_auth.py  (genera el refresh_token)
4. Agregar al .env:
     GOOGLE_ADS_DEVELOPER_TOKEN=...
     GOOGLE_ADS_CLIENT_ID=...
     GOOGLE_ADS_CLIENT_SECRET=...
     GOOGLE_ADS_REFRESH_TOKEN=...
     GOOGLE_ADS_CUSTOMER_ID=...  (formato sin guiones: 1234567890)
"""
import os
import random
from datetime import datetime, timedelta
from typing import Optional


# ─── Verificación de credenciales ────────────────────────────────────────────

REQUIRED_ENV_VARS = [
    "GOOGLE_ADS_DEVELOPER_TOKEN",
    "GOOGLE_ADS_CLIENT_ID",
    "GOOGLE_ADS_CLIENT_SECRET",
    "GOOGLE_ADS_REFRESH_TOKEN",
    "GOOGLE_ADS_CUSTOMER_ID",
]


def is_configured() -> bool:
    """True si todas las credenciales de Google Ads están en el .env."""
    return all(os.environ.get(v) for v in REQUIRED_ENV_VARS)


# ─── Datos demo realistas ─────────────────────────────────────────────────────

def _demo_campaign_metrics(period_days: int = 7) -> dict:
    """
    Genera métricas de campañas realistas para demo.
    Basado en benchmarks de fintech México con presupuesto ~$50k MXN/mes.
    """
    random.seed(42)  # Seed fijo para reproducibilidad en demo

    def r(base, variance=0.15):
        return round(base * (1 + random.uniform(-variance, variance)), 2)

    return {
        "period": {
            "start": (datetime.now() - timedelta(days=period_days)).strftime("%d/%m/%Y"),
            "end": datetime.now().strftime("%d/%m/%Y"),
            "days": period_days,
        },
        "summary": {
            "total_spend_mxn": r(12500),
            "total_impressions": int(r(285000)),
            "total_clicks": int(r(8420)),
            "total_conversions": int(r(187)),
            "total_leads": int(r(312)),
            "cac_mxn": r(380),           # objetivo <$350 — ligeramente alto
            "cpl_mxn": r(142),           # objetivo <$150 — ok
            "roas": r(3.2),              # objetivo >4x — bajo
            "ctr_overall": r(2.95),
        },
        "campaigns": [
            {
                "name": "🔍 Search — Declaración Impuestos",
                "type": "Search",
                "status": "ENABLED",
                "spend_mxn": r(4200),
                "impressions": int(r(42000)),
                "clicks": int(r(2100)),
                "ctr": r(5.1),           # ✅ >4%
                "cpc_mxn": r(2.0),
                "conversions": int(r(89)),
                "cpl_mxn": r(118),       # ✅ <$150
                "quality_score_avg": r(7.4),  # ✅ >7
                "top_keywords": [
                    {"keyword": "declarar impuestos freelancer", "clicks": 412, "ctr": 6.8, "cpl": 95},
                    {"keyword": "app declaracion SAT", "clicks": 387, "ctr": 5.2, "cpl": 108},
                    {"keyword": "como facturar sin contador", "clicks": 298, "ctr": 4.9, "cpl": 125},
                ],
            },
            {
                "name": "🔍 Search — RESICO Awareness",
                "type": "Search",
                "status": "ENABLED",
                "spend_mxn": r(1800),
                "impressions": int(r(28000)),
                "clicks": int(r(560)),
                "ctr": r(2.0),           # ⚠️ bajo
                "cpc_mxn": r(3.2),
                "conversions": int(r(18)),
                "cpl_mxn": r(200),       # 🔴 >$150
                "quality_score_avg": r(5.8),  # ⚠️ <7
                "top_keywords": [
                    {"keyword": "que es resico", "clicks": 180, "ctr": 2.1, "cpl": 195},
                    {"keyword": "resico obligaciones SAT", "clicks": 145, "ctr": 1.8, "cpl": 210},
                ],
            },
            {
                "name": "📱 Meta — Conductores Plataformas",
                "type": "Meta_Leads",
                "status": "ENABLED",
                "spend_mxn": r(3500),
                "impressions": int(r(180000)),
                "clicks": int(r(4200)),
                "ctr": r(2.3),
                "cpc_mxn": r(0.83),
                "leads": int(r(145)),
                "cpl_mxn": r(138),       # ✅ <$150
                "cpm_mxn": r(19.4),      # ✅ <$80
                "frequency": r(2.8),     # ✅ <4
                "top_creatives": [
                    {"name": "Video 30s — '¿Manejas para Uber?'", "ctr": 3.1, "cpl": 112, "leads": 58},
                    {"name": "Imagen — Hook miedo SAT", "ctr": 2.4, "cpl": 148, "leads": 47},
                    {"name": "Carrusel — Features heru", "ctr": 1.8, "cpl": 195, "leads": 40},
                ],
            },
            {
                "name": "📱 Meta — Freelancers Digitales",
                "type": "Meta_Traffic",
                "status": "ENABLED",
                "spend_mxn": r(1800),
                "impressions": int(r(95000)),
                "clicks": int(r(1560)),
                "ctr": r(1.64),          # ⚠️ bajo
                "cpc_mxn": r(1.15),
                "leads": int(r(62)),
                "cpl_mxn": r(168),       # 🔴 >$150
                "cpm_mxn": r(18.9),
                "frequency": r(3.6),     # ⚠️ subiendo
                "top_creatives": [
                    {"name": "Reel — 'Factura en 2 min'", "ctr": 2.2, "cpl": 145, "leads": 35},
                    {"name": "Imagen — Propuesta de valor", "ctr": 1.1, "cpl": 195, "leads": 27},
                ],
            },
            {
                "name": "♻️ Remarketing — Visitantes sin conversión",
                "type": "Display_Remarketing",
                "status": "ENABLED",
                "spend_mxn": r(780),
                "impressions": int(r(48000)),
                "clicks": int(r(380)),
                "ctr": r(0.79),
                "cpc_mxn": r(2.05),
                "conversions": int(r(28)),
                "cpl_mxn": r(104),       # ✅ mejor CAC (ya conocen el producto)
                "quality_score_avg": None,
            },
        ],
        "alerts": [
            {
                "severity": "🔴 CRÍTICA",
                "campaign": "Search — RESICO Awareness",
                "issue": "CPL $200 MXN (objetivo <$150). Quality Score 5.8 — anuncios poco relevantes.",
                "action": "Revisar match de keywords vs landing page. Actualizar ad copy.",
            },
            {
                "severity": "⚠️ ATENCIÓN",
                "campaign": "Meta — Freelancers Digitales",
                "issue": "Frequency 3.6 en 7 días — audiencia saturándose. CPL subiendo.",
                "action": "Refrescar creativos o ampliar audiencia (lookalike 3-5%).",
            },
            {
                "severity": "⚠️ ATENCIÓN",
                "campaign": "General",
                "issue": "ROAS 3.2x — por debajo del objetivo 4x.",
                "action": "Reasignar presupuesto de campañas con ROAS bajo a Search — Declaración (mejor performer).",
            },
        ],
        "ab_tests_active": [
            {
                "name": "Hook video conductores",
                "variant_a": "Miedo: '¿Ya te llegó carta del SAT?'",
                "variant_b": "Beneficio: 'Declara en 5 minutos desde tu cel'",
                "winner": "Variante B lidera con 23% menor CPL (aún no estadísticamente significativo)",
                "status": "En curso — día 5 de 14",
            }
        ],
        "is_demo": True,
    }


# ─── Conector real (Google Ads API) ──────────────────────────────────────────

def _fetch_real_metrics(period_days: int = 7) -> dict:
    """
    Jala métricas reales desde la Google Ads API.
    Requiere: google-ads library + credenciales en .env
    """
    try:
        from google.ads.googleads.client import GoogleAdsClient
    except ImportError:
        raise ImportError(
            "Instala la librería: pip install google-ads\n"
            "Luego configura las credenciales en .env (ver cabecera de este archivo)"
        )

    customer_id = os.environ.get("GOOGLE_ADS_CUSTOMER_ID", "").replace("-", "")

    config = {
        "developer_token": os.environ["GOOGLE_ADS_DEVELOPER_TOKEN"],
        "client_id":       os.environ["GOOGLE_ADS_CLIENT_ID"],
        "client_secret":   os.environ["GOOGLE_ADS_CLIENT_SECRET"],
        "refresh_token":   os.environ["GOOGLE_ADS_REFRESH_TOKEN"],
        "use_proto_plus":  True,
    }
    client = GoogleAdsClient.load_from_dict(config)
    ga_service = client.get_service("GoogleAdsService")

    end_date   = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=period_days)).strftime("%Y-%m-%d")

    # Query GAQL — métricas de campaña
    query = f"""
        SELECT
            campaign.id,
            campaign.name,
            campaign.status,
            campaign.advertising_channel_type,
            metrics.impressions,
            metrics.clicks,
            metrics.ctr,
            metrics.average_cpc,
            metrics.conversions,
            metrics.cost_micros,
            metrics.cost_per_conversion
        FROM campaign
        WHERE segments.date BETWEEN '{start_date}' AND '{end_date}'
          AND campaign.status = 'ENABLED'
        ORDER BY metrics.cost_micros DESC
    """

    response = ga_service.search(customer_id=customer_id, query=query)

    campaigns = []
    total_spend = 0
    total_clicks = 0
    total_impressions = 0
    total_conversions = 0

    for row in response:
        spend_mxn = row.metrics.cost_micros / 1_000_000
        total_spend       += spend_mxn
        total_clicks      += row.metrics.clicks
        total_impressions += row.metrics.impressions
        total_conversions += row.metrics.conversions

        campaigns.append({
            "name":          row.campaign.name,
            "type":          row.campaign.advertising_channel_type.name,
            "status":        row.campaign.status.name,
            "spend_mxn":     round(spend_mxn, 2),
            "impressions":   row.metrics.impressions,
            "clicks":        row.metrics.clicks,
            "ctr":           round(row.metrics.ctr * 100, 2),
            "cpc_mxn":       round(row.metrics.average_cpc / 1_000_000, 2),
            "conversions":   round(row.metrics.conversions, 1),
            "cpl_mxn":       round(row.metrics.cost_per_conversion / 1_000_000, 2),
        })

    return {
        "period": {
            "start":   start_date,
            "end":     end_date,
            "days":    period_days,
        },
        "summary": {
            "total_spend_mxn":   round(total_spend, 2),
            "total_impressions": total_impressions,
            "total_clicks":      total_clicks,
            "total_conversions": round(total_conversions, 1),
            "cpl_mxn":           round(total_spend / total_conversions, 2) if total_conversions else 0,
        },
        "campaigns": campaigns,
        "alerts":    [],
        "is_demo":   False,
    }


# ─── Interfaz pública ─────────────────────────────────────────────────────────

class GoogleAdsConnector:
    """
    Conector unificado Google Ads.
    Si las credenciales están configuradas usa la API real,
    si no, corre en modo DEMO con datos de ejemplo.
    """

    def __init__(self, force_demo: bool = False):
        self.demo_mode = force_demo or not is_configured()
        if self.demo_mode:
            print("  📊 [Google Ads] Modo DEMO — datos de ejemplo realistas")
        else:
            print("  📊 [Google Ads] Conectado — jalando datos reales")

    def get_metrics(self, period_days: int = 7) -> dict:
        if self.demo_mode:
            return _demo_campaign_metrics(period_days)
        return _fetch_real_metrics(period_days)

    def format_for_agent(self, period_days: int = 7) -> str:
        """
        Formatea las métricas como texto estructurado para pasarle al agente de performance.
        """
        data = self.get_metrics(period_days)
        period = data["period"]
        s = data["summary"]
        demo_label = " [DATOS DE EJEMPLO - DEMO]" if data.get("is_demo") else ""

        lines = [
            f"=== MÉTRICAS GOOGLE ADS{demo_label} ===",
            f"Período: {period['start']} → {period['end']} ({period['days']} días)\n",
            "--- RESUMEN GENERAL ---",
            f"Inversión total:     ${s['total_spend_mxn']:,.0f} MXN",
            f"Impresiones:         {s['total_impressions']:,}",
            f"Clics:               {s['total_clicks']:,}",
            f"Conversiones/Leads:  {s.get('total_conversions', s.get('total_leads', 'N/A'))}",
            f"CPL promedio:        ${s.get('cpl_mxn', 'N/A')} MXN",
        ]

        if "cac_mxn" in s:
            lines.append(f"CAC estimado:        ${s['cac_mxn']} MXN")
        if "roas" in s:
            lines.append(f"ROAS:                {s['roas']}x")

        lines.append("\n--- CAMPAÑAS ---")
        for c in data["campaigns"]:
            lines += [
                f"\n[{c['name']}]",
                f"  Tipo:          {c['type']}",
                f"  Gasto:         ${c['spend_mxn']:,.0f} MXN",
                f"  Impresiones:   {c.get('impressions', 'N/A'):,}",
                f"  Clics:         {c.get('clicks', 'N/A'):,}",
                f"  CTR:           {c.get('ctr', 'N/A')}%",
                f"  CPL:           ${c.get('cpl_mxn', 'N/A')} MXN",
            ]
            if c.get("quality_score_avg"):
                lines.append(f"  Quality Score: {c['quality_score_avg']}/10")
            if c.get("frequency"):
                lines.append(f"  Frequency:     {c['frequency']}")
            if c.get("top_keywords"):
                lines.append("  Top Keywords:")
                for kw in c["top_keywords"]:
                    lines.append(f"    • '{kw['keyword']}' — CTR {kw['ctr']}% | CPL ${kw['cpl']}")
            if c.get("top_creatives"):
                lines.append("  Creativos:")
                for cr in c["top_creatives"]:
                    lines.append(f"    • {cr['name']} — CTR {cr['ctr']}% | CPL ${cr['cpl']}")

        if data.get("alerts"):
            lines.append("\n--- ALERTAS DETECTADAS ---")
            for a in data["alerts"]:
                lines += [
                    f"\n{a['severity']}: {a['campaign']}",
                    f"  Problema: {a['issue']}",
                    f"  Acción:   {a['action']}",
                ]

        if data.get("ab_tests_active"):
            lines.append("\n--- A/B TESTS ACTIVOS ---")
            for t in data["ab_tests_active"]:
                lines += [
                    f"\n• {t['name']}",
                    f"  A: {t['variant_a']}",
                    f"  B: {t['variant_b']}",
                    f"  Estado: {t['status']}",
                    f"  Resultado parcial: {t['winner']}",
                ]

        return "\n".join(lines)
