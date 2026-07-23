# Registro de supuestos y riesgos iniciales

Documento vivo, actualizado por cada agente. Esta primera versión (Fase 1) contiene únicamente supuestos y riesgos **metodológicos/estructurales de arranque** — no los riesgos sustantivos del contenido del proyecto (corrupción, captura, sanciones FIFA, etc.), que se detallan formalmente en la Fase 8 (Agente 16, Red Team) sobre el diseño ya construido, y se irán registrando aquí a medida que cada agente los identifique en su ámbito.

## 1. Registro de supuestos

| ID | Supuesto | Justificación | Sensibilidad | Consecuencia si es falso | Validación requerida |
|---|---|---|---|---|---|
| S-01 | México cuenta con capacidad instalada (infraestructura, ligas, academias, capital humano) suficiente para que el 70% de las acciones de los primeros 4 años sean de reforma/integración, no de creación | Principio rector del proyecto (Parte I) | Alta — si la capacidad real es menor, la regla del 70% no es alcanzable sin bajar el estándar de calidad | Confirmar con el inventario del Agente 1 (Fase 2) |
| S-02 | Existe suficiente información pública/semipública (Nivel A/B) sobre presupuestos y gobernanza de FMF/Liga MX/clubes para sustentar recomendaciones estructurales | Regla metodológica de la sección 3.2 | Alta — si la transparencia es baja, gran parte del diagnóstico caería en evidencia C/D | Agentes 1–4 deben declarar explícitamente los vacíos de información al cierre de Fase 2 |
| S-03 | Los benchmarks internacionales (Fase 4) son parcialmente transferibles a México sin necesitar adaptación total | Parte VII, matriz de transferibilidad | Media | Si las condiciones previas de los países de referencia no existen en México, el benchmark aporta menos de lo esperado | Agentes 5A–5E deben calificar cada caso como aplicable directo / con adaptación / difícil / no recomendable |
| S-04 | Es posible diseñar reformas de gobernanza y competencia sin incurrir en injerencia gubernamental sancionable por FIFA | Parte VI y sección 29 del prompt maestro | Alta — un diseño que la viole podría hacer inviable todo el pilar jurídico | Agente 3 debe validar cada propuesta jurídica contra los estatutos FIFA vigentes |
| S-05 | El calendario de 22 semanas de investigación/diseño (sección 7 del manual metodológico) es alcanzable con la disponibilidad real de fuentes primarias | Estimación de proceso, nivel de confianza C | Media | Retrasos en respuesta de instituciones (FMF, Conade, SEP, estados) extienden el calendario | Recalibrar al cierre de cada control |

## 2. Registro de riesgos iniciales

Riesgos que afectan la **viabilidad del proceso de investigación y diseño en sí** (no todavía riesgos del contenido sustantivo del proyecto, que corresponden al Agente 16 en Fase 8):

| Riesgo | Probabilidad | Impacto | Señal temprana | Responsable | Mitigación | Contingencia |
|---|---|---|---|---|---|---|
| Falta de transparencia de FMF/Liga MX/clubes sobre presupuestos y gobernanza | Alta | Alto | Solicitudes de información sin respuesta o incompletas en Fase 2 | Agente 1, 2, 4 | Declarar vacío explícitamente, usar fuentes Nivel B, solicitar vía convenio institucional | Avanzar con supuesto provisional marcado (Registro de supuestos) hasta validación |
| Agentes de diseño (Fase 5) se adelantan a proponer soluciones sin esperar línea base/benchmark completos | Media | Alto | Entregables de Fase 5 sin referencias a hallazgos de Fase 2–4 | Agente 0 | Control 2 y 3 bloquean formalmente el inicio de Fase 5 | Devolver el entregable al agente autor |
| Recomendaciones que impliquen injerencia gubernamental incompatible con FIFA | Media | Alto — riesgo de sanción a toda la Selección/clubes | Propuestas jurídicas o de gobernanza que doten a una entidad pública de facultades de decisión deportiva | Agente 3, Agente 16 | Revisión jurídica obligatoria contra estatutos FIFA en Control 4 | Reformular la propuesta antes de Control 5 |
| Volumen de información (32 países, 14 pilares, 18 agentes) supera la capacidad de síntesis coherente | Alta | Medio | Entregables inconsistentes entre agentes al llegar a Fase 6 | Agente 0 | Uso estricto de la plantilla de 26 puntos y registros maestros para forzar comparabilidad | Fase 6 (integración preliminar) elimina duplicidades y contradicciones antes de continuar |
| Cambio de autoridades (FMF, gobierno federal/estatal) durante el proceso interrumpe la continuidad de insumos o compromisos | Media | Alto | Cambios de titulares en instituciones clave durante la investigación | Agente 2, Agente 15 | Diseñar el pacto nacional (Parte XI) con mecanismos de continuidad independientes de personas | Recalendarizar y re-confirmar compromisos con nuevas autoridades |
| Presión por producir resultados/anuncios antes de completar el diagnóstico | Media | Medio | Solicitudes de publicar conclusiones antes del Control 8 | Agente 0 | Recordar la instrucción de arranque: no resolver el proyecto completo en una sola ejecución | Publicar únicamente los entregables de fase ya aprobados, no el proyecto completo |

## 3. Registros aún no aplicables en Fase 1

- **Registro de contradicciones** — se activa en la Fase 3, cuando existan hallazgos sustantivos de los Agentes 1–4 que puedan entrar en conflicto entre sí (por ejemplo, una cifra de presupuesto reportada distinto por Liga MX vs. un club).
- **Registro de decisiones** — se activa desde la Fase 3 en adelante, para documentar cada vez que el Agente 0 (o quien apruebe) elige entre alternativas propuestas por distintos agentes.

Ambos registros deben crearse como archivos independientes (`05-registro-contradicciones.md`, `06-registro-decisiones.md`) al iniciar la Fase 3, con las columnas especificadas en la Parte XXIII del prompt maestro.
