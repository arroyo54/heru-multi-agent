# 🤖 Sistema Multi-Agente heru.app

Sistema de agentes de IA especializados para automatizar y potenciar las operaciones de marketing, ventas y contenido de [heru.app](https://heru.app) — la plataforma fiscal para trabajadores independientes en México.

---

## ¿Qué hace este sistema?

Orquesta **8 agentes especializados** impulsados por Claude (Anthropic) que trabajan de forma coordinada para:

- Calificar leads de ventas automáticamente
- Crear contenido para redes sociales listo para publicar
- Generar conceptos visuales y prompts para diseño con IA
- Monitorear menciones y tendencias del ecosistema fiscal en redes sociales
- Gestionar y reportar campañas de Google Ads y Meta Ads
- Analizar datos de negocio y cruzar insights entre fuentes
- Monitorear cambios del SAT y generar alertas fiscales para el equipo

---

## 🗂 Estructura del Proyecto

```
heru-multi-agent/
│
├── main.py                          # Punto de entrada principal
├── requirements.txt
├── .env                             # Variables de entorno
│
├── config/
│   └── heru_context.yaml            # 📋 Contexto compartido de heru.app
│
├── core/                            # Motor del sistema
│   ├── base_agent.py                # Clase base que todos los agentes heredan
│   ├── models.py                    # Modelos de datos (Pydantic)
│   ├── orchestration.py             # Orquestador + AgentRegistry + TaskQueue
│   ├── google_chat.py               # Envío de mensajes a Google Chat
│   ├── google_sheets.py             # Subida de reportes a Google Sheets
│   ├── image_generator.py           # Generación de imágenes con IA
│   ├── scheduler.py                 # Tareas programadas (APScheduler)
│   └── connectors/
│       ├── apify.py                 # Social media scraping (Apify + Reddit API + YouTube API)
│       └── google_ads.py            # Google Ads API (demo + real)
│
├── agents/                          # Agentes especializados
│   ├── orchestrator/
│   ├── lead_qualifier/
│   ├── copywriter/
│   ├── graphic_designer/
│   ├── social_listener/
│   ├── performance_ads/
│   ├── business_analyst/
│   └── sat_intelligence/
│
├── scripts/
│   ├── weekly_report.py             # Reporte semanal Social Listener (automatizado)
│   ├── performance_report.py        # Reporte semanal Performance Ads
│   └── campaign_builder.py          # Constructor de campañas: PPT estratégico + CSVs por canal
│
├── .claude-skills/                  # Skills de Claude Code para el equipo
│   ├── remotion/                    # Best practices para video con Remotion
│   ├── copywriting/                 # Copywriting para landing pages y marketing
│   ├── paid-ads/                    # Google Ads y Meta Ads
│   ├── social-content/              # Contenido para redes sociales
│   └── ...                          # +30 skills de marketing y CRO
│
├── api/
│   └── server.py                    # FastAPI server con scheduler integrado
│
├── credentials/
│   └── google_sheets.json           # Service account Google (no commitear)
│
└── output/
    └── reports/                     # Reportes generados localmente
```

---

## 🤖 Los 8 Agentes

### 1. 🧠 Orquestador Principal
**Archivo:** `agents/orchestrator/`

El cerebro del sistema. Recibe cualquier solicitud, la analiza, decide qué agente(s) deben intervenir y coordina el flujo de trabajo. Puede ejecutar agentes en secuencia o en paralelo.

**Capacidades:**
- Análisis de solicitudes y creación de planes de ejecución
- Routing inteligente por IA o por palabras clave
- Síntesis de resultados de múltiples agentes
- Priorización de tareas según impacto en el negocio

---

### 2. 🎯 Qualifier de Leads
**Archivo:** `agents/lead_qualifier/`

Evalúa el potencial de conversión de prospectos usando un framework de calificación basado en necesidad fiscal, fit con el producto, urgencia y capacidad de pago.

**Capacidades:**
- Lead scoring 0-100 con desglose por criterio
- Clasificación HOT 🔥 / WARM ⚡ / COLD ❄️
- Identificación de segmento (conductor, freelancer, profesionista, comerciante)
- Generación de mensajes personalizados por perfil
- Manejo de objeciones con respuestas sugeridas
- Calificación desde conversaciones de chat

**Segmentos que identifica:**
| Segmento | Plataformas | Mensaje principal |
|----------|------------|-------------------|
| Conductor | Uber, DiDi, inDriver | "El SAT ya sabe cuánto ganas" |
| Delivery | Rappi, Uber Eats | "Tu plataforma reporta al SAT" |
| Freelancer digital | Diseño, dev, marketing | "Tus clientes necesitan CFDI" |
| Profesionista | Médicos, abogados | "Deduce correctamente" |
| Comerciante online | Mercado Libre, Shopify | "Tus ventas se reportan al SAT" |

---

### 3. ✍️ Copywriter de Contenido
**Archivo:** `agents/copywriter/`

Crea contenido para todas las plataformas digitales de heru, adaptando el tono y formato a cada canal. Convierte el miedo al SAT en contenido que detiene el scroll.

**Capacidades:**
- Posts para Instagram, Facebook, TikTok y LinkedIn
- Copy para Google Ads y Meta Ads (con variantes A/B)
- Secuencias de email (bienvenida, nurturing, re-engagement)
- Guiones completos para TikTok/Reels
- Calendarios de contenido semanales
- Adaptación de contenido entre plataformas

**Tipos de contenido:**
- 📚 **Educativo:** Explica conceptos fiscales en lenguaje simple
- 😰 **Pain point:** Activa la urgencia sin asustar
- 🌟 **Social proof:** Testimoniales y casos de éxito
- 📱 **Producto:** Features y beneficios de heru
- 📅 **Temporada:** Declaración anual, fechas SAT

---

### 4. 🎨 Diseñador Gráfico
**Archivo:** `agents/graphic_designer/`

Conceptualiza assets visuales para campañas digitales. Genera prompts listos para usar en herramientas de IA generativa y briefs completos para el equipo de diseño.

**Capacidades:**
- Conceptos visuales con brief + prompt de IA
- Storyboards para carruseles (slide por slide)
- Prompts optimizados para DALL-E 3, Midjourney y Stable Diffusion
- Guiones visuales para videos/Reels
- Briefs para creativos de campañas de ads
- Especificaciones técnicas por plataforma

**Identidad visual de heru:**
- Color principal: `#00C48C` (verde heru)
- Estilo: Flat design moderno, ilustraciones de personas mexicanas diversas
- Mood: Tranquilizador, empoderador, tecnológico pero humano

---

### 5. 👂 Social Listener
**Archivo:** `agents/social_listener/`
**Script:** `scripts/weekly_report.py`

Monitorea el ecosistema digital en **dos tracks simultáneos**:
- **Track A — Brand:** qué dice la gente DE heru (menciones directas, sentimiento, crisis)
- **Track B — Ecosystem:** qué habla la gente sobre impuestos, SAT, RESICO, freelancers y conductores — miedos, dolores, oportunidades de mercado

Genera un reporte semanal automático todos los lunes que envía un resumen ejecutivo a Google Chat y sube el análisis completo a Google Sheets.

**Fuentes de datos:**
| Plataforma | Método | Costo |
|------------|--------|-------|
| Reddit | JSON API pública | Gratis |
| YouTube | YouTube Data API v3 | Gratis |
| Twitter/X | Apify | Créditos |
| TikTok | Apify | Créditos |
| Instagram | Apify | Créditos |
| Facebook Grupos | Apify | Créditos |

**Subreddits monitoreados:**
`r/mexico`, `r/MexicoFinanciero`, `r/FinanzasPersonales`, `r/freelance`, `r/digitalnomad`, `r/mexicoexpats`, `r/MexicoCity`, `r/sidehustle`, `r/SATMexico`

**Capacidades de análisis:**
- Miedos y ansiedades del ecosistema fiscal
- Dolores y frustraciones de freelancers y conductores
- Preguntas frecuentes (oportunidades de contenido)
- Trending topics de la semana
- Insights accionables para producto y marketing
- Alertas de crisis de reputación de heru

**Uso:**
```bash
python scripts/weekly_report.py --preview   # corre sin mandar a Chat
python scripts/weekly_report.py --send      # manda a Google Chat
python scripts/weekly_report.py --quora     # reporte quincenal de Quora
```

---

### 6. 📈 Experto en Performance y Ads
**Archivo:** `agents/performance_ads/`
**Script:** `scripts/performance_report.py`
**Conector:** `core/connectors/google_ads.py`

Gestiona la estrategia, optimización y reporte de campañas de publicidad pagada. Se conecta a Google Ads API para leer métricas reales; incluye modo demo con datos de ejemplo realistas para presentaciones.

**Capacidades:**
- Reportes semanales/mensuales con semáforo de KPIs (✅ ⚠️ 🔴)
- Planes de optimización con cambios específicos paso a paso
- Estrategias completas de campaña con distribución de presupuesto
- Análisis de funnel con identificación de puntos de fuga
- Keyword research estratégico para Google Search
- Recomendaciones de A/B testing con reglas de validación

**KPIs monitoreados:**
| Métrica | Objetivo | Alerta Roja |
|---------|----------|-------------|
| CAC | < $350 MXN | > $600 MXN |
| CPL | < $150 MXN | > $280 MXN |
| ROAS | > 4x | < 2x |
| CTR Search | > 4% | < 2% |
| Quality Score | > 7 | < 5 |

**Uso:**
```bash
python scripts/performance_report.py          # modo demo
python scripts/performance_report.py --real   # datos reales (requiere credenciales)
python scripts/performance_report.py --days 30 # período de 30 días
```

---

### 7. 📊 Business Analyst
**Archivo:** `agents/business_analyst/`

Analiza datos de negocio, cruza información entre fuentes y genera insights estratégicos para la toma de decisiones. Especializado en el contexto de heru: métricas de adquisición, retención, comportamiento fiscal y estacionalidad.

**Capacidades:**
- Análisis de reportes con contexto de negocio heru
- Correlaciones cruzadas entre fuentes (ads + social + SAT + ventas)
- Presentaciones ejecutivas con narrativa de datos
- Insights de campañas de marketing con recomendaciones de presupuesto
- Resúmenes ejecutivos semanales multi-fuente
- Validación o refutación de hipótesis de negocio

**Ejemplo de uso:**
```python
analyst = BusinessAnalystAgent(client=client)

# Cruzar social listening + performance ads
insight = analyst.cross_analyze(
    sources={"social": social_report, "ads": ads_report},
    hypothesis="Los usuarios de RESICO convierten mejor por urgencia fiscal"
)
```

---

### 8. 🏛 SAT Intelligence
**Archivo:** `agents/sat_intelligence/`

Monitorea cambios del SAT, analiza su impacto en los usuarios de heru y genera alertas, contenido y planes de acción para el equipo. Es el experto fiscal del sistema.

**Capacidades:**
- Análisis de actualizaciones del SAT con impacto segmentado por tipo de usuario
- Evaluación de riesgo para conductores, freelancers y profesionistas
- Briefs de contenido urgente ante cambios regulatorios
- Alertas fiscales con tono empático (nunca alarmista)
- Calendario fiscal proactivo con recordatorios
- Respuestas a preguntas fiscales complejas de usuarios

**Tipos de alertas:**
| Urgencia | Ejemplo | Acción |
|----------|---------|--------|
| 🔴 INMEDIATA | Cambio en fecha de declaración | Push notification + post mismo día |
| 🟡 ESTA SEMANA | Nueva obligación RESICO | Email + contenido educativo |
| 🟢 ESTE MES | Recordatorio declaración anual | Campaña de nurturing |

---

## ⚙️ Arquitectura del Sistema

```
Usuario / Sistema Externo / Scheduler
              │
              ▼
    ┌─────────────────┐
    │   Orchestrator   │  ← Analiza y crea el plan de ejecución
    └────────┬────────┘
             │ Delega
    ┌─────────────────────────────────────────┐
    │         │         │         │           │
    ▼         ▼         ▼         ▼           ▼
  Lead    Copywriter  Graphic  Social     Performance
Qualifier           Designer  Listener      Ads
                                │              │
                         Business Analyst ◄────┘
                                │
                         SAT Intelligence
    │         │         │         │           │
    └─────────┴─────────┴─────────┴───────────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
        Google Chat           Google Sheets
     (resumen ejecutivo)    (reporte completo)
```

### Integraciones activas

| Integración | Para qué | Estado |
|------------|----------|--------|
| Google Chat Webhook | Envío de reportes y alertas | ✅ Activo |
| Google Sheets | Reportes completos con histórico | ✅ Activo |
| Reddit JSON API | Social listening ecosistema | ✅ Activo |
| YouTube Data API v3 | Social listening videos | ✅ Activo |
| Apify | TikTok, Instagram, Facebook, Twitter | ⏳ Créditos |
| Google Ads API | Métricas de campañas reales | 🔧 Pendiente credenciales |
| APScheduler | Reporte automático lunes 8am CDMX | ✅ Activo |

---

## 🚀 Instalación y Uso

### 1. Instalar dependencias

```bash
cd heru-multi-agent
pip install -r requirements.txt
```

### 2. Configurar variables de entorno

```bash
# Variables requeridas en .env:
ANTHROPIC_API_KEY=...          # console.anthropic.com
APIFY_API_TOKEN=...            # apify.com
GOOGLE_API_KEY=...             # console.cloud.google.com
GOOGLE_CHAT_WEBHOOK_URL=...    # Google Chat → Espacios → Webhooks
GOOGLE_SHEETS_ID=...           # ID de tu Google Sheet
```

### 3. Ejecutar

```bash
# Modo interactivo
python main.py

# Hablar directamente con un agente
python main.py --agent leads
python main.py --agent copy
python main.py --agent diseno
python main.py --agent social
python main.py --agent ads
python main.py --agent analyst
python main.py --agent sat

# Reportes automáticos
python scripts/weekly_report.py --preview
python scripts/performance_report.py

# Constructor de campañas (PPT estratégico + CSVs por canal)
python scripts/campaign_builder.py
```

### 4. Uso desde código

```python
import anthropic
from agents.copywriter.agent import CopywriterAgent
from agents.lead_qualifier.agent import LeadQualifierAgent
from agents.business_analyst.agent import BusinessAnalystAgent
from agents.sat_intelligence.agent import SATIntelligenceAgent

client = anthropic.Anthropic(api_key="tu-api-key")

# Copywriter
copywriter = CopywriterAgent(client=client)
post = copywriter.create_post(platform="instagram", topic="Declaración anual SAT")

# Lead qualifier
qualifier = LeadQualifierAgent(client=client)
score = qualifier.qualify_lead("Conductor de Uber, tiene RFC, nunca ha declarado")

# Business analyst
analyst = BusinessAnalystAgent(client=client)
insight = analyst.cross_analyze(sources={"social": data1, "ads": data2})

# SAT intelligence
sat = SATIntelligenceAgent(client=client)
alerta = sat.analyze_sat_update("Nueva regla RESICO — baja automática a 2 meses")
```

---

## 💬 Ejemplos de solicitudes al Orquestador

```
"Necesito un post de Instagram + concepto visual para la declaración anual"
→ Activa: Copywriter + Graphic Designer

"¿Cómo van nuestras campañas de Meta Ads esta semana?"
→ Activa: Performance Ads

"Llegó un lead por DM: es diseñadora freelance, tiene RFC pero nunca ha declarado"
→ Activa: Lead Qualifier

"El SAT cambió las reglas de RESICO, ¿qué hacemos?"
→ Activa: SAT Intelligence → Copywriter + Performance Ads

"Dame un resumen cruzado del social listening y el performance de esta semana"
→ Activa: Business Analyst
```

---

## 📊 Casos de uso por área

| Área | Agente(s) | Frecuencia |
|------|-----------|------------|
| **Ventas** | Lead Qualifier | Continuo |
| **Content** | Copywriter + Graphic Designer | Diario |
| **Community** | Social Listener | Automático lunes |
| **Marketing** | Performance Ads | Automático lunes |
| **Estrategia** | Business Analyst | Semanal / demanda |
| **Fiscal** | SAT Intelligence | On-demand + alertas |
| **Campañas** | Todos | Temporadas SAT |

---

## 🏗 Próximas integraciones

- [ ] **Meta Ads API** — leer métricas reales de Facebook e Instagram Ads
- [ ] **Google Ads API** — conectar con credenciales reales (estructura lista)
- [ ] **YouTube API key** — habilitar en Google Cloud (estructura lista)
- [ ] **CRM (HubSpot)** — crear contactos desde leads calificados
- [ ] **WhatsApp Business API** — calificación de leads en tiempo real
- [ ] **Pipeline Social → Copy** — insights de Reddit alimentan ideas de contenido automáticamente

---

## 🛠 Stack Tecnológico

| Componente | Tecnología |
|------------|-----------|
| Modelo de IA | Claude Opus 4.6 (Anthropic) |
| SDK | `anthropic` Python SDK |
| Config de agentes | YAML |
| Modelos de datos | Pydantic v2 |
| CLI / TUI | Rich |
| API Server | FastAPI + Uvicorn |
| Tareas programadas | APScheduler |
| Social scraping | Apify + Reddit JSON API + YouTube Data API |
| Reportes | Google Sheets (gspread) + Google Chat Webhook |
| Variables de entorno | python-dotenv |
| Deploy | Railway |

---

## 🧩 Claude Code Skills

La carpeta `.claude-skills/` contiene **34 skills** listos para usar en Claude Code. El equipo puede instalarlos localmente con:

```bash
cp -r .claude-skills/* ~/.claude/skills/
```

Una vez instalados, se invocan desde Claude Code con `/nombre-del-skill`:

| Skill | Uso |
|-------|-----|
| `/remotion` | Best practices para video con Remotion |
| `/copywriting` | Copy para landing pages, hero sections, CTAs |
| `/paid-ads` | Estrategia y copy para Google Ads y Meta Ads |
| `/social-content` | Posts para LinkedIn, Instagram, TikTok, X |
| `/email-sequence` | Secuencias de email y drip campaigns |
| `/ab-test-setup` | Diseño de experimentos A/B |
| `/analytics-tracking` | GA4, GTM, planes de tracking |
| `/pricing-strategy` | Estrategia de precios y packaging |
| `/churn-prevention` | Flows de cancelación y retención |
| `/seo-audit` | Auditoría SEO técnica y on-page |
| + 24 más | CRO, lead magnets, RevOps, SEO, etc. |

---

## 🇲🇽 Contexto heru.app

**heru.app** es una fintech mexicana que ayuda a trabajadores independientes (freelancers, conductores de Uber/DiDi, repartidores, profesionistas y comerciantes) a cumplir con el SAT de forma simple desde el celular.

**El problema que resuelve:** El 70%+ de los trabajadores independientes en México no declaran correctamente sus impuestos por miedo, desconocimiento o falta de tiempo. heru convierte ese miedo en tranquilidad.

**Planes:** Desde $99 MXN/mes | App en iOS y Android | +100,000 usuarios

---

*Construido con ❤️ para el equipo de heru.app*
