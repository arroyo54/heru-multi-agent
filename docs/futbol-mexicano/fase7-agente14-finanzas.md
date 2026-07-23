# Fase 7 — Agente 14: Finanzas
## Presupuesto del diseño de los 14 pilares (Fase 5-6) — escenarios, costos unitarios, fuentes y sensibilidad

**Fecha de entrega:** 2026-07-23
**Agente:** 14 — Finanzas (Fase 7, en paralelo con el Agente 15 — Implementación, luego reconciliados)
**Insumos recibidos:** `00-agente0-metodologia-y-plan.md`, `02-plantilla-entregable.md`, `05-fase3-linea-base-consolidada.md`, `08-fase4-benchmark-consolidado.md`, los ocho entregables de Fase 5 (`fase5-agente6` a `fase5-agente13`), `09-fase6-integracion-preliminar-diseno.md`, `03-registro-preguntas.md`, `04-registro-supuestos-riesgos.md`.
**Naturaleza de este entregable:** este agente **no diseña** ningún pilar nuevo. Costea lo ya diseñado y reconciliado en las Fases 5-6, en pesos mexicanos (MXN) salvo indicación contraria, con nivel de confianza explícito por cifra. No se reabre investigación de campo; se usan las cifras y órdenes de magnitud ya citados por los Agentes 6-13, complementados con dos verificaciones puntuales de mercado (costo de rehabilitación/construcción de canchas en México, 2025-2026) para calibrar unidades de obra que ningún agente de diseño había costeado.

---

## 1. Resumen ejecutivo

**[RECOMENDACIÓN]** El diseño de los 14 pilares (Fase 5-6) es, tal como advirtió la Fase 6 (sección 7), mayoritariamente barato: ~89% de las recomendaciones sustantivas son auditoría, reglamento, convenio, currícula o base de datos, no obra ni institución nueva. Este entregable traduce eso en tres escenarios de presupuesto anual recurrente (año 4-8, régimen estable) — **conservador ≈ $260-290 millones MXN/año**, **intermedio ≈ $650-700 millones MXN/año**, **transformador ≈ $1,450-1,550 millones MXN/año** (confianza C, con partidas individuales C-D) —, más un componente de inversión inicial (años 1-4) de $90-100M (conservador), $135-150M (intermedio) y $175-200M (transformador). Comparado con el único ancla financiera dura de la línea base (ingresos de Liga MX: 600-900 millones USD/año, ≈ $11,400-17,100 millones MXN/año a un tipo de cambio de referencia de 19 MXN/USD, confianza B), incluso el escenario transformador representa **menos del 14% de un solo año de ingresos de la liga**, y el escenario conservador, menos del 2.5%. El rubro de **mayor magnitud absoluta no es infraestructura nueva sino rehabilitación escolar de bajo costo unitario aplicada a escala nacional** (patios sin instalación deportiva, 32.9% de escuelas según INEGI) — consistente con la jerarquía de intervención, pero relevante porque el volumen, no el costo unitario, es lo que produce la cifra grande. Se detectaron y evitaron dos duplicidades de costeo (certificación de academias fusionada Agentes 6+7, currícula técnica unificada Agentes 6+8) y se identifican **cinco rubros sin fuente de financiamiento creíble hoy** (fondo de incentivo tipo allocation money, fondo/redistribución para la Liga MX Femenil, fútbol adaptado a gran escala, minutos de contenido comunitario en TV como ingreso, y uso del 5% de solidaridad doméstica como fuente activa) que se marcan explícitamente como **no costeados en firme**, no como partidas infladas para cuadrar el presupuesto. El mayor riesgo financiero transversal es la opacidad financiera de Liga MX/FMF (S-02, S-06, riesgo ya documentado en la línea base): mientras no se resuelva, una parte no trivial del escenario transformador permanece aspiracional.

---

## 2. Objetivo

Costear —no diseñar— las recomendaciones ya reconciliadas de los ocho pilares de Fase 5 (Agentes 6-13) e integradas por el Agente 0 en la Fase 6, separando inversión de operación, construyendo tres escenarios presupuestales con desglose por rubro, evaluando el realismo de cada fuente de financiamiento posible, calculando costos unitarios aproximados con nivel de confianza explícito, y realizando un análisis de sensibilidad ante los riesgos macro y de gobernanza ya identificados en fases anteriores. Responde directamente a PG-23 (¿Cuánto costará?) y PG-24 (¿Quién pagará?) del registro maestro de preguntas.

---

## 3. Preguntas

Del registro maestro (`03-registro-preguntas.md`):

| ID | Pregunta | Respuesta de este entregable |
|---|---|---|
| PG-23 | ¿Cuánto costará? | Secciones 6-9 (escenarios, rubros, costos unitarios) |
| PG-24 | ¿Quién pagará? | Sección 10 (fuentes de financiamiento) |
| PQ-D07 | ¿ROI real de la inversión en fuerzas básicas? | No respondida — depende de series de datos que el Agente 10 aún no produce (sección 8, limitaciones); se marca como pregunta pendiente (sección 26) |

Preguntas de fases anteriores que este entregable **no puede resolver**, pero que condicionan directamente la precisión de su propio costeo (heredadas de `09-fase6-integracion-preliminar-diseno.md`, sección 4, y tratadas aquí explícitamente como supuestos de costeo, no como certezas):

- PQ-A05 (entrenadores certificados por nivel) — condiciona el costo real de escalar licenciamiento (sección 7.3).
- PQ-A07/PQ-C06 (qué certifica y qué % de academias están supervisadas) — condiciona el costo real de la certificación fusionada (sección 7.2).
- Verificación de integración SIID-FIFA Connect ID (Agente 10) — condiciona si el Pilar 9 es gestión de verificación (barato) o desarrollo técnico mayor (caro).
- S-N04 (Agente 11, si ya existe cuerpo colegiado equivalente al Comité Técnico de Continuidad) — condiciona si ese costo es de reforma o de creación.
- PQ-D03/PQ-D04 (montos reales de TV y de solidaridad FIFA cobrada) — condiciona toda fuente de financiamiento basada en derechos audiovisuales o solidaridad (sección 10).
- S-06 (cifras autorreportadas de la FMF sin auditoría) — condiciona el universo real de academias, canchas y jugadores sobre el que se calculan todos los costos unitarios (sección 9).

---

## 4. Metodología

**Fuentes usadas:** los ocho entregables de Fase 5, la integración de Fase 6, la línea base (Fase 3) y el benchmark (Fase 4) ya cerrados; dos verificaciones puntuales de mercado mexicano 2025-2026 sobre costo de canchas de fútbol (rehabilitación y construcción con pasto sintético), realizadas mediante búsqueda web dirigida el 23 de julio de 2026, para calibrar la única categoría de obra física de este proyecto que ningún agente de diseño había costeado en pesos.

**Clasificación de evidencia (sección 3.2 del manual metodológico):** este entregable **no genera evidencia A ni B nueva** — no existen estados financieros auditados de FMF/Liga MX/clubes/academias que permitan un presupuesto de nivel A. Toda cifra de este documento es **nivel C** (inferencia razonable/analogía de mercado, con orden de magnitud verificable) o **D** (estimación exploratoria sin ancla de mercado, marcada como tal). Las únicas cifras de nivel B heredadas —y usadas solo como referencia de escala, no como partida presupuestal— son: ingresos de Liga MX (600-900 millones USD/año), inversión del CAR (390 millones MXN), multa COFECE 2021 (177.6 millones MXN) y los rangos de costo que los Agentes 8 y 10 ya calcularon en sus propios entregables (reproducidos aquí sin modificación, solo consolidados).

**Periodo cubierto:** presupuesto de la primera fase de implementación (años 1-4, inversión) y régimen estable proyectado (años 4-8, operación recurrente), con nota cualitativa sobre el horizonte de 12-20 años donde aplica. No se costea el proyecto completo a 20 años con cifras nominales fijas — sería una falsa precisión dado el nivel de evidencia disponible (ver sección 11, sensibilidad a inflación).

**Regla de no duplicidad aplicada:** siguiendo `09-fase6-integracion-preliminar-diseno.md` (sección 2), este entregable costea **una sola vez** (a) la certificación de academias fusionada (Agentes 6+7) y (b) la currícula técnica nacional unificada (Agentes 6+8), en vez de sumar los costos que cada agente de origen mencionó por separado.

---

## 5. Hallazgos

1. Solo dos de los ocho pilares de Fase 5 (Agentes 8 y 10) entregaron una tabla de costos en pesos con orden de magnitud propio; los otros seis (Agentes 6, 7, 9, 11, 12, 13) dejaron el costeo explícitamente para esta fase, con solo indicaciones cualitativas de "bajo/medio/alto costo relativo". Este entregable debe, por tanto, construir el 75% del presupuesto desde cero, con menor ancla que el 25% restante.
2. El único rubro de este proyecto donde existe una obra física de gran escala nacional (rehabilitación de patios escolares sin instalación deportiva, 32.9% de escuelas) no tenía ninguna cifra unitaria en pesos en el diseño original (Agente 9, sección 18, remite explícitamente a este agente). La verificación de mercado (sección 4) permitió construir un rango unitario razonable.
3. Cinco rubros del diseño están explícitamente condicionados por sus propios agentes de origen a "transparencia financiera mínima de Liga MX/FMF" que hoy no existe (Agentes 6, 8, 10, 11, 12, 13, todos de forma independiente). Este entregable no inventa una fuente para esos rubros — los marca como no costeados en firme (sección 10.4).
4. El costeo agregado, incluso en su escenario más ambicioso, es una fracción pequeña de los ingresos ya documentados de Liga MX — un dato relevante para el Agente 16 (Red Team): la barrera a este proyecto no es la disponibilidad de dinero en el sistema, es la disposición a redirigirlo con transparencia verificable.

---

## 6. Evidencia

| Cifra | Fuente | Fecha | Alcance | Metodología | Limitaciones | Confianza |
|---|---|---|---|---|---|---|
| Ingresos Liga MX: 600-900 millones USD/año | `fase2-agente4-economia-del-futbol.md`, reproducido en `05` | 2026 | Nacional, liga | Rango disperso de fuentes periodísticas/institucionales, sin estado financiero consolidado auditado | Rango amplio (50% de variación), sin desglose por partida | B |
| Inversión CAR (COM): 390 millones MXN | `fase2-agente1-capacidades-existentes.md` | 2025-2026 | Nacional (un solo activo) | Cifra institucional (FIFA Forward + FMF) | Sin desglose público del uso de los 390 mdp (hallazgo ya citado por el Agente 9) | B |
| Multa COFECE a FMF/17 clubes: 177.6 millones MXN | `fase2-agente3-derecho-y-regulacion.md` | 2021 | Nacional | Resolución administrativa pública | Es sanción, no gasto de formación — se usa solo como referencia de escala | B |
| Costo estimado de formar un jugador hasta primer equipo: $7-10 millones MXN | `05-fase3-linea-base-consolidada.md`, Bloque D | 2026 | Nacional | No auditada, cifra periodística/de industria | Sin desglose de qué incluye (academia, staff, competencia); se usa solo como referencia, no como partida | C |
| Costo de fuerzas básicas para una familia: $0 a >$40,000 MXN/año | Profeco 2026, citado en `05` | 2026 | Nacional, muestreo de academias | Encuesta de precios al consumidor | No es censo, es muestreo; heterogeneidad no explicada | B |
| Costo unitario licencia D/C (beca): $1,500-3,000 MXN/becario | `fase5-agente8-entrenadores-ciencia.md`, sección 18 | 2026 | Nacional | Analogía con capacitación vocacional de corta duración en México | Sin cifra oficial FMF del costo real de emisión de licencia | C |
| Rehabilitación de cancha pública municipal: $500,000-$17,000,000 MXN según alcance | Verificación de mercado, búsqueda web dirigida (Chihuahua, Querétaro, Tamaulipas, Estado de México, 2025-2026) | 2025-2026 | Municipal, muestra de 6 casos publicados en prensa local | Casos individuales reportados por gobiernos municipales, no una muestra aleatoria representativa | Alta dispersión según si incluye solo pasto/portería o remodelación integral con graderío/iluminación | C |
| Pasto sintético instalado: $250-520 MXN/m² ($55,000-85,000 fútbol 5; $180,000-260,000 fútbol 7; $550,000-900,000 fútbol 11) | Verificación de mercado, proveedores comerciales (Sportmaster y comparables), 2025-2026 | 2025-2026 | Nacional, precios de proveedores comerciales | Cotizaciones públicas de proveedores, no licitación pública | Precio de proveedor privado, no de obra pública con licitación (que puede diferir por sobrecostos administrativos) | C |

---

## 7. Fuentes

- FMF. Certificación de Academias (`certificacionacademias.fmf.mx`), formalización prevista agosto 2026 — citada en `fase5-agente6` y `fase5-agente7`.
- `fase5-agente8-entrenadores-ciencia.md`, sección 18 (tabla de costos propia).
- `fase5-agente10-datos-scouting.md`, sección 18 (tabla de costos propia).
- `fase5-agente6-formacion-fuerzas-basicas.md`, `fase5-agente7-escuela-universidad-comunidad.md`, `fase5-agente9-infraestructura.md`, `fase5-agente11-selecciones.md`, `fase5-agente12-cultura-medios.md`, `fase5-agente13-femenil-inclusion.md` (indicaciones cualitativas de costo, secciones 18/21 según numeración de cada uno).
- INEGI, Inventario Nacional de Viviendas / censo de escuelas, citado en `fase5-agente9`, sección 5 (32.9% de escuelas sin instalaciones deportivas).
- Búsqueda web dirigida, 23 de julio de 2026: notas de gobiernos municipales de Chihuahua, Querétaro, Tamaulipas y Estado de México sobre costo de rehabilitación de canchas (2025-2026); Sportmaster y comparables, precios de pasto sintético 2025-2026.
- `04-registro-supuestos-riesgos.md` (S-02, S-06, S-10, S-11, riesgos de opacidad financiera).

---

## 8. Limitaciones

- **No existe un estado financiero auditado de la FMF, Liga MX ni de ningún club** — la limitación más determinante de este entregable. Todo costo de este documento es una estimación de orden de magnitud, no un presupuesto de línea de partida verificable contra cifras reales de la industria.
- **No existe un censo verificado de jugadores, academias ni canchas** (S-06) — los costos unitarios de la sección 9 dependen de universos (número de academias, número de canchas, número de jugadores) que son autorreportados, no auditados. Si el universo real es distinto (mayor o menor), el costo total cambia proporcionalmente aunque el costo unitario no cambie.
- **Las dos verificaciones de mercado de este agente (sección 4) son una muestra pequeña y no aleatoria** (casos publicados en prensa local, cotizaciones de proveedores comerciales) — sirven para fijar un orden de magnitud razonable, no un presupuesto de obra pública licitado.
- **No se costea el proyecto completo a 20 años en cifras nominales fijas** — dado que ni la inflación acumulada ni el universo real de beneficiarios son predecibles con la evidencia disponible, cualquier cifra a 20 años sería una falsa precisión. Se da orientación cualitativa (sección 11).
- **Cinco rubros no se costean en absoluto** (sección 10.4) por ausencia de fuente de financiamiento verificable — esto es una limitación deliberada, no un vacío accidental.
- Este entregable no evalúa el retorno social o deportivo de la inversión (PQ-D07) — solo su costo y su fuente. La pregunta de si el gasto "vale la pena" corresponde a los indicadores de cada pilar (Fase 5) y a la síntesis final (Fase 10, Agente 17).

---

## 9. Activos existentes

Este agente no diagnostica activos nuevos — reutiliza los ya documentados por los Agentes 1 y 6-13, en particular como **base para no costear como "inversión nueva" lo que ya es gasto corriente ya presupuestado**:

- Legado físico del Mundial 2026 (3 estadios, 8 canchas FIFA Arena, CAR-COM renovado con 390 mdp) — ya pagado; este entregable solo costea su **mantenimiento futuro**, no su construcción.
- Pirámide de licencias D→C→B→A→PRO y portal `formacionacademica.fmf.mx` — ya existente; se costea su extensión digital, no su creación.
- SIID (Sistema Integral de Información Deportiva) — ya existente y ya reconocido (D-01) como sistema doméstico de registro; se costea su extensión, no una plataforma nueva.
- Red de scouting escolar (28,000+ escuelas) y +2,000 academias certificadas/en trámite — ya existentes y ya operando con presupuesto propio (de las familias/academias/clubes); se costea solo el costo incremental de auditoría, acceso económico y datos, no la operación de la red en sí.
- Fundaciones de clubes (Chivas, América, Pachuca) y canales de contenido de fuerzas básicas (Tigres, Pachuca) — ya operando con presupuesto propio de los clubes; se costea solo el costo incremental de escalar el formato, no la fundación completa.
- CIRT, Premio Nacional de Periodismo, patrocinios ya comprometidos (Comex, Henkel) — ya existentes; se costea solo el costo marginal de coordinación.

---

## 10. Problemas

Los problemas de fondo (poder de veto de la Asamblea de Dueños, opacidad financiera, incentivo punitivo no premial, vacío de protección de menores) ya fueron diagnosticados en Fases 2-6 y no se repiten aquí. El problema específico de **este** agente es:

1. Ningún pilar de Fase 5, salvo dos, costeó su propio diseño en pesos — este entregable debe construir esos números sin caer en falsa precisión.
2. No existe, en ninguna fuente pública consultada durante todo el proyecto, un costo unitario oficial de: auditoría de academia, cancha inventariada, o beca de jugador — los tres costos unitarios más citados en el encargo de esta misión (sección 9 de este documento) debieron construirse por analogía, no por dato primario.
3. El diseño de Fase 5 dejó, correctamente, cinco piezas de alto valor potencial (fondo de incentivo, fondo femenil, fútbol adaptado, contenido comunitario en TV, solidaridad FIFA) condicionadas a datos que no existen — este agente debe resistir la tentación de "rellenar" esas piezas con una cifra inventada solo para presentar un presupuesto que cuadre.

---

## 11. Alternativa de mejora

No aplica en el sentido estricto de la plantilla (este agente no reforma un activo existente) — el equivalente aquí es: **mejorar la precisión de este mismo presupuesto** en cuanto se resuelvan los bloqueadores de datos ya señalados por la Fase 6 (sección 4) y por los Agentes 8 y 10 (PQ-A05, PQ-A07/PQ-C06, integración FIFA Connect ID). Este documento debe tratarse como una primera versión a recalibrar, no como cifra definitiva.

## 12. Alternativa de integración

Los tres presupuestos por auditoría externa (academias, entrenadores, datos/scouting — Agentes 6, 8 y 10 respectivamente) pueden integrarse en un solo contrato marco de auditoría deportiva con tres módulos y un mismo despacho/consorcio auditor rotativo, en vez de tres contratos separados — reduce costos fijos de coordinación (un solo proceso de licitación, un solo reporte anual consolidado) sin fusionar el contenido técnico de cada módulo (que sigue siendo distinto: calidad de academia, licenciamiento de entrenador, integridad de datos). Se estima un ahorro de coordinación de 5-10% sobre la suma de los tres presupuestos de auditoría por separado (confianza D, sin verificación de mercado directa).

## 13. Alternativa de escalamiento

El presupuesto de este documento está diseñado, por construcción, como una escala gradual de tres escenarios (sección 14) más que como una alternativa aislada — el escenario conservador puede escalarse al intermedio y luego al transformador sin rediseñar la arquitectura de rubros, simplemente ampliando cobertura (más escuelas rehabilitadas, más becarios, más academias auditadas por ciclo).

## 14. Alternativa de sustitución

No aplica — este agente no sustituye ningún mecanismo de diseño; solo costea alternativas ya decididas en Fase 5-6.

## 15. Necesidad de nueva capacidad

No aplica — este agente no propone ninguna institución, plataforma o mecanismo nuevo. Todo lo que aquí se costea ya fue evaluado contra las 14 preguntas de justificación por su agente de diseño de origen (ver `09-fase6-integracion-preliminar-diseno.md`, sección 5: solo 6 elementos de todo el diseño necesitaron esa justificación, y los seis ya la tienen).

---

## 16. Recomendación (priorizada)

1. **[RECOMENDACIÓN — máxima prioridad]** Adoptar el **escenario intermedio** (sección 14.2) como presupuesto de referencia para los primeros 4 años, no el conservador ni el transformador: el conservador retrasa recomendaciones que ya tienen vehículo institucional listo (certificación de agosto 2026, extensión del SIID) sin razón financiera real (son baratas), y el transformador incluye escalamiento de rehabilitación escolar y becas a un ritmo que ni el propio Agente 15 (Implementación, aún no entregado) ha validado como ejecutable en 4 años.
2. **[RECOMENDACIÓN]** Financiar la certificación de academias fusionada (sección 17.2) por cuota de licenciamiento autofinanciable, con un puente de arranque de un solo ejercicio fiscal (año 1) vía fondos FIFA Forward/formación ya existentes — no crear una línea presupuestal pública nueva para esta pieza.
3. **[RECOMENDACIÓN]** No comprometer, en ningún escenario, presupuesto en firme para los cinco rubros sin fuente creíble (sección 10.4) — tratarlos como "presupuesto contingente" que solo se activa si su condición de desbloqueo (transparencia financiera de Liga MX, verificación de discapacidad, renegociación de contratos de TV) efectivamente ocurre.
4. **[RECOMENDACIÓN]** Priorizar en el año 1 el desembolso más pequeño y de mayor apalancamiento informativo de todo el presupuesto: el inventario nacional georreferenciado de canchas (Agente 9, recomendación 1) — sin él, ningún costo unitario de infraestructura de este documento (el más grande en magnitud absoluta) puede refinarse ni priorizarse territorialmente.
5. **[RECOMENDACIÓN]** Fusionar el contrato de auditoría externa de academias, entrenadores y datos/scouting en un solo vehículo de contratación con tres módulos técnicos (sección 12), para capturar la eficiencia de coordinación sin diluir el estándar técnico de cada módulo.
6. **[RECOMENDACIÓN]** Recalibrar este presupuesto formalmente en el año 2, una vez que: (a) la FMF confirme el universo real de academias/canchas/licencias (PQ-A05, PQ-A07/PQ-C06), y (b) se resuelva, aunque sea parcialmente, la transparencia financiera de Liga MX (S-02) — no esperar hasta el año 4.

---

## 17. Responsable

- FMF (Dirección de Administración y Finanzas / Formación Académica / ENDIT / Certificación de Academias / Dirección de Sistemas): ejecutor primario de la mayoría de los rubros (entrenadores, academias, tecnología, selecciones, protección).
- Asamblea de Dueños de Liga MX: responsable de decidir sobre cualquier rubro que implique costo de cumplimiento para los clubes (licenciamiento condicionado, coordinación de calendario) y sobre la viabilidad de los rubros condicionados a transparencia financiera.
- CONADE / institutos estatales del deporte / SEP / municipios: responsables del rubro de mayor magnitud absoluta (infraestructura escolar/municipal), vía presupuesto público ya existente, no vía un fondo nuevo del proyecto.
- Comité Olímpico Mexicano: responsable del mantenimiento del CAR (ya renovado).
- CIRT, Consejo Ciudadano del Premio Nacional de Periodismo: responsables del rubro de comunicación (bajo costo, autofinanciado por la propia industria).
- Agente 15 (Implementación, Fase 7, en reconciliación con este entregable): responsable de calendarizar el desembolso de cada rubro contra el cronograma de dependencias ya señalado por cada agente de Fase 5.
- Agente 0 (Fase 9, Control 6): verificación final de que este presupuesto cumple los cuatro requisitos del Control 6 (inversión, operación, fuente permanente, sensibilidad).

---

## 18. Costo

Ver desglose completo en las secciones 14 (escenarios), 8 (rubros) y 9 (unitarios). Resumen de los tres escenarios (recurrente anual en régimen estable, años 4-8; confianza C, partidas individuales C-D):

| Escenario | Operación recurrente/año | Inversión inicial (años 1-4, acumulada) | % de un año de ingresos de Liga MX (rango 600-900 M USD ≈ $11,400-17,100 M MXN) |
|---|---|---|---|
| Conservador | $260-290 millones MXN | $90-100 millones MXN | 1.5-2.5% |
| Intermedio | $650-700 millones MXN | $135-150 millones MXN | 4.5-6.1% |
| Transformador | $1,450-1,550 millones MXN | $175-200 millones MXN | 9.6-13.6% |

*(Tipo de cambio de referencia 19 MXN/USD, confianza D, solo para esta comparación de escala — no se usa en ningún cálculo de rubro, todos denominados en MXN.)*

## 19. Tiempo

- **Año 1:** desembolso concentrado en verificaciones de bajo costo (inventario de canchas, auditoría de integración FIFA Connect ID, publicación de registros existentes) y en el arranque de la certificación de academias fusionada — la mayor parte del gasto de este año es de auditoría/coordinación, no de obra.
- **Años 2-4:** rampa de becas, mentores/analistas regionales, primeros ciclos de rehabilitación escolar priorizados por el inventario, primeras auditorías completas de academias y entrenadores.
- **Años 4-8:** régimen estable (las cifras de la sección 18/14 corresponden a este horizonte); posible primera recalibración con datos ya auditados.
- **Años 8-20:** fuera del alcance de costeo nominal de este documento (ver sección 8, limitaciones, y sección 11 de análisis de sensibilidad); se advierte cualitativamente que el costo real por unidad debería **caer** en este horizonte si las metas de auditabilidad (Agente 10, indicador 23.4: de 0% a 100% de cifras verificadas externamente en 8 años) se cumplen, porque el costo marginal de verificar sistemas ya digitalizados es menor que el de auditar sistemas en papel.

## 20. Dependencias

- Que el Agente 15 (Implementación) calendarice el desembolso de cada rubro contra las dependencias ya fijadas por cada agente de Fase 5 (en particular: el inventario de infraestructura, recomendación 1 del Agente 9, es dependencia dura de toda priorización territorial de rehabilitación/construcción).
- Que se resuelva, aunque sea parcialmente, la transparencia financiera de Liga MX/FMF (S-02, S-06) — condición para activar cualquiera de los cinco rubros hoy no costeados en firme (sección 10.4).
- Que la FMF confirme el universo real de academias, licencias y canchas (PQ-A05, PQ-A07/PQ-C06) — condición para refinar los costos unitarios de la sección 9 de estimación a cálculo verificado.
- Que el Agente 16 (Red Team, Fase 8) revise este presupuesto contra el criterio de que ninguna reforma puede depender solo de la buena voluntad de la Asamblea de Dueños (advertencia central del benchmark, `08`, sección 4) — varios rubros de este documento (licenciamiento condicionado, coordinación de calendario) dependen de que ese actor no bloquee su costo de cumplimiento.

## 21. Riesgos

Ver detalle completo en la sección 11 (análisis de sensibilidad). Resumen de los riesgos financieros de mayor probabilidad e impacto:

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| La opacidad financiera de Liga MX/FMF persiste más allá del año 4, manteniendo bloqueados los cinco rubros de la sección 10.4 de forma permanente, no solo temporal | Alta | Alto | Diseñar el presupuesto (como se hizo aquí) para que el escenario intermedio no dependa de esos rubros; tratarlos como upside, no como base |
| El universo real de academias/canchas/jugadores es sustancialmente mayor al autorreportado (S-06), y el costo total de auditoría/rehabilitación resulta 30-50% mayor al estimado aquí | Media-Alta | Alto | Fijar el año 1 (inventario, auditoría de integración) como paso obligatorio antes de comprometer presupuesto plurianual en firme para rehabilitación/auditoría a gran escala |
| Los municipios con menor capacidad fiscal no pueden aportar la contraparte esperada para uso compartido/mantenimiento, generando implementación desigual por región | Alta | Medio-Alto | Priorizar, dentro del presupuesto federal/estatal, los municipios de mayor déficit confirmado por el inventario, no un reparto proporcional parejo |
| Cambio de gobierno federal (2030) o estatal/municipal interrumpe la continuidad del financiamiento de infraestructura escolar, el rubro de mayor magnitud absoluta de este presupuesto | Media | Alto | Etiquetar presupuesto plurianual (siguiendo la recomendación ya hecha por el Agente 9 para el mantenimiento del legado 2026), no anual discrecional |
| El fondo con bolsa de dinero o el fondo femenil se implementen de forma prematura, antes de que exista transparencia financiera verificable, repitiendo el patrón de "reforma de papel" ya advertido por el benchmark | Media | Alto | Este documento no costea esos rubros en firme, precisamente para no crear la apariencia de que ya tienen fuente resuelta |

## 22. Bloqueadores

- Ausencia de estados financieros auditados de FMF/Liga MX/clubes — bloqueador transversal de todo este documento (no exclusivo de un rubro).
- Ausencia de un censo verificado de academias/canchas/jugadores — bloqueador directo de la precisión de los costos unitarios (sección 9).
- La Asamblea de Dueños de Liga MX, como actor de mayor poder de veto documentado, puede bloquear cualquier rubro que perciba como costo de cumplimiento no compensado (licenciamiento condicionado, coordinación de calendario, incentivo premial).
- Capacidad fiscal desigual de municipios — ya señalado por el Agente 9 como bloqueador de los convenios de uso compartido y ahora heredado por este presupuesto para el rubro de mayor magnitud.
- Falta de respuesta de FMF/Liga MX a solicitudes de transparencia pendientes desde la Fase 2 — bloqueador directo de la activación de los cinco rubros de la sección 10.4.

## 23. Indicadores

- % del presupuesto anual ejecutado vs. presupuestado, por rubro y por escenario (fuente: Agente 15/dashboard de implementación; frecuencia: anual).
- % de los cinco rubros no costeados en firme (sección 10.4) que logran desbloquear una fuente verificable en cada ciclo de 2 años (fuente: este agente, en su recalibración; frecuencia: bianual) — indicador de si la opacidad financiera se está resolviendo o no.
- Costo real de auditoría por academia, por entrenador certificado y por cancha rehabilitada, comparado contra el rango estimado de este documento, una vez exista al menos un ciclo de ejecución real (fuente: despacho auditor/CONADE; frecuencia: anual) — indicador de calibración del propio presupuesto.
- % del universo de academias/canchas/jugadores confirmado por auditoría externa/inventario, sobre el total autorreportado (mismo indicador ya fijado por el Agente 10, sección 23.4, reutilizado aquí como condición de precisión presupuestal).
- Variación real del tipo de cambio y de la inflación acumulada contra los supuestos de la sección 11, medida en cada recalibración presupuestal (fuente: Banco de México; frecuencia: anual).

## 24. Casos internacionales

Ningún caso del benchmark (`08-fase4-benchmark-consolidado.md`) ofrece una cifra de presupuesto directamente comparable y auditada que este agente pueda usar como ancla — es la misma limitación de opacidad financiera que afecta a México, en mayor o menor grado, a casi todos los países estudiados salvo aquellos con financiamiento público explícito (Noruega/Suecia, vía monopolio estatal de juego, clasificado ya como "difícil de aplicar" a México por el Agente 6 y el Agente 9). El único punto de referencia de escala relativa disponible es cualitativo: en ningún caso exitoso del benchmark (Uruguay, Corea del Sur, Alemania, Bélgica) la reforma dependió de una inversión de capital comparable, en proporción a los ingresos del fútbol local, a la de "construir una gran academia" — consistente con el criterio de esta misión de no sobreestimar el presupuesto total.

## 25. Adaptación a México

No aplica en el sentido de adaptar un mecanismo extranjero — este entregable adapta, en cambio, el **nivel de precisión** que exige la plantilla (`02-plantilla-entregable.md`, "Formato de cifras") a la realidad de que México no tiene, hoy, ningún estado financiero deportivo auditado públicamente: por eso este documento presenta rangos con nivel de confianza explícito en vez de cifras puntuales, y declara cinco rubros como no costeables en vez de inventar una cifra para parecer completo.

## 26. Preguntas pendientes

Ver sección "Preguntas nuevas para el registro maestro" más abajo.

---

# Parte 2 — Desarrollo del costeo

## Anexo A. Duplicidades evitadas (aplicación de la sección 2 de `09-fase6-integracion-preliminar-diseno.md`)

1. **Certificación de academias (Agentes 6+7):** se costea **una sola vez** en la sección A.2 de abajo, con sus tres capas (auditoría técnica del Agente 6, criterio de acceso económico y Sello de Compatibilidad Académica del Agente 7) como un solo contrato/proceso, no tres.
2. **Currícula técnica nacional (Agentes 6+8):** se costea **una sola vez**, dentro del rubro "Entrenadores" (es la misma currícula vista desde el ángulo del entrenador que la certifica), no también dentro de "Academias" ni como línea aparte.
3. **Vínculo CONDDE/CONADEIP–FMF (Agentes 7+10):** el Convenio Marco (Agente 7) se costea en el rubro "Academias/Becas"; la interoperabilidad de datos que el Agente 10 construye **sobre** ese convenio se costea en el rubro "Tecnología" — no son el mismo gasto, pero se marca explícitamente su secuencia de dependencia para que el Agente 15 no calendarice el segundo antes del primero.
4. **Auditoría externa (Agentes 6, 8 y 10):** se presenta como un solo vehículo de contratación con tres módulos (Anexo A.13), no tres contratos ni tres cifras sumadas de forma redundante.

---

## A.1 Rubro: Infraestructura (mantenimiento, rehabilitación, uso compartido, ampliación, construcción nueva)

Pilar 10 (Agente 9), con la enmienda obligatoria del Agente 13 (variable de disponibilidad por rama, protocolo de seguridad vespertino/nocturno, accesibilidad universal) ya incorporada al alcance, no como línea aparte.

**Estimación propia de este agente [ESTIMACIÓN, confianza C, con verificación de mercado propia — ver sección 4 y 6]:**

| Componente | Conservador | Intermedio | Transformador | Base del cálculo |
|---|---|---|---|---|
| Inventario nacional georreferenciado (una vez) | $8-10M | $10-12M | $12-15M | Analogía con el costo de integración de datos ya existentes del Agente 10 (más barato por ser consolidación pura, sin desarrollo de plataforma) |
| Mantenimiento plurianual del legado 2026 (CAR-COM + FIFA Arena; los 3 estadios se asumen mantenidos por sus operadores/clubes) | $20M/año | $35M/año | $50M/año | Analogía de 5-13% anual del valor de un activo deportivo renovado (390 mdp del CAR) sobre la porción no cubierta por el operador |
| Rehabilitación de patios escolares sin instalación (nivelación, portería, marcaje, malla) | 300 escuelas/año × $200,000 = $60M/año | 1,000 escuelas/año × $250,000 = $250M/año | 2,500 escuelas/año × $300,000 = $750M/año | Verificación de mercado (sección 4/6): paquete básico sin pasto sintético, cotizado por debajo del rango de fútbol 7 con pasto ($180-260K), reflejando alcance menor (patio existente, no cancha nueva) |
| Uso compartido (seguro de responsabilidad civil, gestor comunitario) | $5M/año | $10M/año | $15M/año | Estimación por analogía con costos de gestión comunitaria/seguro de instalaciones de escala similar |
| Ampliación FIFA Arena (módulos futsal) | $0 (diferido) | $1-2M/año (amortizado) | $2-3M/año (amortizado) | 8 canchas × $300,000-600,000, una vez, amortizado sobre 4 años |
| Construcción nueva (3-5 centros regionales, condicionada al inventario) | $0 (diferido hasta confirmar déficit) | $30M/año (amortizado) | $40M/año (amortizado, ritmo acelerado) | Analogía con remodelación integral de multideportivo municipal documentada ($17M) escalada a un centro regional algo mayor ($15-30M) |
| **Subtotal recurrente/año** | **≈ $85-90M** | **≈ $290-300M** | **≈ $810-820M** | |
| **Inversión inicial (inventario, una vez)** | **$8-10M** | **$10-12M** | **$12-15M** | |

**Nota de escala:** este es, en todos los escenarios, el rubro de mayor magnitud absoluta del presupuesto completo — no porque su costo unitario sea alto (es, de hecho, el más barato por unidad de todo el proyecto, consistente con la jerarquía de intervención), sino porque el déficit (32.9% de escuelas) es de escala nacional. **[HALLAZGO]** Esto no contradice la instrucción de no sobreestimar el presupuesto: sigue siendo rehabilitación, no construcción nueva, y su costo por escuela ($200,000-$300,000) es una fracción pequeña del costo de una cancha profesional o de un centro de alto rendimiento.

---

## A.2 Rubro: Academias (certificación fusionada Agentes 6+7 — auditoría técnica + acceso económico + Sello de Compatibilidad Académica)

**[ESTIMACIÓN, confianza C-D]**

- Universo de referencia: +2,000 academias certificadas/en trámite (cifra autorreportada, S-06, confianza B como hecho de que la cifra existe, D en cuanto a su exactitud).
- Auditoría externa (visita + informe técnico-deportivo + acceso económico + compatibilidad académica, tres capas en un solo reporte): $8,000-18,000 MXN por auditoría, ciclo de verificación de 3 años (no todas las academias se auditan cada año) → 650-700 auditorías/año en régimen estable.
- Sello de Compatibilidad Académica (coordinación FMF-SEP, sin estructura propia): costo marginal, absorbido en gran parte por el presupuesto administrativo ya existente de ambas dependencias.

| | Conservador | Intermedio | Transformador |
|---|---|---|---|
| Auditorías/año | ~500 | ~700 | ~1,000 (ciclo más corto, 2 años) |
| Costo/año | $15-17M | $22-25M | $30-34M |
| Puente de arranque (año 1, antes de que la cuota de licenciamiento cubra el costo) | $6M | $8M | $10M |

**Fuente prevista:** cuota de licenciamiento de las propias academias (autofinanciable, escalonada por tamaño/ingreso de la academia para no repetir el riesgo de "pay to play" ya señalado por el Agente 7), con puente de arranque vía fondos FIFA Forward/formación ya existentes. **No requiere presupuesto público nuevo en régimen estable.**

---

## A.3 Rubro: Entrenadores (Pilar 8, Agente 8 — cifra reproducida, no recalculada)

**[ESTIMACIÓN, confianza C-D — cifra original del Agente 8]:** $50-90 millones MXN/año (años 1-4), incluyendo escalamiento digital de Licencia D, becas de Licencia D/C, cuerpo de mentores regionales, becas de especialización, y auditoría externa de entrenadores (este último componente, $3-6M/año, es uno de los tres módulos del vehículo de auditoría fusionado, Anexo A.13).

| | Conservador | Intermedio | Transformador |
|---|---|---|---|
| Costo/año | $50M (extremo bajo del rango del Agente 8) | $70M (punto medio) | $90M (extremo alto del rango del Agente 8) |

No se recalcula esta cifra — se adopta íntegramente la estimación del agente de diseño de origen, que ya incluye su propia base de cálculo por componente (ver `fase5-agente8-entrenadores-ciencia.md`, sección 18).

---

## A.4 Rubro: Becas (jugadores de bajos recursos — distinto de las becas de entrenadores, ya contadas en A.3)

**[ESTIMACIÓN, confianza D — el propio Agente 6 (sección 21) señala que este es "el componente más nuevo y que requiere estimación en Fase 7"]**

- Becas parciales (transporte, materiales, cuota subsidiada) para jugadores de las etapas 9-12 a 16-18 años identificados por scouting escolar/academias certificadas en municipios de bajo ingreso, no becas integrales de alojamiento (esas ya están contempladas en la certificación de academias, sección A.2, como condición de licencia, sin costo público directo).
- Costo unitario: $8,000-20,000 MXN/jugador/año (ancla: rango Profeco de costo total de fuerzas básicas, $0-$40,000/año; la beca cubre una fracción, no el total).

| | Conservador | Intermedio | Transformador |
|---|---|---|---|
| Becarios/año | 3,000 | 10,000 | 25,000 |
| Costo unitario promedio | $10,000 | $10,000 | $10,000 |
| Costo/año | $30M | $100M | $250M |

**Nota de confianza:** esta es, junto con el rubro de infraestructura escolar, la partida con menor ancla de mercado de todo el documento — no existe cifra pública de cuántos jugadores serían elegibles ni de cuánto costaría en la práctica una beca parcial estandarizada. Se marca D explícitamente y se recomienda validar con un piloto de 1 año antes de comprometer la escala intermedia/transformadora.

---

## A.5 Rubro: Tecnología (Pilar 9, Agente 10 — cifra reproducida, no recalculada)

**[ESTIMACIÓN, confianza C-D — cifra original del Agente 10]:** $70-130 millones MXN una vez (años 1-4) + $50-90 millones MXN/año en régimen, incluyendo auditoría de integración FIFA Connect ID, extensión del SIID, módulos de datos (pruebas físicas, lesiones, escolaridad, video, minutos), esquema común de datos con CONDDE/CONADEIP, y el módulo de datos/scouting del vehículo de auditoría fusionado (incremento marginal $2-4M/año sobre el presupuesto de auditoría de entrenadores).

| | Conservador | Intermedio | Transformador |
|---|---|---|---|
| Inversión inicial (una vez) | $70M | $100M | $130M |
| Costo recurrente/año | $50M | $70M | $90M |

No se recalcula — se adopta íntegramente la estimación del Agente 10.

---

## A.6 Rubro: Competencias (licenciamiento de club condicionado, incentivo premial regulatorio)

**[ESTIMACIÓN, confianza C]** Costo administrativo de diseñar y operar el sistema de licenciamiento condicionado (escalonado Liga MX/Expansión primero) y el ajuste regulatorio de incentivo premial (cupos de extranjeros/prioridad en fondos, sin bolsa de dinero): mayormente costo de cumplimiento para los propios clubes (auditoría de sus academias, ya contada en A.2), no gasto nuevo del proyecto. Costo administrativo directo (FMF/Liga MX, personal jurídico y de reglamento): $2-8M MXN/año según escenario.

El **fondo con bolsa de dinero (allocation money)** que el propio Agente 6 marcó como "categoría 7, condicionado a transparencia financiera" **no se costea en ningún escenario** — ver sección 10.4.

---

## A.7 Rubro: Transporte (rural, escolar, acceso a canchas rehabilitadas)

**[ESTIMACIÓN, confianza D]** Ampliación de rutas ya existentes (escolares/públicas) hacia canchas rehabilitadas en zonas rurales, más transporte subsidiado para jugadores de la etapa 13-15/16-18 identificados en zonas periféricas (Agente 6, sección 17). Costo estimado por analogía con subsidios de transporte escolar de escala municipal: $10-20M/año (conservador), $30-50M/año (intermedio), $60-100M/año (transformador) — escala con el número de escuelas rehabilitadas (A.1) y becarios (A.4).

---

## A.8 Rubro: Selecciones (Pilar 13, Agente 11)

**[ESTIMACIÓN, confianza C-D]**

| Componente | Conservador | Intermedio | Transformador |
|---|---|---|---|
| Comité Técnico de Continuidad (honorarios, 7-9 miembros técnicos) | $2-3M/año | $3-4M/año | $4-5M/año |
| Manual metodológico y protocolo de transición (documentación, una vez) | $2M (una vez) | $3M (una vez) | $4M (una vez) |
| Expediente único de selecciones (marginal sobre el SIID extendido, A.5) | $0 (diferido) | $3-5M (una vez) | $5-8M (una vez) |
| Unidad de Captación y Competencia por Talento Binacional (2-4 responsables + logística/consular) | $0 (diferido) | $10-15M/año | $18-25M/año |
| **Subtotal recurrente/año** | **≈ $3-4M** | **≈ $15-25M** | **≈ $27-35M** |

**Nota:** en el escenario conservador se difiere deliberadamente la Unidad de Captación Binacional — es la única de las dos piezas de categoría 7 del Agente 11 que tiene un costo real de personal/logística; el Comité Técnico de Continuidad (la otra pieza de categoría 7) es barata (reforma estatutaria + honorarios) y se mantiene en los tres escenarios.

---

## A.9 Rubro: Cultura y comunicación (Pilar 12, Agente 12)

**[ESTIMACIÓN, confianza C]** Boletín de desarrollo trimestral, protocolo CIRT, Mesa de Estándares, categoría de premio periodístico — todo de bajo costo por diseño explícito del propio Agente 12 (ningún rubro requiere presupuesto público nuevo relevante).

| | Conservador | Intermedio | Transformador |
|---|---|---|---|
| Costo/año | $2-3M | $4-6M | $6-10M |

---

## A.10 Rubro: Fútbol femenil e inclusión (Pilar 11, Agente 13 — porción costeable)

**[ESTIMACIÓN, confianza C-D]** Estabilización de nomenclatura, reportes de transparencia salarial, paridad de observación en scouting, cuota de horas de infraestructura, extensión del convenio de protección a personal adulto (R8) — todo de bajo costo administrativo, en gran parte marginal a los rubros ya costeados en A.1-A.5 y A.8 (la corrección de la auditoría transversal no es una línea de gasto nueva, es un criterio añadido a rubros ya presupuestados).

| | Conservador | Intermedio | Transformador |
|---|---|---|---|
| Costo/año (porción costeable) | $2-3M | $5-8M | $8-12M |

**No costeado (sección 10.4):** Fondo de Desarrollo Femenil (R17) y redistribución de derechos comerciales hacia Liga MX Femenil (R13) — condicionados a la misma transparencia financiera de Liga MX que bloquea el fondo de incentivo del Agente 6. Fútbol adaptado a gran escala (R19) — condicionado a la verificación de línea base (R18) que hoy no existe.

---

## A.11 Rubro: Protección (menores y, por extensión del Agente 13, adultas)

**[ESTIMACIÓN, confianza C-D]** Convenio administrativo FMF-SIPINNA, canal de denuncia independiente, verificación de antecedentes/código de conducta del cuerpo técnico, extensión a protección de adultas.

| | Conservador | Intermedio | Transformador |
|---|---|---|---|
| Costo/año | $5M | $15-20M | $25-35M |

Escala principalmente por el costo de verificación de antecedentes penales a escala (estimado en $300-600 MXN por verificación individual, escalado según el número de entrenadores licenciados que se busca cubrir, ligado a la meta de cobertura de licenciamiento del Agente 8, sección 23).

---

## A.12 Rubro: Investigación (verificaciones de los bloqueadores de datos)

**[ESTIMACIÓN, confianza C]** Estudios/verificaciones puntuales, una vez: verificación primaria del reglamento de la regla de menores (D-02), verificación de la ponderación de voto en la Asamblea FMF, verificación de integración SIID-FIFA Connect ID (parcialmente ya contada en A.5), verificación de estructuras de discapacidad (R18 del Agente 13), estudio comparativo del "sobreprecio" del jugador mexicano (S-11).

| | Conservador | Intermedio | Transformador |
|---|---|---|---|
| Costo (una vez, año 1-2) | $8M | $15M | $20M |

---

## A.13 Rubro: Auditoría (vehículo consolidado de tres módulos)

**No se suma como línea aparte** para evitar doble conteo: el costo de auditoría de academias está en A.2, el de entrenadores en A.3 (dentro del rango del Agente 8) y el de datos/scouting en A.5 (dentro del rango del Agente 10, más el incremento marginal ya señalado). Este apartado solo documenta la **recomendación de consolidación operativa** (sección 12 de la Parte 1) y su ahorro estimado de coordinación (5-10% sobre la suma de los tres, confianza D, no incluido en los totales de la sección 14 para no anticipar un ahorro no verificado).

## A.14 Rubro: Personal (honorarios/coordinación no contados en otros rubros)

**[ESTIMACIÓN, confianza D]** Honorarios de comités (ya contados en A.8), coordinadores de convenio (FMF-CONDDE-CONADEIP-SEP, FMF-SIPINNA) y gestores comunitarios de uso compartido (ya contados parcialmente en A.1) — este rubro captura solo el remanente de coordinación interinstitucional no asignado a un rubro sustantivo específico.

| | Conservador | Intermedio | Transformador |
|---|---|---|---|
| Costo/año | $5M | $15-18M | $25-35M |

---

## 14. Escenarios consolidados

### 14.1 Escenario conservador — recurrente ≈ $260-290M MXN/año; inversión inicial ≈ $90-100M MXN

| Rubro | $/año (recurrente) |
|---|---|
| Infraestructura | 85-90M |
| Entrenadores | 50M |
| Academias | 15-17M |
| Becas | 30M |
| Tecnología | 50M |
| Competencias | 2M |
| Transporte | 10-20M |
| Selecciones | 3-4M |
| Comunicación | 2-3M |
| Fútbol femenil (porción costeable) | 2-3M |
| Protección | 5M |
| Personal | 5M |
| **Total recurrente** | **≈ 260-290M** |
| Inversión inicial (inventario + tecnología + investigación + puente academias) | ≈ 92-98M |

**Perfil:** ejecuta solo lo que ya tiene vehículo institucional listo y bajo costo de coordinación; difiere la Unidad de Captación Binacional y la construcción nueva de infraestructura; escala becas y rehabilitación escolar al ritmo más lento.

### 14.2 Escenario intermedio — recurrente ≈ $650-700M MXN/año; inversión inicial ≈ $135-150M MXN

| Rubro | $/año (recurrente) |
|---|---|
| Infraestructura | 290-300M |
| Entrenadores | 70M |
| Academias | 22-25M |
| Becas | 100M |
| Tecnología | 70M |
| Competencias | 4M |
| Transporte | 30-50M |
| Selecciones | 15-25M |
| Comunicación | 4-6M |
| Fútbol femenil (porción costeable) | 5-8M |
| Protección | 15-20M |
| Personal | 15-18M |
| **Total recurrente** | **≈ 650-700M** |
| Inversión inicial | ≈ 135-150M |

**Perfil — recomendado (sección 16, recomendación 1):** ejecuta el diseño de Fase 5-6 al ritmo que los propios agentes de origen indicaron como "corto-mediano plazo" para la mayoría de sus recomendaciones, con escalamiento gradual del licenciamiento condicionado y la Unidad de Captación Binacional operando en su versión básica.

### 14.3 Escenario transformador — recurrente ≈ $1,450-1,550M MXN/año; inversión inicial ≈ $175-200M MXN

| Rubro | $/año (recurrente) |
|---|---|
| Infraestructura | 810-820M |
| Entrenadores | 90M |
| Academias | 30-34M |
| Becas | 250M |
| Tecnología | 90M |
| Competencias | 8M |
| Transporte | 60-100M |
| Selecciones | 27-35M |
| Comunicación | 6-10M |
| Fútbol femenil (porción costeable) | 8-12M |
| Protección | 25-35M |
| Personal | 25-35M |
| **Total recurrente** | **≈ 1,450-1,550M** |
| Inversión inicial | ≈ 175-200M |

**Perfil:** acelera rehabilitación escolar y becas a escala nacional casi completa en 4 años, amplía la Unidad de Captación Binacional, acelera construcción nueva de centros regionales (dentro del límite de 3-5 que el propio Agente 9 fijó como techo de 4 años). **No incluye** los cinco rubros de la sección 10.4 aun en su versión más ambiciosa — "transformador" describe el ritmo de ejecución de lo ya diseñado, no la invención de fuentes de financiamiento que hoy no existen.

---

## 9 (bis). Costos unitarios aproximados

| Unidad | Rango estimado | Confianza | Base |
|---|---|---|---|
| Por academia auditada (tres capas: técnica + acceso económico + compatibilidad académica) | $8,000-18,000 MXN por visita/informe | D | Analogía con auditoría de cumplimiento de pequeña escala en México; sin cifra de mercado directa de auditoría deportiva |
| Por entrenador certificado (beca Licencia D/C) | $1,500-3,000 MXN/becario | C | Cifra propia del Agente 8, por analogía con capacitación vocacional de corta duración |
| Por cancha rehabilitada (paquete básico: nivelación, portería, marcaje, malla) | $200,000-500,000 MXN | C | Verificación de mercado 2025-2026 (sección 4/6); varía según si incluye pasto sintético |
| Por cancha con rehabilitación media (+ iluminación + seguridad perimetral) | $1,000,000-3,000,000 MXN | C | Verificación de mercado (casos municipales documentados de $500,000 a $5,800,000) |
| Por cancha inventariada (solo consolidación de datos, sin obra) | $500-2,000 MXN/cancha | D | Estimación por analogía con costo de verificación de campo ligera; universo real de canchas desconocido (bloqueador) |
| Por centro regional multiuso construido (nivel 5, condicionado) | $15,000,000-30,000,000 MXN | C | Analogía con remodelación integral de multideportivo municipal documentada ($17,000,000) |
| Por jugador atendido (beca parcial: transporte, materiales, cuota subsidiada) | $8,000-20,000 MXN/jugador/año | D | Ancla en rango Profeco de costo total de fuerzas básicas ($0-$40,000/año); la beca cubre una fracción |
| Por jugador en formación integral hasta primer equipo (referencia, no partida de este presupuesto) | $7,000,000-10,000,000 MXN | C (cifra heredada de la línea base) | `05-fase3-linea-base-consolidada.md`, Bloque D — se cita solo como orden de magnitud de contraste, no como costo unitario de ninguna partida de este documento |

**Nota de confianza general:** la mayoría de estos costos unitarios son **nivel C** (analogía razonada con ancla de mercado verificable) o **D** (estimación exploratoria sin ancla directa), consistente con la ausencia de estados financieros auditados en todo el sistema (FMF, Liga MX, clubes, academias). Ninguno alcanza nivel A o B porque ninguna institución del sistema publica el costo real de estas actividades.

---

## 10. Fuentes de financiamiento — evaluación de realismo por rubro

### 10.1 Fuentes con realismo alto (financiamiento ya existente, solo requiere redirección)

| Fuente | Rubros que puede cubrir | Evaluación de realismo |
|---|---|---|
| Cuotas de licenciamiento de academias | Academias (A.2) | Alto — mecanismo ya diseñado, autofinanciable; riesgo de "pay to play" si la cuota no se escala por tamaño/ingreso de la academia (mitigado en el propio diseño del Agente 7) |
| FIFA Forward + fondos de formación/tecnología ya asignados a la FMF | Entrenadores (A.3), Tecnología (A.5), puente de arranque de Academias (A.2) | Medio-alto — ya se usó para el CAR (390 mdp); el monto disponible real no es públicamente verificable (bloqueador), por lo que el realismo depende de que la FMF confirme montos, no de que la fuente exista |
| Presupuesto público de infraestructura educativa/deportiva ya existente (CONADE, SEP, municipios) | Infraestructura escolar (A.1, la mayor parte del rubro) | Alto para la función específica de rehabilitación de patios escolares — es presupuesto público ya destinado a educación/deporte, no una carga nueva sobre el sistema del fútbol profesional; realismo bajo si se pretendiera usarlo para gobernanza o competencias del fútbol profesional (fuera de la jurisdicción de CONADE, según la línea base) |
| Fundaciones de clubes (Chivas, América, Pachuca, Tigres, Pachuca) | Comunicación (A.9), Protección/seguimiento familiar (A.11) | Alto — ya financian estas funciones de forma parcial; el costo incremental de escalar es bajo |
| Patrocinios ya comprometidos (Comex, Henkel) | Comunicación (A.9) | Alto para el monto ya comprometido; bajo para cualquier expansión no negociada |

### 10.2 Fuentes con realismo medio (posibles, pero con condición no resuelta)

| Fuente | Rubros | Condición pendiente |
|---|---|---|
| Liga MX / Asamblea de Dueños (decisión regulatoria sin desembolso directo) | Competencias (A.6, ajuste de incentivo premial sin fondo, licenciamiento condicionado) | No requiere gasto directo de la Asamblea, solo su no oposición — pero es el actor de mayor poder de veto documentado; realismo depende de que perciba beneficio competitivo, no solo costo |
| Alianzas público-privadas tipo CAR (empresas + FIFA Forward + FMF) | Infraestructura, mantenimiento del legado 2026 (A.1) | Depende de que se resuelva la falta de desglose público del uso de los 390 mdp ya señalada por el Agente 1 — sin ese precedente de transparencia, una alianza similar arriesga repetir la misma opacidad |
| Gobiernos estatales/municipales (contraparte de uso compartido, transporte) | Infraestructura (A.1), Transporte (A.7) | Capacidad fiscal desigual entre municipios (bloqueador ya señalado por el Agente 9); realista solo si se prioriza por déficit confirmado, no por reparto parejo |
| Concacaf (intercambios, formación regional) | Selecciones (A.8), Entrenadores (A.3) | Montos menores, no cuantificables con la evidencia disponible; realismo bajo-medio, contribución marginal, no estructural |

### 10.3 Fuentes no realistas o no verificables como fuente activa (marcar como aspiracionales)

| Fuente | Por qué no es una fuente en firme |
|---|---|
| Mecanismo de solidaridad FIFA doméstico (5%) | S-10: ni el Agente 3 ni el Agente 4 pudieron confirmar casos reales de cobro. No puede presupuestarse como flujo activo hasta que se verifique que efectivamente se cobra. |
| Derechos audiovisuales de Liga MX (como fuente directa de nuevo ingreso para el proyecto) | PQ-D03: sin cifra pública real de los contratos de TV. Cualquier "minutos de contenido comunitario" (Agente 12, R7) depende de ciclos de renegociación contractual fuera del control del proyecto — es, en el mejor caso, un canal, no un ingreso presupuestable. |
| Universidades (CONDDE/CONADEIP) | Aportan infraestructura y talento en especie (uso compartido de instalaciones), no efectivo nuevo — no debe contarse como fuente monetaria de ningún rubro. |

### 10.4 Rubros sin fuente de financiamiento creíble hoy — **no costeados en firme**

Siguiendo la instrucción explícita de la misión de no inventar una fuente para cuadrar el presupuesto, estos cinco elementos **quedan fuera de los totales de la sección 14** en los tres escenarios, y se marcan como presupuesto contingente, activable solo si su condición de desbloqueo ocurre:

1. **Fondo con bolsa de dinero (allocation money), Agente 6, recomendación 8/16.8** — condicionado explícitamente por su propio diseñador a "transparencia financiera mínima de Liga MX", que no existe. Sin ella, no hay forma de verificar si la Asamblea de Dueños aportaría un monto real o simbólico. **Inviable de costear en firme hoy.**
2. **Fondo de Desarrollo Femenil (Agente 13, R17) y redistribución de % de derechos comerciales/TV hacia Liga MX Femenil (R13)** — misma dependencia no resuelta (transparencia financiera de Liga MX). **Inviable de costear en firme hoy.**
3. **Fútbol adaptado a gran escala (Agente 13, R19)** — condicionado a R18 (verificación de si ya existe estructura vinculada al Comité Paralímpico Mexicano/CONADE), que hoy no tiene respuesta. No existe siquiera línea base de necesidad; cualquier cifra sería inventada. **Inviable de costear en firme hoy — ni el alcance ni la fuente están definidos.**
4. **"Minutos de contenido comunitario" en contratos de TV como fuente de ingreso (Agente 12, R7)** — depende de renegociación contractual futura de los cuatro operadores mediáticos, fuera del control de este proyecto; en el mejor caso es un canal de visibilidad, no un flujo de financiamiento. **No se cuenta como fuente en ningún escenario.**
5. **Uso del 5% de solidaridad FIFA doméstica como fuente activa para becas/redistribución (Agente 7, R16)** — S-10 no confirma que este mecanismo se cobre en la práctica hoy. **No se presupuesta como fuente hasta verificar cobro real.**

**[RECOMENDACIÓN]** Estos cinco elementos deben permanecer en el diseño (Fase 5-6) como recomendaciones válidas y correctamente secuenciadas por sus propios agentes de origen — este agente no recomienda eliminarlos, solo advierte que **presupuestarlos hoy sería una falsa promesa financiera**. Se recomienda al Agente 15 (Implementación) calendarizarlos como "sujetos a activación condicionada", no como parte del cronograma firme de los primeros 4 años.

---

## 11. Análisis de sensibilidad

| Variable | Rubros más expuestos | Efecto estimado | Confianza |
|---|---|---|---|
| **Inflación** (referencia: rango histórico reciente de México, 4-8% anual en distintos años de la última década, sin cifra oficial verificada por este agente) | Todos los rubros de operación recurrente (entrenadores, becas, personal, protección) | Sin ajuste, el presupuesto nominal de régimen estable (año 4-8) podría requerir 15-35% más pesos nominales para mantener el mismo poder adquisitivo, dependiendo de cuántos años transcurran antes de la recalibración (sección 16, recomendación 6) | D |
| **Tipo de cambio (MXN/USD)** | Tecnología (equipos de video/cámaras importados, plataformas comerciales de video), pasto sintético para ampliación/construcción nueva (insumo con componente importado) | Una depreciación del peso de 10-20% frente al dólar encarecería estos dos rubros en proporción similar; los rubros de mano de obra/servicios domésticos (auditoría, becas, honorarios, mantenimiento de obra civil) son mucho menos sensibles | D |
| **Caída de derechos audiovisuales de Liga MX** | Rubros ya marcados como no costeados en firme (sección 10.4) — el diseño de este presupuesto los aisló deliberadamente de esta fuente | Riesgo ya parcialmente mitigado por diseño: como el escenario intermedio (recomendado) no depende de derechos de TV, una caída de estos ingresos no afecta directamente el presupuesto en firme. Sí podría reducir la disposición de clubes/FMF a sostener incluso los rubros de bajo costo ya presupuestados (fundaciones, canales de contenido, A.9) | C |
| **Cambio de gobierno federal (2030) o estatal/municipal (calendarios variables)** | Infraestructura escolar/municipal (A.1, el rubro de mayor magnitud absoluta), mantenimiento del legado 2026 | Riesgo de discontinuidad de convenios y de presupuesto etiquetado plurianual entre administraciones — mismo riesgo ya señalado en el registro de riesgos metodológico (sección 10 del manual) y en el análisis del Agente 9 (mantenimiento del legado 2026) | C |
| **Retrasos de ejecución** (patrón típico de obra pública en México, sin cifra específica verificada aquí) | Construcción nueva de centros regionales (A.1, nivel 5), inventario nacional (A.1, dependencia dura de todo el pilar de infraestructura) | Se recomienda una holgura de cronograma de +30-50% sobre los tiempos ya estimados por el Agente 9 (sección 19 de ese entregable) antes de comprometer el desembolso de construcción nueva | D |
| **Falta de respuesta de FMF/Liga MX a solicitudes de transparencia pendientes desde la Fase 2** | Los cinco rubros de la sección 10.4 en su totalidad; además, la precisión de los costos unitarios de la sección 9 (que dependen de que la FMF confirme el universo real de academias/canchas/licencias) | Es el **riesgo financiero más determinante de todo el proyecto**: mientras persista, el escenario transformador no puede ejecutarse en su totalidad (los rubros de la sección 10.4 seguirían sin fuente), y la precisión de todo el presupuesto —incluido el escenario conservador— permanece en nivel C-D en vez de mejorar a B | Alta probabilidad (histórico documentado de opacidad, S-02/S-06), impacto alto |

**Conclusión del análisis de sensibilidad:** el presupuesto de este documento es más sensible a **variables de gobernanza y transparencia** (respuesta de FMF/Liga MX, cambio de gobierno) que a variables macroeconómicas tradicionales (inflación, tipo de cambio) — un patrón consistente con el hallazgo central de todo el proyecto desde la Fase 4 (el benchmark): la gobernanza y los incentivos, no el monto de inversión, son el factor determinante.

---

## 12. Verificación de los requisitos del Control 6 (Presupuesto)

| Requisito del Control 6 | Estado en este entregable |
|---|---|
| Inversión | Cumplido — sección 14, columna "inversión inicial", y detalle por rubro en el Anexo A |
| Operación | Cumplido — sección 14, columna "recurrente/año" |
| Fuente permanente de financiamiento | Cumplido parcialmente — sección 10.1/10.2 identifica fuentes realistas para la mayoría de los rubros; sección 10.4 declara explícitamente los rubros sin fuente permanente verificable, en vez de asumir una |
| Sensibilidad | Cumplido — sección 11 |
| Sostenibilidad | Cumplido con salvedad — la sostenibilidad del escenario transformador depende de que se resuelva la opacidad financiera (riesgo transversal, sección 11); el escenario conservador e intermedio son sostenibles con las fuentes ya identificadas como realistas |

Este entregable se considera listo para reconciliación con el Agente 15 (Implementación) y para la revisión del Agente 16 (Red Team, Fase 8), con las salvedades explícitas ya declaradas en las secciones 8 (limitaciones) y 10.4 (rubros no costeados).

---

## Preguntas nuevas para el registro maestro

*(No se edita `03-registro-preguntas.md` directamente, para evitar conflictos de edición simultánea con otros agentes. El Agente 0 debe incorporar esta tabla en la integración de Fase 9/10.)*

| ID propuesto | Pregunta | Agente sugerido | Fuente esperada |
|---|---|---|---|
| PQ-F14-01 | ¿Cuál es el costo real (no estimado) de una visita de auditoría técnica a una academia certificada de tamaño mediano en México, con las tres capas (técnica, económica, académica)? | 14 (seguimiento) / despacho auditor | Licitación real del contrato de auditoría fusionado, una vez convocada |
| PQ-F14-02 | ¿Cuál es el monto real y auditado de los fondos FIFA Forward/de formación y tecnología que la FMF administra actualmente, y qué porcentaje ya está comprometido a otros fines? | 14 / FMF (Dirección de Administración y Finanzas) | Estados financieros de la FMF, si se hacen públicos |
| PQ-F14-03 | ¿Cuál es el universo real (auditado, no autorreportado) de canchas de fútbol en México, por tipo (pública, escolar, universitaria, de club)? | 14 / Agente 9 (seguimiento) | Inventario nacional georreferenciado, una vez completado (recomendación 1 del Agente 9) |
| PQ-F14-04 | ¿Qué proporción de municipios tiene capacidad fiscal real para aportar la contraparte de mantenimiento/uso compartido de infraestructura escolar sin depender enteramente de presupuesto federal etiquetado? | 14 / CONADE, SHCP | Datos de finanzas públicas municipales (INEGI, SHCP) |
| PQ-F14-05 | ¿Existe, en algún ejercicio fiscal reciente, un desglose público (aunque sea parcial) de en qué se gastaron los 390 millones de pesos de la renovación del CAR? | 14 / Agente 1 (seguimiento) | Comité Olímpico Mexicano, FMF |
| PQ-F14-06 | ¿Cuál sería el costo real de una beca parcial estandarizada (transporte + materiales) para un jugador de fuerzas básicas, medido mediante un piloto de al menos un ciclo escolar en 3-5 estados de distinto perfil socioeconómico? | 14 (seguimiento) / FMF, academias piloto | Piloto de campo, no estimación de gabinete |
| PQ-F14-07 | ¿Cuánto costaría, en términos reales, mantener actualizado el inventario nacional de canchas después del levantamiento inicial (costo de actualización anual, no solo de creación)? | 14 / Agente 9 (seguimiento) | Operador del inventario, una vez implementado |

---

## Supuestos y riesgos nuevos identificados

### Supuestos nuevos (a incorporar por el Agente 0 en `04-registro-supuestos-riesgos.md`)

| ID propuesto | Supuesto | Justificación | Sensibilidad | Consecuencia si es falso | Validación requerida |
|---|---|---|---|---|---|
| S-F14-01 | El costo de una auditoría técnica de academia en México es comparable, en orden de magnitud, al de una auditoría de cumplimiento de pequeña escala genérica ($8,000-18,000 MXN por visita) | Analogía razonada, sin cifra de mercado de auditoría deportiva específica en México | Media — si el costo real es 2-3x mayor (por ejemplo, si requiere desplazamiento a zonas rurales remotas o equipo técnico especializado más caro), el rubro Academias (A.2) podría duplicarse | Licitación real del contrato de auditoría fusionado (recomendación 5 de este documento) |
| S-F14-02 | El costo de rehabilitación básica de un patio escolar sin instalación deportiva (nivelación + portería + marcaje + malla, sin pasto sintético) es menor al de una cancha de fútbol 7 con pasto sintético completo ($180,000-260,000) | Inferencia razonable por alcance menor de obra, sin cotización directa de este paquete específico (la verificación de mercado de este agente cubrió canchas completas, no el paquete mínimo exacto que propone el Agente 9) | Alta — es el supuesto detrás del rubro de mayor magnitud absoluta de todo el presupuesto (infraestructura escolar); si el costo real es igual o mayor al de una cancha completa, el escenario intermedio podría acercarse al transformador solo en este rubro | Cotización real de 10-20 casos piloto en distintas regiones antes de comprometer el escalamiento a 1,000+ escuelas/año (escenario intermedio) |
| S-F14-03 | Las fundaciones de clubes (Chivas, América, Pachuca, Tigres) tienen capacidad de absorber, sin costo público adicional relevante, el escalamiento de comunicación y seguimiento familiar a los 18 clubes de Liga MX | Extrapolación de 2-4 casos ya verificados a los 18 clubes | Media — si los clubes de menor presupuesto no tienen fundación activa o capacidad equivalente, el rubro de Comunicación (A.9) subestimaría el costo real de escalar a todo el sistema | Encuesta directa a los 18 clubes sobre capacidad y presupuesto de fundación/RSC existente |
| S-F14-04 | El tipo de cambio de referencia usado para comparar este presupuesto contra los ingresos de Liga MX (19 MXN/USD) es representativo del periodo de ejecución de los primeros 4 años | Tipo de cambio aproximado a la fecha de este entregable (julio 2026), sin proyección cambiaria propia | Media — una depreciación sostenida del peso reduciría el porcentaje que este presupuesto representa de los ingresos de Liga MX (medidos en USD), lo cual no cambia el costo real en pesos pero sí la narrativa comparativa de escala | Recalibrar la comparación en cada recalibración presupuestal (sección 16, recomendación 6) con el tipo de cambio vigente en ese momento |

### Riesgos nuevos (a incorporar por el Agente 0 en `04-registro-supuestos-riesgos.md`)

| Riesgo | Probabilidad | Impacto | Señal temprana | Responsable | Mitigación | Contingencia |
|---|---|---|---|---|---|---|
| El presupuesto de este documento se cita en fases posteriores (Fase 8-10) como si fuera una cifra de nivel A/B, perdiendo las etiquetas de confianza C-D con las que fue construido | Media | Alto — erosionaría la credibilidad de todo el proyecto si una cifra estimada se presenta como auditada | Uso de cifras de este documento sin su rango ni su nivel de confianza en comunicados o en el documento ejecutivo final (Agente 17) | Agente 0, Agente 17 | Exigir que cualquier cita de este documento en fases posteriores reproduzca el rango y el nivel de confianza completo, no solo el punto medio | Corrección editorial obligatoria antes de publicación (Control 8) |
| Los cinco rubros no costeados en firme (sección 10.4) se presenten en el documento ejecutivo final (Fase 10) como si ya tuvieran presupuesto resuelto, por presión de mostrar un proyecto "completo" | Media | Alto — repetiría exactamente el error que este documento buscó evitar (inventar una fuente para cuadrar el presupuesto) | Borradores de Fase 9-10 que asignen una cifra fija a estos cinco rubros sin citar su condición de desbloqueo | Agente 16 (Red Team), Agente 17 | El Agente 16 debe verificar explícitamente, en su revisión de Fase 8, que estos cinco rubros sigan marcados como condicionados | Devolver el borrador al Agente 17 si los presenta como presupuesto firme |
| El escenario "conservador" se adopte por defecto no por ser el más responsable dado el nivel de evidencia, sino como excusa para no ejecutar recomendaciones ya baratas y ya listas (certificación de agosto 2026, extensión del SIID) | Media | Medio-Alto | Retraso en la ejecución de recomendaciones que este mismo documento identifica como de bajo costo y alta disponibilidad institucional inmediata | Agente 15, Agente 0 | Este documento recomienda explícitamente el escenario intermedio, no el conservador, como referencia (sección 16, recomendación 1) | Escalar como hallazgo al Agente 16 si el escenario conservador se adopta sin justificación adicional |
| La recalibración presupuestal recomendada para el año 2 (sección 16, recomendación 6) no ocurra, y el proyecto complete su horizonte de 20 años sobre estimaciones de nivel C-D nunca actualizadas con datos reales | Media-Alta | Alto — perpetuaría la misma opacidad financiera que este documento diagnostica como el riesgo transversal más importante | Ausencia de un ejercicio formal de recalibración presupuestal en el informe de avance del año 2 | Agente 0, Agente 15 | Fijar la recalibración del año 2 como un entregable obligatorio, no opcional, del cronograma de implementación (Agente 15) | Escalar al Agente 16/Comité de seguimiento si no ocurre en el plazo fijado |
