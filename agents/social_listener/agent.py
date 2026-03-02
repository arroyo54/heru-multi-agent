"""
Agente Social Listener de heru.app
"""
from pathlib import Path
from typing import Optional, List
import anthropic

from core.base_agent import BaseAgent


CONFIG_PATH = Path(__file__).parent / "config.yaml"


class SocialListenerAgent(BaseAgent):
    """
    Agente especializado en social listening, monitoreo de menciones,
    análisis de sentimiento y detección de tendencias para heru.app.
    """

    def __init__(self, client: anthropic.Anthropic, **kwargs):
        super().__init__(
            config_path=str(CONFIG_PATH),
            client=client,
            **kwargs,
        )

    def analyze_mentions(
        self,
        mentions_data: str,
        platform: Optional[str] = None,
        time_range: str = "últimos 7 días",
    ) -> str:
        """
        Analiza un conjunto de menciones y produce un reporte con insights.

        Args:
            mentions_data: String con las menciones a analizar (puede ser texto plano,
                          JSON, o datos copiados de una herramienta de social listening)
            platform: Plataforma de origen (opcional)
            time_range: Rango de tiempo de las menciones
        """
        prompt = f"""Analiza estas menciones de heru.app y genera un reporte de social listening:

PLATAFORMA: {platform or "múltiples plataformas"}
PERÍODO: {time_range}

MENCIONES:
{mentions_data}

Genera el siguiente reporte:

## 📊 REPORTE DE SOCIAL LISTENING
**Período:** {time_range} | **Plataforma:** {platform or "múltiples"}

---

### RESUMEN EJECUTIVO
[3-5 bullets con los insights más importantes]

---

### MÉTRICAS
- Total de menciones analizadas:
- Sentimiento positivo: X%
- Sentimiento neutro: X%
- Sentimiento negativo: X%
- Alcance estimado:
- Engagement promedio:

---

### 🟢 MENCIONES POSITIVAS DESTACADAS
[Top 3 con transcripción y análisis]

### 🔴 MENCIONES NEGATIVAS / ALERTAS
[Con clasificación: prioridad ALTA / MEDIA / BAJA y respuesta sugerida]

### 💡 OPORTUNIDADES DETECTADAS
[Conversaciones donde heru puede intervenir con valor]

---

### TEMAS PRINCIPALES
1. [Tema] - X menciones - Sentimiento predominante
2. [Tema] - X menciones - Sentimiento predominante
3. [Tema] - X menciones - Sentimiento predominante

---

### RECOMENDACIONES
[3 acciones concretas para el equipo de marketing/community]"""

        return self.run(prompt)

    def monitor_competitor(
        self,
        competitor_name: str,
        competitor_data: str,
        comparison_period: str = "esta semana",
    ) -> str:
        """
        Analiza la actividad de un competidor en redes sociales.
        """
        prompt = f"""Analiza la actividad de {competitor_name} en redes sociales y compara con heru:

PERÍODO: {comparison_period}

DATOS DEL COMPETIDOR:
{competitor_data}

Genera un análisis competitivo que incluya:

## 🔍 ANÁLISIS COMPETITIVO: {competitor_name} vs heru

### ESTRATEGIA DE CONTENIDO
- Tipos de contenido que publica
- Frecuencia de publicación
- Temas principales
- Tono de comunicación

### MÉTRICAS DE ENGAGEMENT
- Engagement rate estimado
- Tipo de contenido con mejor performance
- Horarios de publicación

### MENSAJES Y POSICIONAMIENTO
- Propuesta de valor que comunica
- Pain points que ataca
- Audiencias que parece targetear

### ANÁLISIS SWOT RÁPIDO
- ✅ Qué están haciendo bien
- ❌ Qué están haciendo mal
- 🎯 Oportunidades que no están aprovechando

### RECOMENDACIONES PARA HERU
[Qué puede heru aprender o hacer diferente basado en este análisis]"""

        return self.run(prompt)

    def detect_trends(
        self,
        topics_data: str,
        context: str = "México, trabajadores independientes, impuestos",
    ) -> str:
        """
        Detecta tendencias relevantes para heru en el ecosistema digital.
        """
        prompt = f"""Analiza estos datos de tendencias y conversaciones digitales en México:

CONTEXTO: {context}

DATOS DE TENDENCIAS:
{topics_data}

Identifica y analiza:

## 📈 REPORTE DE TENDENCIAS

### TENDENCIAS RELEVANTES PARA HERU
Para cada tendencia:
- **[NOMBRE TENDENCIA]** - Nivel de relevancia: ALTO/MEDIO/BAJO
  - Qué es: [descripción]
  - Por qué importa a heru: [conexión con el negocio]
  - Oportunidad de contenido: [idea concreta]
  - Ventana temporal: [urgente/esta semana/este mes]

### OPORTUNIDADES DE NEWSJACKING
[Tendencias donde heru puede insertarse con contenido relevante HOY]

### ALERTAS FISCALES / SAT
[Noticias o cambios regulatorios que impactan a los usuarios de heru]

### PLAN DE ACCIÓN INMEDIATO
1. [Acción] - Agente responsable - Timeline
2. [Acción] - Agente responsable - Timeline
3. [Acción] - Agente responsable - Timeline"""

        return self.run(prompt)

    def identify_lead_opportunities(self, conversations: str) -> str:
        """
        Identifica oportunidades de leads en conversaciones públicas de redes sociales.
        Las personas que preguntan sobre impuestos, SAT, etc. sin mencionar heru.
        """
        prompt = f"""Analiza estas conversaciones públicas de redes sociales y encuentra
oportunidades donde heru.app podría aportar valor o captar leads:

CONVERSACIONES:
{conversations}

Para cada oportunidad identifica:

## 🎯 OPORTUNIDADES DE LEAD EN REDES SOCIALES

### OPORTUNIDADES DE ALTO VALOR
Para cada una:
- **Plataforma:**
- **Usuario/Cuenta:**
- **Conversación/Post:**
- **Problema que tienen:**
- **Por qué es fit con heru:**
- **Respuesta sugerida:** [Draft de respuesta pública no spammy]
- **Score de oportunidad (1-10):**

### TEMAS RECURRENTES
[Temas que se repiten y podrían inspirar contenido orgánico de heru]

### PALABRAS CLAVE DE CAPTACIÓN
[Keywords que usaría alguien con necesidad de heru, para añadir al social listening]

### NOTA SOBRE ENGAGEMENT
[Guía de cómo responder a estas oportunidades sin sonar a spam o bot]"""

        return self.run(prompt)

    def generate_daily_report(
        self,
        date: str,
        mentions_count: int,
        sample_mentions: str,
        alerts: Optional[str] = None,
    ) -> str:
        """
        Genera el reporte diario de social listening para el equipo.
        """
        alerts_section = f"\nALERTAS DEL DÍA:\n{alerts}" if alerts else ""

        prompt = f"""Genera el reporte diario de social listening de heru.app:

FECHA: {date}
TOTAL MENCIONES HOY: {mentions_count}
{alerts_section}

MUESTRA DE MENCIONES:
{sample_mentions}

Genera un reporte ejecutivo diario conciso:

## 📱 DAILY SOCIAL LISTENING — {date}

**[Si hay alertas críticas, empezar con ⚠️ ALERTA CRÍTICA]**

### RESUMEN DEL DÍA (30 segundos de lectura)
[3 bullets máximo con lo más importante]

### NÚMEROS
- Menciones totales: {mentions_count}
- Sentimiento: 🟢X% 🟡X% 🔴X%
- Trend vs ayer: ↑/↓ X%

### HIGHLIGHT DEL DÍA
[La mención más relevante con contexto]

### ACCIONES REQUERIDAS HOY
[Solo si hay algo urgente, con responsable y deadline]

*Próximo reporte: mañana {date} + 1*"""

        return self.run(prompt)

    def analyze_ecosystem_insights(self, mentions_data: str, time_range: str = "última semana") -> str:
        """
        Analiza conversaciones del ecosistema (impuestos, SAT, RESICO, freelancers, drivers)
        para extraer miedos, dolores, oportunidades e insights de mercado.
        NO es sobre heru — es sobre lo que habla la gente afuera.
        """
        prompt = f"""Eres el Social Listener de heru.app. Analiza estas conversaciones públicas
sobre impuestos, SAT, RESICO, freelancers y conductores de plataformas en México.

OBJETIVO: Extraer inteligencia de mercado — qué le preocupa, duele, confunde y motiva
a nuestra audiencia objetivo. No busques menciones de heru, busca la voz del usuario.

PERÍODO: {time_range}

CONVERSACIONES:
{mentions_data}

Entrega este análisis estructurado:

---

## MIEDOS Y ANSIEDADES DETECTADOS
[Los temores más frecuentes — frases reales si las hay]
- [Miedo 1]: frecuencia + cita representativa
- [Miedo 2]: frecuencia + cita representativa
- [Miedo 3 si hay]

## DOLORES Y FRUSTRACIONES
[Problemas concretos que la gente está viviendo]
- [Dolor 1]: descripción + frecuencia
- [Dolor 2]: descripción + frecuencia

## PREGUNTAS MÁS FRECUENTES
[Las dudas reales que tiene la gente — oportunidades de contenido directo]
1. [Pregunta]
2. [Pregunta]
3. [Pregunta]

## OPORTUNIDADES DE MERCADO
[Necesidades no satisfechas que heru podría resolver o capitalizar]
- [Oportunidad 1]
- [Oportunidad 2]

## TEMAS DE CONVERSACIÓN TRENDING
[Los temas más activos esta semana en este ecosistema]
| Tema | Volumen | Sentimiento | Oportunidad para heru |
|------|---------|-------------|----------------------|

## INSIGHTS CLAVE PARA PRODUCTO Y MARKETING
[Máximo 3 insights accionables — lo que este análisis implica para heru]
1. [Insight → implicación concreta]
2. [Insight → implicación concreta]
3. [Insight → implicación concreta]

## OPORTUNIDADES DE CONTENIDO INMEDIATAS
[Ideas de contenido que responden directamente a lo que la gente está pidiendo esta semana]
- [Idea 1]: plataforma + ángulo + urgencia
- [Idea 2]: plataforma + ángulo + urgencia"""

        return self.run(prompt)

    def analyze_brand_mentions(self, mentions_data: str, time_range: str = "última semana") -> str:
        """
        Analiza específicamente las menciones directas de heru.app.
        Sentimiento, crisis, testimonios, quejas y oportunidades de respuesta.
        """
        prompt = f"""Analiza estas menciones directas de heru.app en redes sociales:

PERÍODO: {time_range}

MENCIONES:
{mentions_data}

Entrega:

## MENCIONES DE HERU — {time_range}

**Total analizadas:** X
**Sentimiento:** 🟢 X% positivo | 🟡 X% neutro | 🔴 X% negativo

### MENCIONES CRÍTICAS (requieren acción)
[Si hay bugs reportados, acusaciones, problemas de seguridad — con respuesta sugerida]

### MENCIONES POSITIVAS DESTACADAS
[Top 2-3 que se pueden usar como social proof]

### OPORTUNIDADES DE RESPUESTA
[Menciones donde heru puede responder y generar valor]

### ALERTAS ACTIVAS
[Crisis o patrones negativos que requieren atención inmediata]"""

        return self.run(prompt)

    def sentiment_analysis(self, text_data: str) -> str:
        """
        Realiza análisis de sentimiento detallado de un conjunto de textos.
        """
        prompt = f"""Realiza un análisis de sentimiento detallado de estos textos sobre heru.app:

TEXTOS A ANALIZAR:
{text_data}

Entrega:
1. **Sentimiento general**: Positivo/Negativo/Neutro con porcentaje
2. **Emociones detectadas**: Lista de emociones con frecuencia
3. **Temas con sentimiento negativo**: Detallar para poder actuar
4. **Temas con sentimiento positivo**: Para amplificar en comunicación
5. **Frases representativas**: 3 citas que mejor capturan el sentimiento
6. **Score de NPS estimado**: Basado en el análisis
7. **Recomendaciones**: Qué hacer con estos insights"""

        return self.run(prompt)
