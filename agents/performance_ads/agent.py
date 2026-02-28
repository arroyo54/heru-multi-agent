"""
Agente Experto en Performance y Ads de heru.app
"""
from pathlib import Path
from typing import Optional, List, Literal
import anthropic

from core.base_agent import BaseAgent


CONFIG_PATH = Path(__file__).parent / "config.yaml"

AdPlatform = Literal["google", "meta", "tiktok", "all"]
ReportType = Literal["daily", "weekly", "monthly"]


class PerformanceAdsAgent(BaseAgent):
    """
    Agente especializado en gestión, optimización y reporte de campañas
    de Google Ads, Meta Ads y TikTok Ads para heru.app.
    """

    def __init__(self, client: anthropic.Anthropic, **kwargs):
        super().__init__(
            config_path=str(CONFIG_PATH),
            client=client,
            **kwargs,
        )

    def generate_report(
        self,
        report_type: ReportType,
        metrics_data: str,
        platform: AdPlatform = "all",
        period: Optional[str] = None,
        include_forecast: bool = False,
    ) -> str:
        """
        Genera un reporte de performance de campañas de ads.

        Args:
            report_type: daily, weekly, monthly
            metrics_data: Datos de métricas en cualquier formato (CSV, JSON, texto)
            platform: Plataforma(s) a reportar
            period: Período del reporte (ej: "1-7 febrero 2026")
            include_forecast: Si incluir proyecciones para el siguiente período
        """
        forecast_instruction = "\nIncluye proyecciones para el siguiente período (3 escenarios: conservador/base/optimista)." if include_forecast else ""

        prompt = f"""Genera un reporte de performance {report_type.upper()} para heru.app:

PLATAFORMA(S): {platform}
PERÍODO: {period or "período más reciente"}
{forecast_instruction}

DATOS DE MÉTRICAS:
{metrics_data}

Genera el siguiente reporte:

# 📊 REPORTE DE PERFORMANCE {report_type.upper()}
**heru.app** | {period or "Período reciente"} | {platform.upper()}

---

## RESUMEN EJECUTIVO
| KPI | Resultado | Objetivo | Status |
|-----|-----------|----------|--------|
| CAC | $X MXN | <$350 MXN | ✅/⚠️/🔴 |
| CPL | $X MXN | <$150 MXN | ✅/⚠️/🔴 |
| ROAS | Xx | >4x | ✅/⚠️/🔴 |
| Inversión Total | $X MXN | $X MXN presupuesto | ✅/⚠️/🔴 |

**Semáforo General: ✅ EN OBJETIVO / ⚠️ EN RIESGO / 🔴 FUERA DE OBJETIVO**

---

## PERFORMANCE POR PLATAFORMA

### Google Ads
- Impresiones:
- Clics:
- CTR: X% (benchmark >4%)
- CPC: $X
- Conversiones:
- CPL: $X
- Quality Score promedio: X/10

### Meta Ads
- Alcance:
- Impresiones:
- CPM: $X
- CTR: X%
- Leads generados:
- CPL: $X
- Frequency: X.X

---

## TOP CREATIVOS

### 🏆 Top 3 Mejores Creativos
| Creativo | CTR | CPL | Conversiones | Recomendación |
|---------|-----|-----|-------------|---------------|

### ❌ Bottom 3 (Pausar o Optimizar)
| Creativo | CTR | CPL | Problema | Acción |
|---------|-----|-----|---------|--------|

---

## ANÁLISIS Y HALLAZGOS
[3-5 insights más importantes del período]

## ⚠️ ALERTAS
[Cualquier métrica fuera de objetivo que requiere acción]

## ACCIONES TOMADAS ESTE PERÍODO
[Cambios realizados y su justificación]

## 🎯 PLAN PRÓXIMAS 2 SEMANAS
### 3 Acciones Prioritarias:
1. [Acción] - Impacto esperado - Responsable
2. [Acción] - Impacto esperado - Responsable
3. [Acción] - Impacto esperado - Responsable

{"## 📈 FORECAST PRÓXIMO PERÍODO" + chr(10) + "| Escenario | Inversión | Leads Est. | CAC Est. | ROAS Est. |" + chr(10) + "|-----------|-----------|------------|----------|-----------|" + chr(10) + "| Conservador | | | | |" + chr(10) + "| Base | | | | |" + chr(10) + "| Optimista | | | | |" if include_forecast else ""}"""

        return self.run(prompt)

    def optimize_campaign(
        self,
        campaign_data: str,
        optimization_goal: str = "reducir CAC",
        platform: AdPlatform = "meta",
    ) -> str:
        """
        Analiza una campaña y genera recomendaciones específicas de optimización.
        """
        prompt = f"""Analiza esta campaña de {platform.upper()} y genera un plan de optimización:

OBJETIVO DE OPTIMIZACIÓN: {optimization_goal}

DATOS DE LA CAMPAÑA:
{campaign_data}

Entrega:

## 🔧 PLAN DE OPTIMIZACIÓN DE CAMPAÑA

### Diagnóstico
[Qué está causando el bajo performance / qué puede mejorar]

### Cambios Inmediatos (Esta semana)
Para cada cambio:
- **Qué cambiar:** [Específico: qué ajustar exactamente]
- **Cómo:** [Paso a paso en {platform}]
- **Por qué:** [Razonamiento basado en datos]
- **Impacto esperado:** [Métrica y % estimado de mejora]

### Cambios Estratégicos (Próximas 2-4 semanas)
[Cambios más profundos: estructura, audiencias, creativos]

### A/B Tests Recomendados
| Variable | Versión A (Control) | Versión B (Test) | Hipótesis | Duración |
|----------|--------------------|--------------------|-----------|----------|

### Qué NO tocar
[Qué está funcionando bien y no debe modificarse]

### KPIs de Seguimiento Post-Optimización
[Cómo saber en 7 días si los cambios funcionaron]"""

        return self.run(prompt)

    def create_campaign_strategy(
        self,
        objective: str,
        budget: str,
        duration: str,
        target_segment: Optional[str] = None,
    ) -> str:
        """
        Crea una estrategia completa de campaña de ads.
        """
        prompt = f"""Diseña una estrategia completa de campaña de ads para heru.app:

OBJETIVO: {objective}
PRESUPUESTO: {budget}
DURACIÓN: {duration}
{"SEGMENTO OBJETIVO: " + target_segment if target_segment else ""}

Entrega:

## 📋 ESTRATEGIA DE CAMPAÑA: {objective.upper()}

### Resumen de la Estrategia
[Overview en 3-4 líneas]

### Distribución de Presupuesto
| Plataforma | % del Budget | MXN/semana | Justificación |
|------------|-------------|------------|---------------|
| Google Search | X% | $X | |
| Meta Ads | X% | $X | |
| TikTok Ads | X% | $X | |
| Testing/Nuevos | X% | $X | |

### Estructura de Campañas por Plataforma

#### Google Ads
- Campaña 1 [tipo]: [descripción, keywords principales, budget]
- Campaña 2 [tipo]: [descripción, keywords principales, budget]

#### Meta Ads
- Campaign 1 [objetivo]: [descripción, audiencias, formatos, budget]
- Campaign 2 [objetivo]: [descripción, audiencias, formatos, budget]

### Funnel de Conversión
TOFU (Awareness) → MOFU (Consideración) → BOFU (Conversión)
[Describir qué campañas cubren cada etapa]

### Creativos Necesarios
[Lista de assets que se necesitan producir con especificaciones]

### Timeline de Implementación
| Semana | Actividad | Responsable |
|--------|-----------|-------------|

### KPIs y Metas
| Métrica | Meta | Alerta Roja |
|---------|------|-------------|
| CAC | <$350 | >$600 |
| ROAS | >4x | <2x |
| CPL | <$150 | >$280 |

### Riesgos y Contingencias
[Top 3 riesgos y cómo mitigarlos]"""

        return self.run(prompt)

    def analyze_funnel(self, funnel_data: str) -> str:
        """
        Analiza el funnel de conversión de los ads e identifica puntos de fuga.
        """
        prompt = f"""Analiza el funnel de conversión de las campañas de heru.app:

DATOS DEL FUNNEL:
{funnel_data}

Entrega:

## 🔍 ANÁLISIS DE FUNNEL DE CONVERSIÓN

### Visualización del Funnel
```
Impresiones: X,XXX,XXX (100%)
    ↓ CTR X%
Clics: XX,XXX (X%)
    ↓ CVR landing X%
Leads/Registros: X,XXX (X%)
    ↓ Activación X%
Usuarios activos: XXX (X%)
    ↓ Conversión a pago X%
Clientes de pago: XXX (X%)
```

### Puntos de Fuga Identificados
[Dónde se está perdiendo más volumen y por qué]

### Benchmarks de la Industria Fintech México
[Comparar cada etapa vs benchmarks]

### Impacto Económico
[Cuánto revenue se pierde por cada punto porcentual de mejora en cada etapa]

### Plan de Mejora por Etapa
Para cada etapa con problema:
- **Hipótesis** del problema
- **Test A/B** recomendado
- **Cambio técnico** si aplica
- **Impacto esperado** en CAC y ROAS"""

        return self.run(prompt)

    def keyword_research(
        self,
        seed_keywords: List[str],
        objective: str = "conversión",
    ) -> str:
        """
        Realiza keyword research estratégico para campañas de Google Ads.
        """
        keywords_str = "\n".join(f"- {kw}" for kw in seed_keywords)

        prompt = f"""Realiza un keyword research estratégico para Google Ads de heru.app:

KEYWORDS SEMILLA:
{keywords_str}

OBJETIVO: {objective}

Entrega:

## 🔑 KEYWORD RESEARCH — heru.app

### Keywords de Alto Valor (conversión)
| Keyword | Match Type | Volumen Est. | CPC Est. | Intención | Prioridad |
|---------|-----------|--------------|----------|-----------|-----------|

### Keywords Educativas (top of funnel)
[Keywords informativos que pueden generar awareness y remarketing]

### Keywords de Competencia
[Keywords con mención de competidores]

### Long Tail Oportunidades
[Frases específicas con alta intención y menor competencia]

### Negative Keywords Esenciales
[Keywords que hay que excluir sí o sí y por qué]

### Grupos de Anuncios Sugeridos
[Cómo organizar las keywords en ad groups con temática coherente]

### Estimación de Resultados
Con presupuesto de $X/día estimamos:
- Clics/día: X-X
- CPL estimado: $X-X
- Leads/mes: X-X"""

        return self.run(prompt)
