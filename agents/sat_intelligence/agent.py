"""
Agente de Inteligencia Fiscal SAT de heru.app
"""
from pathlib import Path
from typing import Optional
import anthropic

from core.base_agent import BaseAgent


CONFIG_PATH = Path(__file__).parent / "config.yaml"


class SATIntelligenceAgent(BaseAgent):
    """
    Agente especializado en monitoreo e interpretación de cambios regulatorios
    del SAT, DOF y el ecosistema fiscal mexicano para heru.app.
    """

    def __init__(self, client: anthropic.Anthropic, **kwargs):
        super().__init__(
            config_path=str(CONFIG_PATH),
            client=client,
            **kwargs,
        )

    def analyze_sat_update(
        self,
        update_content: str,
        source: str = "SAT.gob.mx",
        publication_date: Optional[str] = None,
    ) -> str:
        """
        Analiza una publicación o comunicado del SAT y determina su impacto en heru.

        Args:
            update_content: Texto o resumen del comunicado/publicación
            source: Fuente (SAT.gob.mx, DOF, RMF, CFF, SHCP, etc.)
            publication_date: Fecha de publicación (opcional)
        """
        date_line = f"**Fecha de publicación:** {publication_date}" if publication_date else ""

        prompt = f"""Analiza esta publicación fiscal y genera una alerta estructurada para el equipo de heru:

FUENTE: {source}
{date_line}

CONTENIDO:
{update_content}

Evalúa el nivel de alerta (CRÍTICA / IMPORTANTE / OPORTUNIDAD) y genera el reporte completo:

## ALERTA FISCAL heru — [NIVEL: determinar según el impacto]

**Fuente:** {source}
{date_line}
**Fecha de vigencia:** [si aplica]

---

### QUÉ CAMBIÓ
[Descripción técnica del cambio con referencia exacta al artículo o regla]

### QUÉ SIGNIFICA EN LENGUAJE SIMPLE
[Traducción para alguien sin conocimientos fiscales — como si se lo explicaras a un conductor de Uber]

---

### IMPACTO POR SEGMENTO

**Usuarios en RESICO:**
[Impacto específico, qué tienen que hacer o qué cambia para ellos]

**Usuarios en Plataformas Tecnológicas (Uber/DiDi/Rappi):**
[Impacto específico]

**Usuarios en Actividad Empresarial / Honorarios:**
[Impacto específico]

---

### QUÉ DEBE HACER EL EQUIPO DE HERU

**Producto:** [acción específica — ¿requiere cambio en la app o flujos?]
**Marketing:** [acción específica — ¿comunicar a usuarios, crear contenido?]
**Soporte:** [qué preguntas esperar de usuarios y cómo responderlas]

---

### OPORTUNIDAD DE CONTENIDO
[Brief para el Copywriter si este cambio puede aprovecharse para educar o captar leads]

### FECHA LÍMITE PARA ACTUAR
[Si hay urgencia regulatoria para usuarios o para heru]

---

### FUENTE Y REFERENCIA LEGAL
[Cita exacta: artículo, resolución, fecha de publicación]
*Nota: Distinguir claramente entre lo que ES la ley y lo que es interpretación.*"""

        return self.run(prompt)

    def assess_user_impact(
        self,
        regulatory_change: str,
        segment: str = "todos",
    ) -> str:
        """
        Evalúa en detalle el impacto de un cambio regulatorio en un segmento específico.

        Args:
            regulatory_change: Descripción del cambio regulatorio
            segment: Segmento a analizar (resico, plataformas, empresarial, todos)
        """
        prompt = f"""Evalúa el impacto de este cambio regulatorio en los usuarios de heru:

CAMBIO REGULATORIO:
{regulatory_change}

SEGMENTO A ANALIZAR: {segment}

Genera un análisis de impacto detallado:

## ANÁLISIS DE IMPACTO — {segment.upper()}

### RESUMEN EJECUTIVO
[Una oración: qué cambia, para quién y cuándo entra en vigor]

---

### USUARIOS AFECTADOS
- Estimación del % de la base de heru que aplica
- Características del usuario afectado
- Situaciones específicas que aplican vs. que no aplican

### QUÉ PASA SI EL USUARIO NO HACE NADA
[Consecuencias concretas: multas, recargos, exclusión de régimen, etc.]

### QUÉ DEBE HACER EL USUARIO (paso a paso)
1. [Primer paso]
2. [Segundo paso]
3. [Si aplica]

---

### CÓMO PUEDE AYUDAR HERU
[Features existentes que cubren este cambio, o gaps que requieren desarrollo]

### PREGUNTAS FRECUENTES ANTICIPADAS
**P:** [Pregunta que harán los usuarios]
**R:** [Respuesta clara y directa]

**P:** [Pregunta 2]
**R:** [Respuesta 2]

---

### AMBIGÜEDADES LEGALES
[Si hay interpretaciones posibles, señalarlas explícitamente — no inventar certeza]

### REFERENCIA LEGAL
[Artículo exacto, resolución o criterio normativo]"""

        return self.run(prompt)

    def create_content_brief(
        self,
        fiscal_news: str,
        content_type: str = "educativo",
        urgency: str = "esta semana",
    ) -> str:
        """
        Crea un brief de contenido educativo basado en una novedad fiscal.

        Args:
            fiscal_news: Descripción de la novedad o cambio fiscal
            content_type: Tipo de contenido (educativo, alerta, newsjacking, temporada)
            urgency: Urgencia del contenido (hoy, esta semana, este mes)
        """
        prompt = f"""Crea un brief de contenido fiscal para el Copywriter de heru:

NOVEDAD FISCAL:
{fiscal_news}

TIPO DE CONTENIDO: {content_type}
URGENCIA: {urgency}

Genera el brief completo:

## BRIEF DE CONTENIDO FISCAL

### CONTEXTO FISCAL
[Qué está pasando — explicación técnica para el copywriter, no para el usuario final]

### AUDIENCIA OBJETIVO
[Segmento(s) de usuarios de heru que más necesitan este contenido]

### ÁNGULO PRINCIPAL
[El hook o perspectiva que hace este contenido relevante e interesante]

### MENSAJES CLAVE
1. [Mensaje 1 — el más importante]
2. [Mensaje 2]
3. [Mensaje 3 si aplica]

### LO QUE NO DEBEMOS DECIR
[Afirmaciones que podrían ser incorrectas, generar pánico injustificado o ser malinterpretadas]

---

### SUGERENCIAS POR PLATAFORMA

**Instagram (carrusel/reel):**
Hook sugerido: [primera frase que para el scroll]
Estructura: [idea de slides o guión]

**TikTok:**
Hook visual/verbal: [primeros 3 segundos]
Ángulo: [cómo hacer viral este tema]

**Facebook (grupos de conductores/freelancers):**
Ángulo: [más conversacional, dirigido a conductores y comerciantes]

---

### REFERENCIAS LEGALES PARA EL COPY
[Datos exactos que el copywriter puede usar sin riesgo legal]

### DEADLINE RECOMENDADO
{urgency}

### NOTA DE COMPLIANCE
[Si hay algo que el copy DEBE aclarar para no dar asesoría fiscal no autorizada]"""

        return self.run(prompt)

    def generate_fiscal_alert(
        self,
        alert_level: str,
        change_description: str,
        source: str,
        effective_date: Optional[str] = None,
    ) -> str:
        """
        Genera una alerta fiscal formateada para envío inmediato al equipo.

        Args:
            alert_level: CRÍTICA / IMPORTANTE / OPORTUNIDAD
            change_description: Descripción del cambio
            source: Fuente del cambio
            effective_date: Fecha de vigencia del cambio
        """
        effective_line = f"**Vigencia:** {effective_date}" if effective_date else "**Vigencia:** Por confirmar"

        prompt = f"""Genera una alerta fiscal formal para el equipo de heru:

NIVEL DE ALERTA: {alert_level.upper()}
FUENTE: {source}
{effective_line}

CAMBIO:
{change_description}

Genera la alerta en el formato estándar de heru:

## ALERTA FISCAL heru — [NIVEL: {alert_level.upper()}]

**Fuente:** {source}
**Fecha de publicación:** [hoy / fecha indicada]
{effective_line}

---

**QUÉ CAMBIÓ**
[Descripción técnica precisa del cambio — citar artículo o regla si aplica]

**QUÉ SIGNIFICA EN LENGUAJE SIMPLE**
[Una sola oración que un conductor de Uber pueda entender]

---

**IMPACTO POR SEGMENTO**
- Usuarios en RESICO: [impacto concreto]
- Usuarios en Plataformas: [impacto concreto]
- Usuarios en Empresarial/Honorarios: [impacto concreto]

---

**QUÉ DEBE HACER EL EQUIPO DE HERU**
- Producto: [acción específica o "sin acción requerida"]
- Marketing: [acción específica o "sin acción requerida"]
- Soporte: [qué esperar de preguntas de usuarios]

**OPORTUNIDAD DE CONTENIDO**
[Brief rápido para el Copywriter si aplica, o "N/A"]

**FECHA LÍMITE PARA ACTUAR**
[Si hay urgencia regulatoria — o "Sin fecha crítica inmediata"]"""

        return self.run(prompt)

    def fiscal_calendar_check(
        self,
        month: str,
        year: str = "2026",
    ) -> str:
        """
        Genera un resumen de obligaciones fiscales del mes para los segmentos de heru.
        """
        prompt = f"""Genera el resumen de obligaciones fiscales de {month} {year} relevantes
para los usuarios de heru.app (RESICO, Plataformas Tecnológicas, Actividad Empresarial):

## CALENDARIO FISCAL HERU — {month.upper()} {year}

### OBLIGACIONES DEL MES

**Para usuarios en RESICO:**
[Qué deben hacer, con fecha exacta]

**Para usuarios en Plataformas Tecnológicas (Uber/DiDi/Rappi):**
[Qué deben hacer, con fecha exacta]

**Para usuarios en Actividad Empresarial / Honorarios:**
[Qué deben hacer, con fecha exacta]

---

### FECHAS CRÍTICAS

| Fecha | Obligación | Segmento | Consecuencia si no cumple |
|-------|------------|----------|--------------------------|
[Completar con datos reales del mes]

---

### COMUNICACIONES RECOMENDADAS PARA HERU
[Qué y cuándo debe comunicar heru a sus usuarios para ayudarlos a cumplir a tiempo]

### CONTENIDO SUGERIDO
[Ideas de posts o emails alineados al calendario fiscal de este mes]

---

*Nota: Verificar contra el calendario oficial del SAT. Si el día 17 es inhábil, se recorre al siguiente día hábil.*"""

        return self.run(prompt)

    def answer_fiscal_query(self, query: str) -> str:
        """
        Responde una consulta técnica fiscal con rigor y lenguaje simple.

        Args:
            query: Pregunta fiscal técnica del equipo
        """
        prompt = f"""Responde esta consulta fiscal con rigor técnico y lenguaje simple:

CONSULTA: {query}

Estructura tu respuesta:

## CONSULTA FISCAL

### RESPUESTA DIRECTA
[La respuesta en 1-2 oraciones, sin rodeos]

### EXPLICACIÓN DETALLADA
[Desarrollo técnico de la respuesta, con citas legales exactas si aplican]

### LENGUAJE PARA EL USUARIO
[Cómo explicarle esto a un conductor de Uber o diseñador freelance]

### CASOS Y EXCEPCIONES
[Si hay situaciones donde la respuesta es diferente, señalarlas]

### FUENTE LEGAL
[Artículo exacto del CFF, LISR, RMF u otra norma]

### AMBIGÜEDADES
[Si hay zonas grises o interpretaciones posibles, señalarlas explícitamente]

---
*Distinguir claramente entre lo que dice la ley y lo que es interpretación.*"""

        return self.run(prompt)
