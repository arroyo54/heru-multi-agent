"""
Agente Business Analyst de heru.app
"""
from pathlib import Path
from typing import Optional
import anthropic

from core.base_agent import BaseAgent


CONFIG_PATH = Path(__file__).parent / "config.yaml"


class BusinessAnalystAgent(BaseAgent):
    """
    Agente especializado en análisis de negocio, cruce de datos de múltiples fuentes
    y generación de reportes ejecutivos accionables para heru.app.
    """

    def __init__(self, client: anthropic.Anthropic, **kwargs):
        super().__init__(
            config_path=str(CONFIG_PATH),
            client=client,
            **kwargs,
        )

    def analyze_report(
        self,
        data: str,
        source: str,
        period: str = "última semana",
    ) -> str:
        """
        Realiza diagnóstico rápido de una sola fuente de datos.

        Args:
            data: Datos crudos a analizar (métricas, CSV, texto, etc.)
            source: Fuente de los datos (ads, social, leads, crm)
            period: Período que cubre el reporte
        """
        prompt = f"""Analiza estos datos de {source} y genera un diagnóstico ejecutivo:

FUENTE: {source}
PERÍODO: {period}

DATOS:
{data}

Usa el framework de diagnóstico rápido:

## DIAGNÓSTICO EJECUTIVO — {source.upper()} | {period}

### HEADLINE INSIGHT
[El insight más importante en una sola oración. Empieza con el hallazgo, no con contexto.]

---

### ¿QUÉ PASÓ?
[Descripción objetiva de los números más relevantes]

### ¿POR QUÉ PASÓ?
[Hipótesis con evidencia de los propios datos]

### ¿QUÉ SIGNIFICA PARA EL NEGOCIO?
[Impacto en MRR, CAC, LTV, retención u otras métricas clave]

### ¿QUÉ HACEMOS?
[Máximo 3 recomendaciones específicas — qué, quién y cuándo]

---

### ¿QUÉ NO SABEMOS TODAVÍA?
[Datos que faltan para una conclusión más sólida]"""

        return self.run(prompt)

    def cross_analyze(
        self,
        datasets: str,
        hypothesis: Optional[str] = None,
    ) -> str:
        """
        Cruza datos de dos o más fuentes para encontrar correlaciones no obvias.

        Args:
            datasets: Múltiples sets de datos, cada uno con su etiqueta de fuente
            hypothesis: Hipótesis inicial a validar o refutar (opcional)
        """
        hypothesis_section = f"\nHIPÓTESIS A EVALUAR: {hypothesis}" if hypothesis else ""

        prompt = f"""Cruza estos datasets y encuentra las correlaciones más relevantes para heru:
{hypothesis_section}

DATOS CRUZADOS:
{datasets}

Genera un análisis cruzado:

## ANÁLISIS CRUZADO DE DATOS

### HALLAZGO PRINCIPAL
[La correlación más importante encontrada. Si hay hipótesis, confirmar o refutar con evidencia.]

---

### EVIDENCIA POR FUENTE
[Para cada fuente de datos, el dato específico que contribuye al hallazgo]

### HIPÓTESIS CAUSAL
[¿Por qué existe esta correlación? Distinguir entre correlación y causalidad]

---

### IMPLICACIONES POR EQUIPO

**Marketing:**
[Qué cambiar en campañas, mensajes, segmentación]

**Producto:**
[Qué mejorar en la app, flujos o features]

**Ventas:**
[Cómo ajustar el proceso de calificación o cierre]

---

### EXPERIMENTO SUGERIDO
[Cómo validar la hipótesis causal — A/B test o análisis adicional específico]

### ¿QUÉ NO SABEMOS TODAVÍA?
[Preguntas que los datos actuales no pueden responder]"""

        return self.run(prompt)

    def create_executive_presentation(
        self,
        all_data: str,
        period: str = "esta semana",
        audience: str = "liderazgo",
    ) -> str:
        """
        Crea una presentación ejecutiva formal con todos los datos del período.

        Args:
            all_data: Datos de todas las fuentes disponibles
            period: Período del reporte
            audience: Audiencia de la presentación
        """
        prompt = f"""Crea una presentación ejecutiva basada en estos datos de heru.app:

PERÍODO: {period}
AUDIENCIA: {audience}

DATOS DISPONIBLES:
{all_data}

Formato de presentación ejecutiva (máximo impacto, mínimo tiempo de lectura):

## BUSINESS INTELLIGENCE REPORT — {period.upper()}
*heru.app | Para: {audience}*

---

### RESUMEN EJECUTIVO
[3 bullets máximo — solo lo más crítico para decisiones]
✅ [Logro o métrica positiva clave]
⚠️ [Riesgo o área de atención]
🎯 [Oportunidad identificada]

---

### SITUACIÓN ACTUAL vs OBJETIVO

| Métrica | Actual | Objetivo | Status |
|---------|--------|----------|--------|
[Completar con los datos disponibles]

---

### HALLAZGOS CLAVE POR ÁREA

**Adquisición:**
[2-3 bullets con semáforo ✅ ⚠️ 🔴]

**Producto / Retención:**
[2-3 bullets con semáforo]

**Monetización:**
[2-3 bullets con semáforo]

---

### TOP 3 OPORTUNIDADES
1. [Oportunidad] — Impacto estimado: [alto/medio/bajo]
2. [Oportunidad] — Impacto estimado: [alto/medio/bajo]
3. [Oportunidad] — Impacto estimado: [alto/medio/bajo]

### TOP 3 RIESGOS / ALERTAS
1. [Riesgo] — Urgencia: [inmediata/esta semana/este mes]
2. [Riesgo] — Urgencia: [inmediata/esta semana/este mes]
3. [Riesgo] — Urgencia: [inmediata/esta semana/este mes]

---

### DECISIONES REQUERIDAS ESTA SEMANA
[Solo si hay algo que el liderazgo debe decidir — con opciones y recomendación]

### MÉTRICAS A MONITOREAR
[KPIs más importantes para la próxima semana]

---

### ¿QUÉ NO SABEMOS TODAVÍA?
[Preguntas abiertas que requieren más datos]"""

        return self.run(prompt)

    def generate_campaign_insights(
        self,
        campaign_data: str,
        campaign_name: Optional[str] = None,
        benchmark: Optional[str] = None,
    ) -> str:
        """
        Genera insights de optimización para una campaña específica.

        Args:
            campaign_data: Métricas de la campaña (CTR, CPL, conversiones, etc.)
            campaign_name: Nombre o descripción de la campaña
            benchmark: Benchmarks de referencia (opcional)
        """
        campaign_label = campaign_name or "campaña"
        benchmark_section = f"\nBENCHMARKS DE REFERENCIA:\n{benchmark}" if benchmark else ""

        prompt = f"""Analiza el performance de esta campaña y genera insights de optimización:

CAMPAÑA: {campaign_label}
{benchmark_section}

DATOS DE LA CAMPAÑA:
{campaign_data}

Genera insights accionables:

## CAMPAIGN INSIGHTS — {campaign_label.upper()}

### HEADLINE
[El insight más importante en una oración — qué está pasando y por qué importa]

---

### PERFORMANCE ACTUAL vs BENCHMARK
[Tabla comparativa con semáforo por métrica]
✅ Métricas por encima del benchmark
⚠️ Métricas en rango aceptable
🔴 Métricas bajo benchmark

---

### SEGMENTOS GANADORES
[Audiencias, creativos, palabras clave o canales con mejor performance — con datos específicos]

### SEGMENTOS PERDEDORES
[Dónde se está desperdiciando presupuesto — con evidencia]

---

### HIPÓTESIS DE OPTIMIZACIÓN
[Por qué está pasando lo que está pasando — con base en los datos]

### CAMBIOS RECOMENDADOS
*Ordenados por impacto estimado:*
1. [Cambio] — Impacto esperado: [+X% CPL / +X conversiones] — Responsable: [equipo]
2. [Cambio] — Impacto esperado: [estimado] — Responsable: [equipo]
3. [Cambio] — Impacto esperado: [estimado] — Responsable: [equipo]

---

### A/B TESTS PROPUESTOS
[1-2 experimentos concretos con hipótesis, variable y métrica de éxito]

### ¿QUÉ NO SABEMOS TODAVÍA?
[Datos que mejorarían el análisis]"""

        return self.run(prompt)

    def weekly_summary(
        self,
        ads_data: Optional[str] = None,
        social_data: Optional[str] = None,
        leads_data: Optional[str] = None,
        crm_data: Optional[str] = None,
        week_label: str = "esta semana",
    ) -> str:
        """
        Genera el resumen ejecutivo semanal cruzando todas las fuentes disponibles.
        """
        sections = []
        if ads_data:
            sections.append(f"=== PERFORMANCE ADS ===\n{ads_data}")
        if social_data:
            sections.append(f"=== SOCIAL LISTENING ===\n{social_data}")
        if leads_data:
            sections.append(f"=== LEADS / CALIFICACIÓN ===\n{leads_data}")
        if crm_data:
            sections.append(f"=== CRM / PRODUCTO ===\n{crm_data}")

        all_data = "\n\n".join(sections) if sections else "No se proporcionaron datos."

        prompt = f"""Eres el Business Analyst de heru.app. Genera el reporte ejecutivo semanal
cruzando todos los datos disponibles. Busca correlaciones entre fuentes:

SEMANA: {week_label}

{all_data}

Genera el reporte ejecutivo semanal:

## WEEKLY BUSINESS INTELLIGENCE — {week_label.upper()}

### EXECUTIVE SUMMARY (30 segundos de lectura)
[3 bullets máximo — el CEO debe poder actuar con esto]

---

### CORRELACIÓN PRINCIPAL DE LA SEMANA
[El insight que surge de cruzar fuentes — la historia que cuentan los datos juntos]

---

### ESTADO DEL FUNNEL

| Etapa | Métrica | Resultado | vs semana anterior |
|-------|---------|-----------|-------------------|
| Awareness | Alcance + Menciones | X | ↑/↓ X% |
| Adquisición | Leads + CPL | X | ↑/↓ X% |
| Conversión | Registros → Pagos | X% | ↑/↓ X% |
| Retención | Churn + NPS | X% | ↑/↓ X% |

---

### ALERTAS Y OPORTUNIDADES
🔴 [Alerta urgente si hay]
⚠️ [Riesgo moderado]
✅ [Oportunidad a capitalizar]

### RECOMENDACIONES PARA LA PRÓXIMA SEMANA
1. [Acción] — Responsable: [equipo] — Métrica de éxito: [KPI]
2. [Acción] — Responsable: [equipo] — Métrica de éxito: [KPI]

---

### ¿QUÉ NO SABEMOS TODAVÍA?
[Preguntas que los datos no responden — para priorizar en próxima semana]"""

        return self.run(prompt)
