# 🤖 Sistema Multi-Agente heru.app

Sistema de agentes de IA especializados para automatizar y potenciar las operaciones de marketing, ventas y contenido de [heru.app](https://heru.app) — la plataforma fiscal para trabajadores independientes en México.

---

## ¿Qué hace este sistema?

Orquesta **6 agentes especializados** impulsados por Claude (Anthropic) que trabajan de forma coordinada para:

- Calificar leads de ventas automáticamente
- Crear contenido para redes sociales listo para publicar
- Generar conceptos visuales y prompts para diseño con IA
- Monitorear menciones y sentimiento en redes sociales
- Gestionar y reportar campañas de Google Ads y Meta Ads

---

## 🗂 Estructura del Proyecto

```
heru-multi-agent/
│
├── main.py                      # Punto de entrada principal
├── requirements.txt
├── .env.example                 # Variables de entorno (copiar a .env)
│
├── config/
│   └── heru_context.yaml        # 📋 Contexto compartido de heru.app
│                                #    (empresa, producto, audiencia, tono)
│
├── core/                        # Motor del sistema
│   ├── base_agent.py            # Clase base que todos los agentes heredan
│   ├── models.py                # Modelos de datos (Pydantic)
│   └── orchestration.py        # Orquestador + AgentRegistry + TaskQueue
│
└── agents/                      # Agentes especializados
    ├── orchestrator/
    │   ├── config.yaml          # Personalidad y lógica de routing
    │   └── agent.py             # OrchestratorAgent
    ├── lead_qualifier/
    │   ├── config.yaml
    │   └── agent.py             # LeadQualifierAgent
    ├── copywriter/
    │   ├── config.yaml
    │   └── agent.py             # CopywriterAgent
    ├── graphic_designer/
    │   ├── config.yaml
    │   └── agent.py             # GraphicDesignerAgent
    ├── social_listener/
    │   ├── config.yaml
    │   └── agent.py             # SocialListenerAgent
    └── performance_ads/
        ├── config.yaml
        └── agent.py             # PerformanceAdsAgent
```

---

## 🤖 Los 6 Agentes

### 1. 🧠 Orquestador Principal
**Archivo:** `agents/orchestrator/`

El cerebro del sistema. Recibe cualquier solicitud, la analiza, decide qué agente(s) deben intervenir y coordina el flujo de trabajo. Puede ejecutar agentes en secuencia (el output de uno alimenta al siguiente) o en paralelo.

**Capacidades:**
- Análisis de solicitudes y creación de planes de ejecución
- Routing inteligente por IA o por palabras clave
- Síntesis de resultados de múltiples agentes
- Priorización de tareas según impacto en el negocio

---

### 2. 🎯 Qualifier de Leads
**Archivo:** `agents/lead_qualifier/`

Evalúa el potencial de conversión de prospectos de heru usando un framework de calificación basado en necesidad fiscal, fit con el producto, urgencia y capacidad de pago.

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

Crea contenido para todas las plataformas digitales de heru, adaptando el tono y formato a cada canal. Domina el arte de convertir el miedo al SAT en contenido que detiene el scroll.

**Capacidades:**
- Posts para Instagram, Facebook, TikTok y LinkedIn
- Copy para Google Ads y Meta Ads (con variantes A/B)
- Secuencias de email (bienvenida, nurturing, re-engagement)
- Guiones completos para TikTok/Reels
- Calendarios de contenido semanales
- Adaptación de contenido entre plataformas

**Tipos de contenido:**
- 📚 **Educativo:** Explica conceptos fiscales en lenguaje simple
- 😰 **Pain point:** Activa el dolor/urgencia sin asustar
- 🌟 **Social proof:** Testimoniales y casos de éxito
- 📱 **Producto:** Features y beneficios de heru
- 📅 **Temporada:** Declaración anual, fechas SAT

---

### 4. 🎨 Diseñador Gráfico
**Archivo:** `agents/graphic_designer/`

Conceptualiza y describe assets visuales para campañas digitales. Genera prompts listos para usar en DALL-E, Midjourney y Stable Diffusion, además de briefs completos para el equipo de diseño humano.

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

Monitorea el ecosistema digital en busca de menciones de heru, conversaciones relevantes sobre impuestos en México, actividad de la competencia y oportunidades de engagement.

**Capacidades:**
- Análisis de menciones con clasificación de sentimiento
- Alertas tempranas de crisis de reputación
- Análisis competitivo vs Contalink, Alegra, CONTPAQi
- Detección de tendencias fiscales y oportunidades de newsjacking
- Identificación de leads en conversaciones públicas
- Reportes diarios, semanales y mensuales

**Clasificación de alertas:**
| Prioridad | Tipo | Tiempo de respuesta |
|-----------|------|---------------------|
| 🔴 ALTA | Bugs críticos, acusaciones, problemas de seguridad | < 30 min |
| 🟡 MEDIA | Quejas de UX, precio, funcionalidades | < 4 horas |
| 🟢 BAJA | Comentarios vagos, confusión de marca | < 24 horas |

---

### 6. 📈 Experto en Performance y Ads
**Archivo:** `agents/performance_ads/`

Gestiona la estrategia, optimización y reporte de todas las campañas de publicidad pagada: Google Ads (Search, Display, Performance Max, YouTube), Meta Ads (Facebook e Instagram) y TikTok Ads.

**Capacidades:**
- Reportes diarios, semanales y mensuales con semáforo de KPIs
- Planes de optimización con cambios específicos y paso a paso
- Estrategias completas de campaña con distribución de presupuesto
- Análisis de funnel con identificación de puntos de fuga
- Keyword research estratégico para Google Search
- Recomendaciones de A/B testing

**KPIs monitoreados:**
| Métrica | Objetivo | Alerta Roja |
|---------|----------|-------------|
| CAC | < $350 MXN | > $600 MXN |
| CPL | < $150 MXN | > $280 MXN |
| ROAS | > 4x | < 2x |
| CTR Search | > 4% | < 2% |
| Quality Score | > 7 | < 5 |

---

## ⚙️ Cómo funciona la arquitectura

```
Usuario / Sistema Externo
         │
         ▼
   ┌─────────────────┐
   │   Orchestrator   │  ← Analiza la solicitud y crea el plan
   └────────┬────────┘
            │ Delega
     ┌──────┼──────────────────────┐
     ▼      ▼          ▼          ▼
  Lead   Copywriter  Graphic  Social     Performance
Qualifier           Designer  Listener   Ads
     │      │          │          │          │
     └──────┴──────────┴──────────┴──────────┘
                       │
                       ▼
             Orchestrator sintetiza
                       │
                       ▼
              Respuesta final
```

### Flujo de trabajo

1. **Recepción**: El sistema recibe una solicitud (texto libre)
2. **Análisis**: El Orquestador analiza qué agente(s) son necesarios
3. **Planificación**: Se crea un plan con pasos ordenados
4. **Delegación**: Cada agente recibe su tarea con contexto completo
5. **Ejecución**: Los agentes trabajan con su `system_prompt` especializado
6. **Síntesis**: El Orquestador integra los resultados en una respuesta cohesiva

### Contexto compartido

Todos los agentes tienen acceso al archivo `config/heru_context.yaml` que contiene:
- Descripción de la empresa y producto
- Audiencias objetivo y sus pain points
- Tono de comunicación de la marca
- Métricas clave del negocio
- Calendario fiscal mexicano

---

## 🚀 Instalación y Uso

### 1. Clonar y configurar

```bash
# Instalar dependencias
cd heru-multi-agent
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env y agregar tu ANTHROPIC_API_KEY
```

### 2. Obtener API Key de Anthropic

1. Ve a [console.anthropic.com](https://console.anthropic.com)
2. Crea una cuenta o inicia sesión
3. En "API Keys", crea una nueva key
4. Cópiala en tu archivo `.env`

### 3. Ejecutar

```bash
# Modo interactivo (recomendado para empezar)
python main.py

# Ejecutar todos los demos
python main.py --demo

# Hablar directamente con un agente
python main.py --agent leads
python main.py --agent copy
python main.py --agent diseno
python main.py --agent social
python main.py --agent ads

# Modo silencioso (menos output)
python main.py --quiet
```

### 4. Uso desde código

```python
import anthropic
from core.orchestration import Orchestrator
from core.models import AgentRole
from agents.copywriter.agent import CopywriterAgent
from agents.lead_qualifier.agent import LeadQualifierAgent

client = anthropic.Anthropic(api_key="tu-api-key")

# Opción A: Usar el orquestador (recomendado)
orchestrator = Orchestrator(client=client)
# ... registrar agentes ...
resultado = orchestrator.process("Crea un post de Instagram sobre la declaración anual")

# Opción B: Usar agente directamente
copywriter = CopywriterAgent(client=client)
post = copywriter.create_post(
    platform="instagram",
    topic="Declaración anual SAT",
    content_type="pain_point",
    objective="conversión",
    target_segment="freelancers digitales",
)

# Opción C: Chat conversacional con un agente
qualifier = LeadQualifierAgent(client=client)
respuesta = qualifier.chat("Tengo un lead que es conductor de Uber, ¿cómo lo califico?")
```

---

## 💬 Ejemplos de solicitudes al Orquestador

```
# El orquestador detecta automáticamente qué agentes usar:

"Necesito un post de Instagram + concepto visual para promocionar que
 la declaración anual vence en abril"
→ Activa: Copywriter + Graphic Designer

"Cómo van nuestras campañas de Meta Ads esta semana?"
→ Activa: Performance Ads

"Llegó un lead por DM: es diseñadora freelance, tiene RFC pero nunca ha declarado"
→ Activa: Lead Qualifier

"Qué dicen de heru en Twitter hoy?"
→ Activa: Social Listener

"Crea una campaña completa para el mes de declaración anual"
→ Activa: Orchestrator → Copywriter + Graphic Designer + Performance Ads
```

---

## 🔧 Personalización

### Modificar la personalidad de un agente

Edita el archivo `config.yaml` de cada agente. Ejemplo para el Copywriter:

```yaml
# agents/copywriter/config.yaml
personality: >
  Tu nueva descripción de personalidad...

objectives:
  - "Nuevo objetivo 1"
  - "Nuevo objetivo 2"
```

### Agregar un nuevo agente

1. Crea el directorio: `agents/nuevo_agente/`
2. Crea `config.yaml` con la estructura estándar
3. Crea `agent.py` heredando de `BaseAgent`
4. Registra en `main.py` con `orchestrator.register_agent(role, agent)`
5. Agrega el rol en `core/models.py` → `AgentRole` enum

### Cambiar el modelo de Claude

En `.env`:
```bash
# Para producción (máxima calidad)
MODEL=claude-opus-4-6

# Para desarrollo/testing (más rápido y económico)
MODEL=claude-haiku-4-5-20251001
```

---

## 📊 Casos de uso por área

| Área | Agente(s) | Ejemplo |
|------|-----------|---------|
| **Ventas** | Lead Qualifier | Calificar leads de WhatsApp, DMs, formularios web |
| **Content** | Copywriter | Calendario semanal de posts, guiones de TikTok |
| **Diseño** | Graphic Designer | Briefs para el equipo, prompts de DALL-E |
| **Community** | Social Listener | Reporte diario de menciones, alertas de crisis |
| **Marketing** | Performance Ads | Reporte semanal de campañas, planes de optimización |
| **Campañas** | Todos | Campaña completa de declaración anual |

---

## 🏗 Próximas integraciones

- [ ] **CRM** (HubSpot / Salesforce): Crear contactos automáticamente desde leads calificados
- [ ] **Meta Ads API**: Leer métricas reales de campañas
- [ ] **Google Ads API**: Keywords, métricas y optimizaciones automatizadas
- [ ] **DALL-E 3 / Stability AI**: Generar imágenes directamente desde el Graphic Designer
- [ ] **Notion / Airtable**: Exportar calendarios de contenido
- [ ] **Slack / Teams**: Notificaciones y alertas del Social Listener
- [ ] **WhatsApp Business API**: Qualificación de leads en tiempo real

---

## 📁 Archivos de Configuración YAML

Cada agente tiene su `config.yaml` con:

| Campo | Descripción |
|-------|-------------|
| `name` | Nombre del agente |
| `role` | Identificador del rol |
| `role_description` | Descripción detallada del rol |
| `personality` | Cómo debe "comportarse" el agente |
| `objectives` | Lista de objetivos específicos |
| `behavior_instructions` | Reglas de comportamiento y formato de respuesta |
| Campos adicionales | Frameworks, métricas, plantillas específicas del rol |

El archivo `config/heru_context.yaml` es el cerebro compartido: todos los agentes lo leen al inicializarse para tener contexto de empresa, producto, audiencias y tono.

---

## 🛠 Stack Tecnológico

| Componente | Tecnología |
|------------|-----------|
| Modelo de IA | Claude (Anthropic) — claude-opus-4-6 |
| SDK | `anthropic` Python SDK |
| Configuración de agentes | YAML |
| Modelos de datos | Pydantic v2 |
| CLI / TUI | Rich |
| Variables de entorno | python-dotenv |

---

## 🇲🇽 Contexto heru.app

**heru.app** es una fintech mexicana que ayuda a trabajadores independientes (freelancers, conductores de Uber/DiDi, repartidores, profesionistas y comerciantes) a cumplir con el SAT de forma simple desde el celular.

**El problema que resuelve:** El 70%+ de los trabajadores independientes en México no declaran correctamente sus impuestos por miedo, desconocimiento o falta de tiempo. heru convierte ese miedo en tranquilidad.

**Planes:** Desde $99 MXN/mes | App en iOS y Android | +100,000 usuarios

---

*Construido con ❤️ para el equipo de heru.app*
