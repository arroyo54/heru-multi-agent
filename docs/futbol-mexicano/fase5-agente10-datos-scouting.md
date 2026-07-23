# Fase 5 — Agente 10: Datos y scouting
## Pilar 9 — Arquitectura de datos interoperable del fútbol mexicano

**Fecha de entrega:** 2026-07-23
**Agente:** 10 (Diseño, Fase 5)
**Depende de:** `00-agente0-metodologia-y-plan.md`, `02-plantilla-entregable.md`, `05-fase3-linea-base-consolidada.md`, `06-registro-contradicciones.md`, `07-registro-decisiones.md` (decisión D-01), `fase2-agente1-capacidades-existentes.md` (sección 5.4), `fase2-agente3-derecho-y-regulacion.md` (sección 5.8), `fase5-agente6-formacion-fuerzas-basicas.md`, `fase5-agente7-escuela-universidad-comunidad.md`, `fase5-agente8-entrenadores-ciencia.md`, `fase5-agente9-infraestructura.md`, `08-fase4-benchmark-consolidado.md`, `fase4-agente5b-benchmark-paises-pequenos.md` (Control 2 y Control 3 superados)
**Alcance:** Pilar 9 de la taxonomía (`00`, sección 4) — identificador único de jugador, historial, minutos, posiciones, pruebas físicas, lesiones, escolaridad, video, scouting, protección de datos, analítica, detección de sesgos, indicadores públicos y evaluación de academias, **construido sobre el SIID (Sistema Integral de Información Deportiva) de la FMF, ya reconocido como sistema doméstico de registro por la decisión D-01** — no como plataforma nueva.
**Regla de intervención aplicada:** de las 22 recomendaciones numeradas de la sección 16, 20 (91%) caen en las categorías 1–6 de la jerarquía de intervención (aprovechar, corregir, integrar, escalar, redistribuir, cambiar reglas) y solo 2 (9%) requieren capacidad complementaria nueva, ambas con las 14 preguntas de justificación respondidas en la sección 15 — cumple el mínimo del 70% exigido por la sección 2 del manual metodológico.

---

## 1. Resumen ejecutivo

La instrucción central de esta misión —"no construyas desde cero si puede integrarse lo existente"— se cumple: **el SIID puede y debe extenderse; no se justifica una plataforma nueva de identificador de jugador.** Dos hallazgos nuevos de este entregable (búsqueda web dirigida, 23 de julio de 2026, ver sección 4) cambian el diagnóstico heredado de la Fase 2/3: primero, el SIID ya registra no solo jugadores sino también **personal del cuerpo técnico** (`[HECHO, nivel B]`, fmf.mx), lo que significa que la base para cerrar el vacío de cifras de entrenadores certificados que pidió el Agente 8 (PQ-A05) probablemente ya existe dentro del propio sistema que administra las licencias, y su cierre es un problema de **publicación y vínculo**, no de construcción; segundo, desde el 1 de julio de 2020 **FIFA exige a todas las asociaciones miembro** implementar un sistema electrónico de transferencias/registro domésticas integrado con el **FIFA Connect ID Service** —el identificador único global que ya existe para resolver exactamente el problema que este pilar debía diseñar— de modo que, si el SIID cumple ese mandato (extremo no verificado directamente en este entregable, ver limitaciones), México **ya tiene acceso a la infraestructura de identificador único interoperable global**, y lo que falta no es crearla sino (a) verificar que la integración FMF-FIFA Connect efectivamente opera, (b) extender la obligatoriedad de registro hacia abajo (academias, escuelas, fuerzas básicas no afiliadas) y hacia los lados (CONDDE/CONADEIP), y (c) construir, **encima** de ese identificador ya existente —no en competencia con él—, una capa de datos de rendimiento, salud, escolaridad, video y scouting hoy inexistente. Este entregable diseña esa capa como extensión/integración del SIID, resuelve las tres tareas pendientes explícitas de la misión (cifras de entrenadores del Agente 8, visibilidad de jugadores CONDDE/CONADEIP del Agente 7, protección de datos de menores sin nueva autoridad) y fija un mecanismo obligatorio de detección de sesgos (maduración temprana/efecto de edad relativa, socioeconómico, regional) diseñado para **producir** auditabilidad —no asumirla, dado que casi ninguna cifra de capacidad instalada mexicana es hoy auditable (S-06, línea base).

---

## 2. Objetivo

Diseñar, para el Pilar 9 de la taxonomía del proyecto, la arquitectura de datos interoperable del fútbol mexicano —identificador único de jugador y de personal técnico, historial, minutos, posiciones, pruebas físicas, lesiones, escolaridad, video, scouting, protección de datos, analítica, detección de sesgos, indicadores públicos y evaluación de academias— **partiendo del SIID ya reconocido por la decisión D-01** y evaluando primero si puede extenderse, antes de proponer cualquier sistema nuevo, siguiendo la jerarquía de intervención de la sección 2 del manual metodológico y cerrando explícitamente los tres pendientes que le dejaron los Agentes 6, 7 y 8.

---

## 3. Preguntas del registro maestro abordadas

| ID | Pregunta | Estado tras este entregable |
|---|---|---|
| PQ-P10 | ¿Existe un identificador único de jugador interoperable entre FMF, clubes, escuelas y universidades? | Reformulada con evidencia nueva: existe una base (SIID + mandato FIFA Connect ID) para el circuito afiliado a la FMF (Liga MX–Expansión–Premier–TDP); no existe para academias no afiliadas ni para CONDDE/CONADEIP. Este entregable diseña cómo cerrar ambos tramos por extensión, no por sustitución (secciones 11–13). |
| PQ-A04 (Agente 1/3) | ¿Existe un sistema doméstico de registro/pase de jugadores? | Ya resuelta por D-01 a favor del SIID; este entregable agrega el hallazgo de que también cubre cuerpo técnico y probablemente esté bajo mandato de integración con FIFA Connect ID (sección 4). |
| PQ-A05 (pendiente del Agente 8) | ¿Cuántos entrenadores certificados hay por nivel y dónde? | No se responde con cifra (sigue sin dato público), pero se diseña el mecanismo concreto de cierre: publicar el módulo de personal técnico que el propio SIID ya administra (sección 12, recomendación 4). |
| PQ-A08 (pendiente del Agente 7) | ¿Qué relación formal existe entre CONDDE/CONADEIP y la FMF? | No se resuelve la negociación (eso es gobernanza, Agente 2/7), pero se diseña el esquema técnico de datos que el convenio marco del Agente 7 (R8) necesita para no depender de un sistema nuevo (sección 12, recomendación 7). |
| PQ-C05 (pendiente del Agente 3) | ¿La Secretaría Anticorrupción y Buen Gobierno emitirá lineamientos de datos de menores en el deporte? | Sigue pendiente institucionalmente; este entregable especifica qué debe cubrir ese lineamiento aplicado al esquema de datos aquí diseñado (sección 14). |
| PQ-E2-04 (Agente 5B) | ¿Existe evidencia de fraude de edad/identidad en categorías juveniles mexicanas que un sistema de bio-banding debería anticipar? | No resuelta como dato; se diseña la salvaguarda (verificación de identidad reforzada en el registro, sección 12, recomendación 11) para que cualquier futuro sistema de bio-banding (Agente 6) no se construya sobre datos de edad no confiables. |

Preguntas nuevas generadas por este entregable: ver sección final.

---

## 4. Metodología

**Fuentes usadas:** los documentos de insumo obligatorio listados en el encabezado, más tres búsquedas web dirigidas (23 de julio de 2026) para resolver, específicamente, el mandato explícito de esta misión de evaluar si el SIID puede extenderse antes de proponer algo nuevo: (1) "FIFA Connect ID / FIFA Connect Programme / DTMS", (2) alcance funcional del SIID (¿registra solo jugadores o también cuerpo técnico?), (3) alcance del SIID por liga (Liga MX, Expansión, Premier, TDP). Las tres búsquedas usaron el motor de búsqueda de esta sesión sobre fuentes primarias de FIFA (`inside.fifa.com`, `football-technology.fifa.com`, `support.fifaconnect.org`, `support.id.ma.services`) y documentos oficiales de la FMF (`fmf.mx/docs/reglamentos/`), pero **no se leyó el texto íntegro de ningún PDF de reglamento ni de la documentación técnica de FIFA Connect** — se trabajó sobre los resúmenes generados por la herramienta de búsqueda, no sobre lectura directa línea por línea. Por esto, todos los hallazgos de esta búsqueda se clasifican **nivel B** (fuente primaria identificada y nombrada con precisión, pero no verificada documento-por-documento en esta sesión), consistente con el estándar ya usado por el Agente 8 al citar `formacionacademica.fmf.mx` sin leer el reglamento completo.

**Clasificación de evidencia:** escala A–D de la sección 3.2 del manual metodológico.

**Periodo cubierto:** estado actual (2020–2026) del SIID y del mandato FIFA Connect ID; metas de diseño a 4, 8, 12 y 20 años, según la sección 3.4 del manual metodológico.

---

## 5. Hallazgos

- **[HECHO, nivel B]** El SIID es, conforme a reglamentos de la FMF (`fmf.mx/docs/reglamentos/75.pdf`, `/464.pdf`, `/458.pdf`), el sistema mediante el cual se realiza **el registro de jugadores Y de personal del cuerpo técnico** de los clubes, mediante sesión de usuario autorizado, y se usa para la captura de registros en Liga TDP y Liga Premier además de Liga Expansión y las categorías profesionales. Esto amplía el hallazgo de la línea base (D-01): el SIID no es solo un sistema de transferencias de Liga MX, sino un sistema de registro que ya cruza varias de las categorías competitivas de la pirámide FMF y ya incluye personal técnico, no solo jugadores.
- **[HECHO, nivel B]** Desde el **1 de julio de 2020**, FIFA exige a **todas** las asociaciones miembro implementar un sistema electrónico de transferencias domésticas y de registro (propio, de un tercero, o el FIFA DTMS) **integrado obligatoriamente con el FIFA Connect ID Service y el FIFA Connect Interface**. El FIFA Connect ID es un identificador global único, asignado a cada persona (jugador, entrenador, árbitro, oficial) registrada en cualquier sistema nacional de registro (NRS) integrado, diseñado explícitamente para deduplicar identidades y unificar el registro entre asociaciones.
- **[DATO INCOMPLETO]** No se pudo verificar en esta sesión si la integración FMF–FIFA Connect ID está efectivamente implementada y operando (a diferencia de estar solo mandatada globalmente desde 2020) — es la pregunta más importante y de menor costo de resolver de todo este entregable (ver sección 26 y preguntas nuevas).
- **[HECHO, ya establecido en línea base]** No hay evidencia de que este identificador (SIID/FIFA Connect ID) alcance a las +2,000 academias certificadas/en proceso que no están afiliadas como club de alguna de las cuatro ligas de la pirámide FMF, ni a la red de scouting escolar (28,000+ escuelas), ni a CONDDE/CONADEIP.
- **[HECHO, ya establecido]** El benchmark danés (Agente 5B) advierte explícitamente que adoptar bio-banding o categorías por maduración sin resolver primero la fiabilidad de los datos de edad/identidad del jugador podría reproducir el fraude de edad ya documentado en otros países de América Latina — riesgo señalado como pendiente de validar por este mismo agente (PQ-E2-04).
- **[HECHO]** La nueva LFPDPPP (marzo de 2025) es aplicable a clubes, academias, apps de scouting y a la propia FMF como responsables del tratamiento de datos de menores, pero la Secretaría Anticorrupción y Buen Gobierno (sucesora del INAI) no ha emitido lineamientos sectoriales específicos para datos de menores en el deporte (Agente 3, sección 5.8) — vacío de reglamentación secundaria, no de ley.
- **[HECHO]** Ningún caso del benchmark completo resolvió un problema de datos/identificador construyendo una plataforma nacional nueva y aislada de la federación (`08`, patrón transversal ya usado por los Agentes 6-9); el caso más cercano (Islandia) resuelve identificación de talento por tamaño poblacional, no por sistema de datos, y explícitamente **no es transferible en escala** — México sí necesita una infraestructura de datos que Islandia nunca requirió (Agente 5B, sección 24).
- **[HECHO, ya establecido]** Los tres agentes anteriores de esta fase (6, 7, 8) dejaron condicionada una parte de su propio diseño a este entregable: el Agente 6 supedita el bio-banding a la fiabilidad de los datos de identidad; el Agente 7 supedita el componente de datos de su convenio marco (R8.3) al esquema que aquí se diseñe; el Agente 8 supedita el cierre de PQ-A05 a la integración de su registro de licencias con la arquitectura de este pilar.

---

## 6. Evidencia (cifras y hallazgos citados en este entregable)

| Cifra / hallazgo | Fuente | Fecha del dato | Alcance | Metodología | Limitaciones | Confianza |
|---|---|---|---|---|---|---|
| SIID registra jugadores y personal técnico; usado en captura de registros de Liga TDP, Liga Premier, Expansión y categorías profesionales | Reglamentos FMF (`fmf.mx/docs/reglamentos/75.pdf`, `/464.pdf`, `/458.pdf`), vía búsqueda web de este entregable | 2024-2026 (reglamentos vigentes citados) | Nacional, ligas afiliadas FMF | Resumen de motor de búsqueda sobre documentos oficiales, no lectura línea por línea | No se confirmó si "Liga TDP" incluye la totalidad de sus categorías o solo algunas; no se leyó el texto íntegro del reglamento | B |
| Mandato FIFA de integración de sistemas domésticos de transferencia/registro con FIFA Connect ID Service, vigente desde el 1 de julio de 2020 | FIFA (`inside.fifa.com/transfer-system/clearing-house/systems-integration`, `support.id.ma.services`), vía búsqueda web de este entregable | 2020 (mandato) / 2025-2026 (documentación de soporte vigente) | Global, todas las asociaciones miembro FIFA | Documentación oficial de producto/soporte de FIFA, resumida por motor de búsqueda | No verificado el cumplimiento específico de México; es un mandato global, no una confirmación de implementación mexicana | B |
| FIFA Connect ID: identificador global único por persona (jugador, entrenador, árbitro, oficial), con función de deduplicación entre sistemas nacionales integrados | FIFA (`football-technology.fifa.com/advancing-football/fifa-connect`, `support.fifaconnect.org`), vía búsqueda web de este entregable | 2025-2026 (documentación vigente) | Global | Documentación oficial de producto FIFA | No se verificó el detalle técnico completo (API, campos, gobierno de datos) más allá del resumen | B |
| +2,000 academias certificadas/en proceso (~168,000 niños); 28,000+ escuelas, 1.13M estudiantes en programa de scouting escolar; 11,000+ observados/año, 315 invitaciones, 97 convocatorias (2025) | FMF, vía Agente 1 y Agente 6 | 2025-2026 | Nacional | Declaración institucional, autorreportada | Sin desagregación territorial, de género, socioeconómica ni por trimestre de nacimiento — el vacío exacto que este entregable busca cerrar | B |
| Nueva LFPDPPP y Secretaría Anticorrupción y Buen Gobierno como autoridad sucesora del INAI | Línea base (`05`, Bloque C), Agente 3 | Marzo-noviembre 2025 | Nacional | Publicación oficial (DOF), vía Agente 3 | Sin lineamientos sectoriales de datos de menores en el deporte aún emitidos | A (existencia de la ley) / B (aplicabilidad al deporte, inferencia del Agente 3) |
| Efecto de edad relativa (RAE) y bio-banding como intervención danesa de una década, con reconocimiento de que el problema persiste pese a tres frentes de intervención | Agente 5B, vía FIFA Training Centre y literatura académica citada | 2026 (reporte) / ~10 años de intervención previa | Nacional (Dinamarca) | Descripción institucional y académica | Sin cifra de efectividad aislada del componente de datos/identidad | B |
| Riesgo de fraude de edad/identidad en categorías juveniles de América Latina si se adopta bio-banding sin resolver fiabilidad de datos | Agente 5B (hipótesis, no verificada para México) | 2026 | Regional (América Latina, general) | Inferencia razonable del propio Agente 5B, no dato mexicano directo | No hay caso mexicano documentado de fraude de edad en esta cadena de entregables; se trata como riesgo a validar, no como hecho | C |

---

## 7. Fuentes

- `00-agente0-metodologia-y-plan.md`, `02-plantilla-entregable.md`, `05-fase3-linea-base-consolidada.md`, `06-registro-contradicciones.md`, `07-registro-decisiones.md`, `fase2-agente1-capacidades-existentes.md`, `fase2-agente3-derecho-y-regulacion.md`, `fase5-agente6-formacion-fuerzas-basicas.md`, `fase5-agente7-escuela-universidad-comunidad.md`, `fase5-agente8-entrenadores-ciencia.md`, `fase5-agente9-infraestructura.md`, `08-fase4-benchmark-consolidado.md`, `fase4-agente5b-benchmark-paises-pequenos.md` — documentos internos del proyecto, con su propia cadena de fuentes primarias/secundarias ya citada.
- Búsqueda web (23 de julio de 2026): "FIFA Connect ID FIFA Connect platform player unique identifier registration federations" — `inside.fifa.com`, `football-technology.fifa.com`, `support.fifaconnect.org`, `support.id.ma.services`.
- Búsqueda web (23 de julio de 2026): "FMF SIID Sistema Integral de Información Deportiva jugadores registro" — `fmf.mx/docs/reglamentos/75.pdf`, `/464.pdf`.
- Búsqueda web (23 de julio de 2026): "SIID FMF Liga Expansión Liga Premier Liga TDP fuerzas básicas registro sistema" — `fmf.mx/docs/reglamentos/458.pdf`, `intranet.ligapremier-fmf.mx`.
- Búsqueda web (23 de julio de 2026): "FIFA Connect ID Mexico FMF DTMS domestic transfer matching system" — `inside.fifa.com`, `support.fifaconnect.org`, sin resultado específico de la implementación mexicana (vacío declarado en limitaciones).

---

## 8. Limitaciones

- La limitación más importante de este entregable: **no se verificó, con lectura directa de fuente primaria, si la FMF efectivamente integró el SIID con el FIFA Connect ID Service** — se confirmó el mandato global de FIFA (2020) y la existencia funcional del SIID como sistema de registro doméstico (ya reconocida por D-01), pero no la integración efectiva entre ambos. Toda la arquitectura de este entregable depende de esa confirmación (ver dependencia 1, sección 20, y pregunta nueva PQ-10-01).
- No se leyó el texto íntegro de ningún reglamento de la FMF citado (`75.pdf`, `464.pdf`, `458.pdf`) ni de la documentación técnica completa de FIFA Connect — se trabajó sobre resúmenes generados por la herramienta de búsqueda de esta sesión, consistente con la limitación ya declarada por otros agentes de Fase 5 al citar el mismo dominio.
- No se pudo confirmar si "Liga TDP" en los reglamentos citados incluye la totalidad de sus categorías/divisiones o solo un subconjunto, ni si las academias certificadas no afiliadas a un club de estas cuatro ligas tienen algún vínculo, aunque sea parcial, con el SIID.
- No se investigó en esta sesión qué proveedores de software de scouting/analítica (tipo Wyscout, InStat, Hudl u homólogos) usan hoy los clubes de Liga MX/Expansión de forma comercial — es una hipótesis razonable (práctica estándar en el fútbol profesional mundial) pero no verificada para México; se marca explícitamente como `[HIPÓTESIS]` en la sección 12 y no se usa como base de ninguna cifra.
- No se investigó el costo real de desarrollo/operación de una capa de interoperabilidad de datos sobre el SIID — los órdenes de magnitud de la sección 18 son estimaciones preliminares (confianza C-D), a afinar por el Agente 14 en Fase 7.
- La escala real de CONDDE/CONADEIP (número de jugadores universitarios federados) no fue investigada de nuevo en este entregable — se reutiliza la cifra de nivel C ya declarada por el Agente 7 (edición 2021 de CONDDE, sin confirmar para 2025-2026), con la misma advertencia de no usarla para dimensionar presupuesto.
- El benchmark internacional de esta fase (Fase 4) no incluyó ningún caso de país con un sistema de datos/scouting nacional documentado en profundidad comparable al que aquí se diseña (el hallazgo más cercano, islandés, es explícitamente "no transferible en escala" para este componente) — este entregable se apoya más en la arquitectura ya existente de FIFA/SIID que en un caso de país replicable, a diferencia de los Agentes 6-9.

---

## 9. Activos existentes

- El SIID (Sistema Integral de Información Deportiva) de la FMF, ya reconocido por la decisión D-01 como sistema doméstico de registro, que además —hallazgo nuevo de este entregable— ya registra personal del cuerpo técnico y ya se usa en el registro de Liga TDP, Liga Premier y Liga Expansión, no solo Liga MX.
- El FIFA Connect ID Service y el FIFA Connect Interface, infraestructura global ya construida y operada por FIFA, de uso obligatorio para toda asociación miembro desde 2020 — un identificador único interoperable que México no necesita construir, solo confirmar que usa correctamente.
- El registro interno de licencias de entrenadores que la FMF ya debe administrar para emitir y renovar licencias (activo ya señalado por el Agente 8, supuesto S-15), potencialmente ya integrado al mismo SIID dado que este registra personal técnico.
- La regla de minutos de menores de Liga MX, que ya exige un seguimiento de minutos jugados por jugador y categoría (aunque su cifra exacta esté suspendida por D-02) — expediente de origen que puede alimentar el historial de minutos sin construir un sistema de conteo nuevo.
- El sistema de scouting nacional de la FMF (11,000+ observados/año, 315 invitaciones, 97 convocatorias en 2025) y la red de scouting escolar (28,000+ escuelas, 1.13M estudiantes) — canales de captura de datos de talento ya operando.
- El CAR del Comité Olímpico Mexicano (renovado con 390 millones de pesos) y el CNAR de CONADE (562 camas), ya identificados por el Agente 9 como infraestructura física reutilizable para pruebas físicas/biométricas estandarizadas, sin construir laboratorios nuevos.
- La Ley Federal del Trabajo (registro laboral obligatorio de contratos de menores deportistas) y la Ley General de NNA/SIPINNA, ya identificadas por el Agente 3 como marco de protección de menores aplicable sin ley nueva.
- La nueva LFPDPPP (2025) y la Secretaría Anticorrupción y Buen Gobierno, ya identificadas por el Agente 3 como autoridad de datos personales con facultad —no ejercida aún— de emitir lineamientos sectoriales, evitando la necesidad de una autoridad de datos deportiva aparte.
- El índice de marginación de CONEVAL y los datos de INEGI/SEP que el Agente 9 ya propone usar para el inventario nacional de canchas — misma lógica de "dato público ya existente" aplicable aquí para el indicador de sesgo socioeconómico (sección 12, recomendación 16).
- CONDDE y CONADEIP, con sus propios sistemas de registro de jugadores universitarios (no documentados en detalle, pero existentes como circuitos organizados), y el mecanismo de convenio marco ya diseñado por el Agente 7 (R8) como puente institucional.

---

## 10. Problemas

1. No se ha verificado si la integración FMF-FIFA Connect ID, mandatada globalmente desde 2020, efectivamente opera en México — es un vacío de verificación, no necesariamente de capacidad.
2. El alcance confirmado del SIID (Liga MX-Expansión-Premier-TDP) no llega a las academias certificadas no afiliadas a un club de esas cuatro ligas, a las escuelas del programa de scouting, ni a fuerzas básicas informales/ligas municipales — el identificador único, si existe, tiene un techo de cobertura muy por debajo de la base de la pirámide.
3. CONDDE y CONADEIP operan, según la línea base y el Agente 7, como circuitos aparentemente paralelos sin vínculo documentado con la FMF — el talento universitario es invisible para el scouting profesional y viceversa (PQ-A08).
4. No existe evidencia de que el SIID capture datos más allá del registro administrativo/transferencias: no hay evidencia de un módulo de pruebas físicas, lesiones, escolaridad o video vinculado al mismo identificador.
5. No existe evidencia de un mecanismo de detección de sesgos (maduración temprana/efecto de edad relativa, socioeconómico, regional) en el propio sistema de scouting de la FMF — hoy no se publica ninguna cifra desagregada de los 11,000+ observados/315 invitados/97 convocados por trimestre de nacimiento, origen socioeconómico o estado.
6. No existe evidencia de un protocolo de verificación reforzada de identidad/edad al registrar jugadores, lo que —según la advertencia del Agente 5B— haría riesgosa cualquier futura reforma de bio-banding (Agente 6) sin resolver esto primero.
7. La nueva LFPDPPP (2025) es aplicable pero no tiene lineamientos sectoriales de datos de menores en el deporte, y no hay evidencia de un esquema de consentimiento diferenciado (padre/tutor) ni de minimización de datos en el ecosistema de scouting/academias.
8. Casi ninguna cifra institucional citada en este documento (academias, escuelas, observados, convocados) es hoy auditable de forma independiente (S-06, línea base) — cualquier indicador que este pilar diseñe corre el riesgo de heredar el mismo problema si no se construye con auditoría externa desde el diseño.
9. No hay evidencia de un estándar reconocido de "evaluación de academias" basado en datos objetivos (egreso a primer equipo, minutos, lesiones, deserción escolar) — la certificación de academias (PQ-A07, Agente 8) es hoy un proceso sin componente de datos de resultado.

---

## 11. Alternativa de mejora

Reformar (no sustituir) el SIID en cuatro puntos concretos, todos ejecutables por la propia FMF sin nueva ley ni nueva institución: (a) verificar y, si falta, completar la integración con el FIFA Connect ID Service que FIFA ya exige desde 2020 —trámite de cumplimiento normativo, no de construcción de plataforma—; (b) publicar (transparencia, no proyecto de datos nuevo) el alcance real del SIID por liga/categoría y el número de personal técnico ya registrado en él, cerrando de forma directa el vacío que el Agente 8 dejó pendiente (PQ-A05); (c) extender la obligatoriedad de alta en el SIID (o en un módulo ligero del mismo sistema) hacia abajo, hasta el primer registro en una academia certificada de la FMF, no solo hasta el primer registro profesional o de transferencia; (d) incorporar, dentro del mismo flujo de alta del SIID, un campo de fecha de nacimiento completa y verificación de identidad reforzada (CURP y, donde exista, biometría ligera ya usada por otros trámites gubernamentales), condición necesaria para cualquier futuro sistema de bio-banding del Agente 6 y para la detección de sesgo de edad relativa de este mismo pilar.

## 12. Alternativa de integración

- **R1 — Auditoría de cumplimiento FIFA Connect ID.** Verificar formalmente con la FMF si el SIID está integrado con el FIFA Connect ID Service (mandato FIFA vigente desde 2020); si ya lo está, el "identificador único interoperable" que pedía PQ-P10 existe en la capa global y solo falta extender su alcance doméstico (recomendaciones siguientes); si no lo está, exigir el cumplimiento de una obligación ya existente, no construir un identificador nuevo.
- **R2 — Publicación del alcance real del SIID.** Publicar, por liga y categoría, qué está y qué no está cubierto hoy por el SIID (Liga MX, Expansión, Premier, TDP, académicas no afiliadas), cerrando la incertidumbre residual que dejó abierta el registro de contradicciones (`06`).
- **R3 — Extensión de la obligatoriedad de registro hacia la base de la pirámide.** Exigir alta (aunque sea en un módulo ligero, de menor exigencia documental que el registro profesional) en el mismo sistema para todo jugador de una academia con sello de "academia certificada de la FMF" (el mismo sello que el Agente 8 propone condicionar a licencia mínima del cuerpo técnico) — un solo trámite de certificación, dos criterios (licencia del cuerpo técnico + alta del jugador en el sistema).
- **R4 — Cierre del vacío de cifras de entrenadores certificados (pedido explícito del Agente 8).** Vincular el módulo de personal técnico que el SIID ya administra (hallazgo de la sección 5) con el registro de licencias D-C-B-A-PRO de Formación Académica/ENDIT, y publicar el cruce (persona + nivel de licencia + club/academia + estado) como reporte anual. Esto resuelve PQ-A05 sin construir un sistema de conteo nuevo: **es el mismo sistema que ya registra al cuerpo técnico, con un campo adicional (nivel de licencia) ya administrado en otra dirección de la misma federación.**
- **R5 — Esquema común de datos para el convenio marco FMF-CONDDE-CONADEIP-SEP (cierre del pedido del Agente 7, componente 3 de su R8).** Definir un "perfil ligero de jugador universitario visible" dentro del mismo espacio de identificador (idealmente el propio FIFA Connect ID, si R1 confirma su uso), poblado mediante un feed periódico de datos desde los sistemas de registro que ya operan CONDDE/CONADEIP (roster de elegibilidad de cada torneo), sin exigirles migrar a una plataforma FMF. La visibilidad se resuelve con un **indicador booleano de "elegible para observación profesional"** vinculado al calendario de scouting reconocido en R19 del Agente 7, no con una base de datos paralela.
- **R6 — Historial de minutos y posiciones.** Vincular el registro de minutos que ya exige la regla de menores de Liga MX (cifra suspendida por D-02, pero el mecanismo de conteo por partido ya debe existir para aplicar sanciones) al mismo expediente de jugador — un solo dato, dos usos (cumplimiento de la regla + historial de carrera), en vez de que Fase 5 diseñe un sistema de conteo de minutos aparte.
- **R7 — Pruebas físicas y biométricas.** Usar el CAR-COM y el CNAR-CONADE, ya renovados (Agente 9), como sede estandarizada de bateria de pruebas físicas para las convocatorias de selecciones y para academias certificadas de alto rendimiento, con protocolo común y resultado vinculado al identificador único — en vez de que cada club/academia desarrolle su propio estándar no comparable.
- **R8 — Lesiones.** Integrar el registro de lesiones al padrón médico que la Ley Federal del Trabajo ya exige para contratos de menores deportistas (Agente 3, sección 5.5) y al convenio de actividades deportivas 14-16 años, en vez de crear un registro médico deportivo nacional aparte; el campo de lesión se agrega al mismo expediente por jugador.
- **R9 — Escolaridad.** Vincular el "Sello de Compatibilidad Académica y Deportiva" que ya diseñó el Agente 7 (R21) —seguimiento de rendimiento escolar del jugador— al mismo identificador único, para que el historial deportivo y el escolar compartan una sola llave, no dos sistemas separados de SEP y FMF.
- **R10 — Video y scouting digital.** `[HIPÓTESIS, no verificada en esta sesión]` Si los clubes de Liga MX/Expansión ya usan plataformas comerciales de análisis de video (práctica estándar en el fútbol profesional mundial, no confirmada específicamente para México en este entregable), reconocer esas plataformas como fuente válida de scouting para categorías inferiores y academias certificadas, en vez de que la FMF construya una plataforma de video nacional propia; condicionar el reconocimiento a que el video quede etiquetado con el identificador único del jugador observado.
- **R11 — Verificación de identidad/edad reforzada.** Incorporar CURP y, donde ya exista infraestructura, verificación biométrica ligera al momento del alta en el SIID/módulo extendido, respondiendo directamente a la advertencia del Agente 5B (riesgo de fraude de edad en bio-banding) — aprovechando infraestructura de identidad ya usada por otros trámites del Estado mexicano, no creando un sistema biométrico deportivo aparte.
- **R12 — Escalamiento del scouting con registro completo (no solo convocados).** Registrar, con el mismo identificador, a los 11,000+ observados/año, no solo a los 315 invitados y 97 convocados — condición necesaria para poder medir sesgo (si solo se registra a quien ya fue convocado, no hay universo de comparación).
- **R13 — Auditoría externa anual de datos y scouting.** Extender el mandato del auditor externo ya propuesto por el Agente 8 (recomendación 20 de ese entregable) para que también verifique la calidad, cobertura territorial y ausencia de sesgo de los datos de este pilar, en vez de crear un segundo mecanismo de auditoría paralelo.
- **R14 — Evaluación de academias con datos objetivos.** Incorporar al proceso de certificación/recertificación de "academia certificada" (ya operado por la FMF, PQ-A07) indicadores objetivos extraídos del propio sistema: tasa de egreso a fuerzas básicas de clubes, minutos promedio, tasa de lesión, tasa de continuidad escolar — reemplazando gradualmente la autocertificación por evaluación basada en datos ya capturados por este mismo pilar.
- **R15 — Convenio FMF-SIPINNA para datos de menores.** Usar el convenio FMF-SIPINNA/Procuradurías de Protección de NNA ya propuesto por el Agente 3 (sección 14 de ese entregable) como canal de denuncia también para uso indebido de datos personales de menores en scouting/academias, en vez de crear una autoridad de integridad de datos deportiva aparte.
- **R16 — Indicador de sesgo socioeconómico.** Cruzar, de forma agregada y anonimizada (sin almacenar domicilio exacto como campo obligatorio del expediente individual, por minimización de datos bajo LFPDPPP), el municipio de origen del jugador observado/convocado con el índice de marginación de CONEVAL —dato público ya existente— para producir un indicador anual de sesgo socioeconómico en la captación.
- **R17 — Indicador de sesgo regional.** Cruzar la densidad de observaciones de scouting/invitaciones por estado con la población de jugadores registrados por estado (usando el mismo inventario territorial que construirá el Agente 9 para infraestructura), para detectar "desiertos de scouting" — estados con alta población de jugadores registrados y baja tasa de observación.
- **R18 — Indicador de efecto de edad relativa (RAE).** Publicar anualmente la distribución por trimestre de nacimiento de jugadores convocados frente a la distribución de la población general de jugadores registrados en el sistema, replicando la métrica que la propia DBU danesa usa para diagnosticar el problema (Agente 5B) — condición de diseño explícita: este indicador solo es posible si R11 (verificación de identidad/edad) está implementado.
- **R19 — Lineamientos sectoriales de datos de menores en el deporte.** Reiterar y operacionalizar, específicamente para el esquema de datos de este pilar, la solicitud ya hecha por el Agente 3 (recomendación 5 de ese entregable) a la Secretaría Anticorrupción y Buen Gobierno, especificando qué debe cubrir el lineamiento: consentimiento parental diferenciado, minimización de datos biométricos/de rendimiento de menores, plazos de retención, y prohibición expresa de venta/transferencia de datos de menores a terceros comerciales (agencias, plataformas de video) sin autorización expresa.
- **R20 — Roles y niveles de acceso.** Diseñar el esquema de acceso del identificador único extendido con al menos tres niveles: (i) dato agregado/anonimizado, de acceso público (indicadores de las recomendaciones 16-18); (ii) dato individual no sensible (historial deportivo, minutos, posiciones), de acceso restringido a club/academia/FMF/selección correspondiente; (iii) dato sensible de menores (biométrico, médico, socioeconómico identificable), de acceso restringido con consentimiento parental expreso y trazabilidad de quién lo consulta — misma arquitectura de niveles que cualquier sistema de datos personales bien diseñado bajo la LFPDPPP, sin requerir una ley deportiva de datos aparte.

## 13. Alternativa de escalamiento

Recomendaciones concretas (numeradas para trazabilidad con la sección 16), clasificadas explícitamente por categoría de la jerarquía de intervención (sección 2 del manual metodológico):

| # | Recomendación | Categoría de intervención |
|---|---|---|
| 1 | Auditar/confirmar la integración SIID–FIFA Connect ID ya mandatada por FIFA desde 2020 | 1. Aprovechar |
| 2 | Publicar el alcance real del SIID por liga/categoría | 1. Aprovechar |
| 3 | Extender la obligatoriedad de registro hasta la primera afiliación a academia certificada | 6. Cambiar reglas |
| 4 | Vincular y publicar el módulo de personal técnico del SIID con el registro de licencias (cierra PQ-A05, pedido del Agente 8) | 3. Integrar |
| 5 | Esquema común de datos para el convenio marco FMF-CONDDE-CONADEIP (cierra el pedido del Agente 7) | 3. Integrar |
| 6 | Vincular el conteo de minutos de la regla de menores al expediente único | 3. Integrar |
| 7 | Usar CAR-COM/CNAR-CONADE como sede estandarizada de pruebas físicas | 1. Aprovechar / 3. Integrar |
| 8 | Integrar el registro de lesiones al padrón médico laboral ya exigido por la LFT | 3. Integrar |
| 9 | Vincular el Sello de Compatibilidad Académica del Agente 7 al identificador único | 3. Integrar |
| 10 | Reconocer plataformas comerciales de video ya usadas por clubes, etiquetadas con el identificador único | 1. Aprovechar |
| 11 | Verificación de identidad/edad reforzada (CURP + biometría ligera ya existente en el Estado) | 2. Corregir / 6. Cambiar reglas |
| 12 | Registrar a todos los observados (11,000+), no solo a convocados | 4. Escalar |
| 13 | Extender el mandato del auditor externo del Agente 8 a datos/scouting | 3. Integrar |
| 14 | Evaluación de academias con indicadores objetivos de datos, no solo autocertificación | 2. Corregir |
| 15 | Usar el convenio FMF-SIPINNA (ya propuesto por el Agente 3) como canal de denuncia de mal uso de datos de menores | 3. Integrar |
| 16 | Indicador de sesgo socioeconómico (municipio × índice de marginación CONEVAL) | 1. Aprovechar |
| 17 | Indicador de sesgo regional (densidad de scouting × población registrada por estado) | 3. Integrar |
| 18 | Indicador de efecto de edad relativa (RAE), publicado anualmente | 6. Cambiar reglas |
| 19 | Lineamientos sectoriales de datos de menores, operacionalizados para este esquema | 3. Integrar |
| 20 | Esquema de acceso por niveles (público/restringido/sensible-menores) | 6. Cambiar reglas |
| 21 | **Programa de Analistas de Datos Regionales** | 7. Crear complementario — requiere 14 preguntas (sección 15) |
| 22 | **Línea presupuestal etiquetada de equipamiento de captura de datos/video para escuelas y academias de bajos recursos** | 7. Crear complementario — requiere 14 preguntas (sección 15) |

**Verificación de la regla del 70%:** de las 22 recomendaciones, 20 (91%) caen en las categorías 1 a 6; únicamente las recomendaciones 21 y 22 (9%) requieren capacidad complementaria nueva, y ambas responden las 14 preguntas de justificación en la sección 15.

## 14. Alternativa de sustitución

**No se identifica ningún activo existente que deba sustituirse por completo.** El SIID se conserva como sistema de registro; el FIFA Connect ID se aprovecha, no se compite con él; el sistema de scouting nacional, la red de scouting escolar y las academias certificadas se conservan y se extienden. La única "sustitución" de este entregable es de **método de evaluación de academias** (de autocertificación pura a evaluación con datos objetivos, recomendación 14) y de **método de verificación de identidad** (de registro sin verificación reforzada a registro con CURP/biometría, recomendación 11) — ambos son correcciones de proceso dentro del mismo sistema, no reemplazo de una institución por otra. Esto es consistente con la conclusión central de este entregable: **el SIID no se sustituye, se extiende.**

## 15. Necesidad de nueva capacidad

### 15.0 Prueba de las 14 preguntas aplicada a la pregunta central de la misión: ¿se justifica una plataforma nueva de identificador único de jugador en lugar de extender el SIID?

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Qué capacidad existe hoy que cubre esta función? | El SIID (registro doméstico de jugadores y personal técnico, ya reconocido por D-01, y ya usado en Liga MX-Expansión-Premier-TDP), más el FIFA Connect ID Service (identificador global único, de uso obligatorio para toda asociación miembro desde 2020). |
| 2 | ¿Quién la controla hoy? | El SIID: la FMF. El FIFA Connect ID: FIFA, vía integración obligatoria de cada asociación miembro con su sistema nacional. |
| 3 | ¿Por qué no cumple su función? | No es que no cumpla su función de identificador — es que su alcance verificado no llega a academias no afiliadas, escuelas de scouting ni a CONDDE/CONADEIP, y no se confirmó si ya está técnicamente integrado con el identificador global de FIFA. |
| 4 | ¿Por qué no puede reformarse en lugar de sustituirse? | Sí puede y debe reformarse: no hay ninguna razón técnica identificada en esta investigación por la que el SIID no pueda extender su obligatoriedad de registro hacia abajo (academias) y hacia los lados (convenio de datos con CONDDE/CONADEIP), ni por la que la integración con FIFA Connect ID (si falta) no pueda completarse como cumplimiento normativo. |
| 5 | ¿Cuánto costaría reformar/extender? | Bajo, en el componente normativo/de alcance (recomendaciones 1-6, sección 12): son extensiones de reglas y publicación de datos ya administrados. Medio en el componente de nueva capa de datos (pruebas físicas, lesiones, video, indicadores de sesgo): requiere desarrollo de módulos e interfaces, no de un sistema de identidad nuevo (ver sección 18). |
| 6 | ¿Cuánto costaría crear un sistema de identificador nuevo? | Alto, y redundante: duplicaría exactamente la función que el FIFA Connect ID ya resuelve a nivel global y que el SIID ya resuelve a nivel doméstico para buena parte de la pirámide; además generaría el riesgo de que clubes/academias deban mantener dos identidades por jugador, aumentando —no reduciendo— el riesgo de fraude de identidad que advierte el Agente 5B. |
| 7 | ¿Qué funciones asumiría la nueva estructura (si se creara)? | Ninguna que el SIID extendido no pueda asumir; no se identifica una función de identificador que requiera una entidad de gobierno distinta a la FMF. |
| 8 | ¿Qué institución dejaría de cumplir esas funciones? | No aplica — no se propone sustituir a la FMF como administradora del identificador. |
| 9 | ¿Cómo se evitaría la duplicidad? | Precisamente al no crear un sistema nuevo: todo el diseño de la sección 12 se construye como módulos/campos adicionales sobre el mismo identificador (SIID/FIFA Connect ID), con una sola llave por persona. |
| 10 | ¿Cómo se financiaría de forma permanente? | No aplica a un sistema nuevo, porque no se propone uno; el desarrollo de los módulos de extensión se costea en la sección 18 con fondos ya existentes de formación/tecnología de la FMF. |
| 11 | ¿Cómo se evaluaría? | No aplica a un sistema nuevo; los indicadores de evaluación de la extensión están en la sección 23. |
| 12 | ¿Quién la supervisaría? | No aplica a un sistema nuevo; la supervisión de la extensión recae en la FMF con el auditor externo extendido (recomendación 13). |
| 13 | ¿Bajo qué condiciones podría cerrarse? | No aplica a un sistema nuevo. |
| 14 | ¿Qué riesgo tiene de ser capturada por intereses particulares? | El riesgo real no es de una institución nueva (no se crea ninguna), sino de que la extensión del SIID se implemente sin auditoría externa ni transparencia, replicando el patrón de opacidad ya documentado en la línea base (Bloque B/D) — mitigado por las recomendaciones 2, 13 y 20. |

**Conclusión de la prueba:** el SIID, extendido y auditado, cumple la función que pedía PQ-P10. No se justifica una plataforma nueva de identificador único de jugador. Las dos únicas capacidades nuevas de este entregable (recomendaciones 21 y 22) no son sistemas de identificador ni de registro — son un programa de personal y una línea presupuestal de equipamiento, tratadas a continuación con el mismo estándar de 14 preguntas que exige la sección 2.1 del manual para cualquier capacidad nueva.

### 15.1 Programa de Analistas de Datos Regionales

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Qué capacidad existe hoy que cubre esta función? | Ninguna identificada: no hay evidencia de personal dedicado a verificar calidad y cobertura de datos por región dentro de la FMF o de las asociaciones estatales. |
| 2 | ¿Quién la controla hoy? | Nadie de forma explícita — la calidad de los datos regionales depende hoy de la buena fe de cada academia/asociación estatal al reportar. |
| 3 | ¿Por qué no cumple su función? | Porque no existe. |
| 4 | ¿Por qué no puede reformarse en lugar de crearse? | No hay nada que reformar porque no hay antecedente; se trata como capacidad complementaria mínima (personal, no institución), siguiendo el mismo patrón que el Agente 8 usó para sus "entrenadores mentores" (Dinamarca, "Talent Coaches") — un cuerpo reducido vinculado a la estructura ya existente (33 asociaciones estatales), no una entidad nueva. |
| 5 | ¿Cuánto costaría la alternativa de no tener este programa? | Los indicadores de sesgo regional/socioeconómico (recomendaciones 16-17) dependerían de datos autorreportados sin verificación de campo, replicando el problema de auditabilidad ya documentado (S-06). |
| 6 | ¿Cuánto costaría el programa? | Orden de magnitud en sección 18 (confianza C-D). |
| 7 | ¿Qué funciones asumiría? | Verificar en campo, por muestreo, la calidad de los datos cargados al sistema extendido por región (no recolectar datos nuevos de forma paralela); apoyar a asociaciones estatales de menor capacidad técnica a completar su registro. |
| 8 | ¿Qué institución dejaría de cumplir esas funciones? | Ninguna — hoy nadie las cumple. |
| 9 | ¿Cómo se evitaría la duplicidad? | Reportan a la misma Dirección de Formación Académica/sistemas de la FMF que administra el SIID extendido; no crean un registro paralelo. |
| 10 | ¿Cómo se financiaría de forma permanente? | Redirección de fondos FIFA Forward/FMF ya destinados a formación y digitalización (mismo mecanismo ya usado por el Agente 8 para sus becas y mentores). |
| 11 | ¿Cómo se evaluaría? | Cobertura de verificación de campo por estado/año; tasa de corrección de inconsistencias detectadas. |
| 12 | ¿Quién la supervisaría? | FMF, con el auditor externo extendido (recomendación 13). |
| 13 | ¿Bajo qué condiciones podría cerrarse? | Si la auditoría externa confirma, por 3 ciclos consecutivos, que los datos autorreportados son confiables sin verificación de campo. |
| 14 | ¿Qué riesgo tiene de ser capturada por intereses particulares? | Riesgo medio: que los analistas regionales sean usados para favorecer a academias/asociaciones afines en vez de auditar de forma neutral. Mitigación: designación y evaluación centralizada por la FMF, no por autoridades estatales/municipales, más el mismo auditor externo de la recomendación 13. |

### 15.2 Línea presupuestal etiquetada de equipamiento de captura de datos/video para escuelas y academias de bajos recursos

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Qué capacidad existe hoy que cubre esta función? | Ninguna identificada específicamente para esto; el presupuesto de Formación Académica/FIFA Forward existe (ya usado para el CAR), pero no hay evidencia de una línea etiquetada para equipamiento de captura de datos en zonas de bajos recursos. |
| 2 | ¿Quién la controla hoy? | La FMF (presupuesto de formación/tecnología) y, en su componente FIFA Forward, FIFA junto con la FMF. |
| 3 | ¿Por qué no cumple su función? | Porque no existe una reserva explícita para este propósito — sin ella, la digitalización del scouting (recomendaciones 10, 12) se concentraría en clubes y academias de zonas urbanas con recursos propios, reproduciendo el sesgo regional/socioeconómico que este mismo pilar busca medir y corregir. |
| 4 | ¿Por qué no puede reformarse en lugar de crearse? | Se diseña deliberadamente, igual que la "Beca Nacional" del Agente 8, como una **reasignación etiquetada** dentro del presupuesto ya existente, no como un fideicomiso o entidad nueva — se trata en esta sección por la misma precaución metodológica que usó el Agente 8, no porque sea una institución. |
| 5 | ¿Cuánto costaría reformar el presupuesto existente para etiquetar esta línea? | Bajo — decisión administrativa de reasignación (misma lógica que Agente 8, sección 15.2 de ese entregable). |
| 6 | ¿Cuánto costaría crear un vehículo financiero nuevo aparte? | No se recomienda — mismo riesgo de captura ya advertido por el Agente 8 (caso Mamić, Croacia) si se crea gobernanza propia innecesaria. |
| 7 | ¿Qué funciones asumiría? | Subsidiar cámaras básicas, conectividad mínima y capacitación de captura de datos para academias/escuelas de scouting en municipios de menor recurso, identificados por el propio indicador de sesgo regional (recomendación 17). |
| 8 | ¿Qué institución dejaría de cumplir esas funciones? | Ninguna — hoy nadie subsidia este rubro específico. |
| 9 | ¿Cómo se evitaría la duplicidad? | Administrada por la misma Dirección de Formación Académica/sistemas que gestiona el SIID extendido y coordinada con la Beca Nacional del Agente 8 (mismo mecanismo administrativo, rubro distinto). |
| 10 | ¿Cómo se financiaría de forma permanente? | Porcentaje fijo y públicamente reportado de fondos FIFA Forward/FMF de formación/tecnología ya existentes. |
| 11 | ¿Cómo se evaluaría? | Número de academias/escuelas equipadas por año y por estado, priorizando zonas identificadas por el indicador de sesgo regional; costo por unidad equipada. |
| 12 | ¿Quién la supervisaría? | FMF, con reporte anual público y el auditor externo extendido (recomendación 13). |
| 13 | ¿Bajo qué condiciones podría cerrarse? | Si el indicador de sesgo regional (recomendación 17) muestra que la brecha de cobertura de datos ya no está correlacionada con el nivel de recursos de la región. |
| 14 | ¿Qué riesgo tiene de ser capturada por intereses particulares? | Riesgo medio-alto, igual que la Beca Nacional del Agente 8, dado el patrón de opacidad financiera ya documentado — mitigación idéntica: reporte público anual y auditoría externa como condición no negociable. |

---

## 16. Recomendación

Priorización en tres horizontes, trazables a la numeración de la sección 13:

**Corto plazo (0-4 años) — verificación y extensión de bajo costo, no depende de resolver gobernanza primero:**
1. Auditar/confirmar la integración SIID-FIFA Connect ID (recomendación 1).
2. Publicar el alcance real del SIID por liga/categoría (recomendación 2).
3. Vincular y publicar el módulo de personal técnico del SIID con el registro de licencias, cerrando PQ-A05 (recomendación 4).
4. Verificación de identidad/edad reforzada al registrar (recomendación 11).
5. Registrar a todos los observados por el sistema de scouting, no solo a convocados (recomendación 12).
6. Extender el mandato del auditor externo del Agente 8 a datos/scouting (recomendación 13).
7. Esquema de acceso por niveles y minimización de datos de menores (recomendación 20).
8. Lineamientos sectoriales de datos de menores, operacionalizados (recomendación 19).

**Mediano plazo (4-8 años) — requiere que la extensión del corto plazo esté operando y produciendo datos confiables:**
9. Extensión de la obligatoriedad de registro hasta academias certificadas (recomendación 3).
10. Esquema común de datos para el convenio marco FMF-CONDDE-CONADEIP (recomendación 5).
11. Vincular minutos, pruebas físicas, lesiones y escolaridad al expediente único (recomendaciones 6-9).
12. Reconocimiento de plataformas de video ya usadas por clubes (recomendación 10).
13. Primeros indicadores de sesgo socioeconómico, regional y de edad relativa (recomendaciones 16-18).
14. Programa de Analistas de Datos Regionales y línea presupuestal de equipamiento (recomendaciones 21-22).

**Largo plazo (8-20 años) — depende de que el mediano plazo produzca series de datos consolidadas:**
15. Evaluación de academias basada en indicadores objetivos de datos, no solo autocertificación (recomendación 14).
16. Serie histórica consolidada de indicadores de sesgo (RAE, socioeconómico, regional) con al menos 8-10 años de datos, permitiendo medir si las correcciones de diseño (becas, mentores, sello de compatibilidad) efectivamente redujeron el sesgo medido en el punto de partida.

## 17. Responsable

FMF — Dirección de Sistemas/Tecnología (integración FIFA Connect ID, extensión del SIID, recomendaciones 1-3, 6, 10-12, 20); FMF — Formación Académica/ENDIT (vínculo con registro de licencias, recomendación 4, en coordinación directa con el responsable señalado por el propio Agente 8); FMF, CONDDE, CONADEIP y SEP (esquema común de datos del convenio marco, recomendación 5, en coordinación con el Agente 7); CAR-COM/CNAR-CONADE (pruebas físicas estandarizadas, recomendación 7); STPS y clubes/academias (padrón médico de lesiones, recomendación 8, aprovechando la obligación laboral ya vigente); FMF y SIPINNA/Procuradurías de Protección de NNA (canal de denuncia de datos de menores, recomendación 15, en coordinación con el Agente 3); Secretaría Anticorrupción y Buen Gobierno (lineamientos sectoriales, recomendación 19); una institución de educación superior o auditor deportivo independiente por convenio, el mismo mecanismo ya propuesto por el Agente 8 (recomendación 13) — no un organismo público nuevo, para evitar el riesgo de injerencia ya señalado en la línea base (`05`, Bloque C, decisión D-03) y consistente con el hallazgo de que ninguna capacidad nueva de este entregable es una institución.

## 18. Costo

**[ESTIMACIÓN, confianza C-D — no hay cifra base pública para calibrar ninguno de estos montos; órdenes de magnitud ilustrativos, a afinar por el Agente 14 en Fase 7]:**

| Componente | Orden de magnitud estimado | Base del cálculo |
|---|---|---|
| Auditoría/confirmación de integración FIFA Connect ID y publicación de alcance del SIID (recomendaciones 1-2) | $1–3 millones de pesos, una vez | Trabajo de verificación técnica y de cumplimiento normativo, no de desarrollo de plataforma |
| Extensión del SIID (módulo ligero de registro para academias, campos de fecha de nacimiento/CURP/biometría ligera, esquema de acceso por niveles) (recomendaciones 3, 11, 20) | $15–30 millones de pesos, una vez, más operación anual menor | Desarrollo sobre el sistema ya existente; no se construye una plataforma nueva desde cero |
| Módulos de datos (pruebas físicas, lesiones, escolaridad, video, minutos) vinculados al identificador único (recomendaciones 6-10) | $20–40 millones de pesos, una vez, más operación anual | Desarrollo de interfaces/API sobre el SIID extendido; costo mayor por número de integraciones (CAR-COM, padrón médico STPS, SEP, plataformas comerciales de video) |
| Esquema común de datos del convenio marco con CONDDE/CONADEIP (recomendación 5) | $3–8 millones de pesos, una vez | Interfaz de intercambio de datos entre sistemas ya existentes, no un sistema universitario nuevo |
| Auditoría externa anual extendida a datos/scouting (recomendación 13, sobre la misma partida ya presupuestada por el Agente 8) | Incremento marginal de $2–4 millones de pesos/año sobre el monto ya estimado por el Agente 8 ($3-6 millones/año) | Ampliación de alcance del mismo contrato de auditoría, no un segundo auditor |
| Programa de Analistas de Datos Regionales (30-40 personas, salario+viáticos, recomendación 21) | $18–24 millones de pesos/año | Analogía directa con el costeo que el propio Agente 8 hizo para su cuerpo de entrenadores mentores regionales (mismo número de personas, misma lógica territorial de 33 asociaciones estatales) |
| Línea presupuestal etiquetada de equipamiento de captura de datos/video (recomendación 22) | $10–20 millones de pesos/año | Estimación por analogía con costos de equipamiento tecnológico básico (cámaras, conectividad) para instituciones educativas de escala similar en México |
| **Total estimado, años 1-4** | **~$70–130 millones de pesos, una vez, más ~$50–90 millones de pesos/año en régimen** | Referencia de escala: comparable al costo total estimado por el Agente 8 para su propio pilar (~$50-90 millones de pesos/año) y muy por debajo del rango de ingresos anuales de Liga MX (600-900 millones de USD/año, según línea base) |

Ningún monto de esta tabla requiere presupuesto público nuevo: se financia redirigiendo fondos FIFA Forward/FMF de formación y tecnología ya existentes (dependencia explícita: transparencia financiera mínima de la FMF, hoy no verificada — riesgo ya documentado en la línea base, Bloque D).

## 19. Tiempo

- **Año 1:** verificación de integración FIFA Connect ID, publicación del alcance del SIID, inicio de verificación de identidad reforzada en nuevos registros.
- **Año 2-4:** extensión del registro a academias certificadas, primeros módulos de datos (minutos, pruebas físicas vía CAR-COM/CNAR), primer ciclo de indicadores de sesgo (aunque con cobertura parcial), lanzamiento del Programa de Analistas de Datos Regionales.
- **Año 4-8:** esquema común de datos con CONDDE/CONADEIP operando (depende de que el convenio marco del Agente 7 se firme), módulos de lesiones/escolaridad/video plenamente integrados, primeros ciclos comparables de indicadores de sesgo con series de 2-3 años.
- **Año 8-20:** evaluación de academias basada en datos objetivos consolidada como estándar; series de 8-10 años de indicadores de sesgo (RAE, socioeconómico, regional) que permitan medir tendencia, no solo fotografía; este pilar no debe prometer que el sesgo se elimine antes de una década, dado que incluso Dinamarca (10 años de intervención documentada) reconoce que el efecto de edad relativa persiste como problema recurrente.

## 20. Dependencias

1. Confirmación directa de la FMF sobre si el SIID ya está integrado con el FIFA Connect ID Service — condiciona si las recomendaciones 1-2 son de verificación de bajo costo o si requieren un proyecto de integración técnica más amplio.
2. Que el Agente 8 confirme (o la FMF confirme directamente) si el registro de licencias de entrenadores ya está de hecho vinculado al mismo SIID que registra personal técnico, o si son dos sistemas distintos dentro de la misma federación — condiciona el costo real de la recomendación 4.
3. Que CONDDE y CONADEIP tengan capacidad institucional y disposición de negociar el convenio marco del Agente 7 (R8) — sin eso, el esquema común de datos (recomendación 5) no tiene contraparte con quien integrarse.
4. Que la Secretaría Anticorrupción y Buen Gobierno efectivamente emita lineamientos sectoriales de datos de menores en el deporte (recomendación 19, ya solicitados por el Agente 3) — mientras no existan, este pilar opera con la LFPDPPP general como piso mínimo.
5. Transparencia financiera mínima de la FMF sobre los fondos FIFA Forward/de formación y tecnología ya existentes, para poder redirigir un porcentaje de forma auditable (recomendaciones 21-22) sin repetir el patrón de opacidad ya documentado.
6. Resolución de la relación de gobernanza FMF-Liga MX post-separación de abril de 2026 (`05`) — sin claridad sobre quién administra los sistemas de registro de clubes de Liga MX, la extensión de recomendaciones 3 y 20 a esa liga específica no tiene un responsable único claro.

## 21. Riesgos

- **Riesgo de que la integración FIFA Connect ID esté mandatada pero no implementada en la práctica**, y que este entregable haya sobreestimado la madurez real del SIID. Mitigación: la recomendación 1 (auditoría de cumplimiento) es la primera acción de todo el pilar, precisamente para no construir el resto del diseño sobre un supuesto no verificado.
- **Riesgo de "vigilancia sin protección"**: que la extensión de datos (pruebas físicas, biométricos, socioeconómicos) de menores se implemente sin los niveles de acceso y el consentimiento diferenciado de la recomendación 20, convirtiendo un sistema pensado para detectar sesgos en un riesgo adicional de privacidad para los mismos niños que busca proteger. Mitigación: la recomendación 20 y el convenio FMF-SIPINNA (recomendación 15) se fijan como condición no negociable, no como mejora opcional.
- **Riesgo de que el indicador de sesgo se cite como evidencia de que el sesgo "ya se resolvió" prematuramente**, sin series de datos suficientes (mínimo 3-5 ciclos) para distinguir tendencia de ruido estadístico. Mitigación: la sección 19 fija explícitamente que ningún indicador de sesgo debe tratarse como concluyente antes del mediano plazo.
- **Riesgo de captura de las dos líneas presupuestales nuevas** (recomendaciones 21-22) por el mismo patrón de opacidad y personalización del poder ya documentado en la línea base (Bloque B/D). Mitigación: reporte público anual y auditoría externa obligatorios, idéntico al estándar ya fijado por el Agente 8.
- **Riesgo de que la extensión del registro a academias (recomendación 3) se perciba como carga administrativa** por academias pequeñas/rurales, generando baja adopción o registro de mala calidad. Mitigación: vincular el registro al mismo sello de "academia certificada" que ya buscan las academias por prestigio/acceso a scouting, y priorizar el Programa de Analistas de Datos Regionales (recomendación 21) hacia esas zonas primero.
- **Riesgo de que el reconocimiento de plataformas comerciales de video (recomendación 10) introduzca dependencia de proveedores extranjeros sin control de datos de menores mexicanos.** Mitigación: condicionar el reconocimiento a que el proveedor cumpla la LFPDPPP y a que el video quede etiquetado con el identificador único bajo control de la FMF, no del proveedor.
- **Riesgo, ya señalado por el Agente 5B, de que cualquier reforma de datos de identidad/edad se construya sobre un problema de fraude de edad no diagnosticado para México** — la recomendación 11 (verificación reforzada) mitiga el riesgo hacia adelante, pero no diagnostica si ya existe fraude de edad en el sistema actual; ese diagnóstico requiere la auditoría de la recomendación 1 y 13.

## 22. Bloqueadores

- Que la FMF no confirme (o confirme negativamente) la integración con FIFA Connect ID, obligando a rediseñar el componente de identificador desde una base distinta a la asumida en este entregable.
- Opacidad financiera de la FMF sobre fondos FIFA Forward/tecnología, que podría impedir verificar que el porcentaje redirigido a las recomendaciones 21-22 efectivamente se ejecuta.
- Ausencia de disposición de CONDDE/CONADEIP a compartir datos de sus jugadores con el sistema de scouting profesional (mismo riesgo ya señalado por el Agente 7: "consenso sin incentivo corregido").
- Que la Secretaría Anticorrupción y Buen Gobierno, de creación reciente y capacidad aún en consolidación (Agente 3), tarde varios años en emitir lineamientos sectoriales, dejando el esquema de datos de menores operando solo con la LFPDPPP general durante ese periodo.
- La Asamblea de Dueños de Liga MX, si percibe la extensión de obligaciones de registro/datos como un costo no compensado — mismo patrón de resistencia ya documentado con la regla de menores y el licenciamiento de entrenadores (Agente 8).

## 23. Indicadores

### 23.1 Indicador central (responde PQ-P10): cobertura real del identificador único por nivel de la pirámide

**[RECOMENDACIÓN, confianza C — no existe hoy una línea base verificada, dado el vacío de auditabilidad ya declarado en S-06]:**

| Nivel de la pirámide | Situación de partida (confianza) | Meta año 4 | Meta año 8 | Meta año 20 |
|---|---|---|---|---|
| Liga MX / Expansión / Premier / TDP | Cubierto por SIID, integración con FIFA Connect ID por confirmar (confianza B) | Integración FIFA Connect ID confirmada y publicada al 100% | Historial de minutos/posiciones/pruebas físicas vinculado al 100% | Serie histórica de 12-16 años por jugador de esta franja |
| Academias certificadas de la FMF (~168,000 niños reportados) | Sin evidencia de registro en el SIID (confianza D) | ≥25% de academias certificadas con registro de jugadores en el módulo extendido | ≥70% | ≥95% |
| Red de scouting escolar (28,000+ escuelas, 1.13M estudiantes) | Sin registro individual, solo cifra agregada de escuelas participantes (confianza B) | Registro del 100% de los 11,000+ observados/año (no solo convocados) | Registro georreferenciado por municipio | Serie histórica de 12-16 años de observaciones, no solo de convocados |
| CONDDE / CONADEIP | Circuitos sin vínculo documentado (confianza B, dato de ausencia) | Convenio marco firmado (depende del Agente 7) con perfil ligero de al menos un torneo nacional por circuito | Perfil ligero para el 100% de los jugadores en fase final de cada campeonato nacional | Historial multianual de jugadores universitarios visibles para scouting profesional |

### 23.2 Indicadores de sesgo (maduración temprana/RAE, socioeconómico, regional)

- Distribución por trimestre de nacimiento de convocados frente a jugadores registrados en el sistema (fuente: FMF/auditor externo, frecuencia anual) — responde directamente al riesgo de efecto de edad relativa señalado por el benchmark danés.
- Tasa de observación/invitación por municipio, cruzada con el índice de marginación de CONEVAL (fuente: FMF + CONEVAL, frecuencia anual).
- Densidad de observaciones de scouting por estado, cruzada con población de jugadores registrados por estado (fuente: FMF/auditor externo, frecuencia anual).
- Porcentaje de academias certificadas cuya certificación incluye ya datos objetivos de egreso/minutos/lesión/continuidad escolar, no solo autocertificación (fuente: auditor externo, frecuencia anual).

### 23.3 Indicador que cierra el pedido explícito del Agente 8

- Número de personas con licencia de entrenador vigente por nivel (D a PRO) y por estado, publicado a partir del cruce SIID (módulo de personal técnico) × registro de licencias de Formación Académica/ENDIT (fuente: FMF, frecuencia anual) — este es el dato exacto que el Agente 8 dejó pendiente en PQ-A05 y que este pilar resuelve por vínculo, no por levantamiento nuevo.

### 23.4 Indicador de auditabilidad (responde al mandato de producir, no asumir, S-06)

- Porcentaje de las cifras institucionales citadas en este documento y en los entregables previos de Fase 5 (academias certificadas, observados, convocados, minutos) que cuentan con verificación externa independiente, no solo autorreporte (fuente: auditor externo extendido, recomendación 13, frecuencia anual) — meta explícita: 0% verificado hoy → ≥50% verificado en año 4 → 100% en año 8.

## 24. Casos internacionales

- **FIFA Connect ID / DTMS (global, no un "país" del benchmark de Fase 4, sino infraestructura del organismo rector) — "aplicable directamente" en su componente de identificador**, porque su adopción ya es obligatoria para la FMF desde 2020; no requiere adaptación de transferibilidad como los casos de país, requiere verificación de cumplimiento (sección 15.0).
- **Dinamarca — "aplicable con adaptación", tratamiento del efecto de edad relativa (RAE) y bio-banding** (`fase4-agente5b`, sección 12): fundamenta el indicador de la sección 23.2 y la advertencia explícita de que este indicador solo es confiable si primero se resuelve la verificación de identidad/edad (recomendación 11) — Dinamarca no tuvo que resolver un problema de fraude de identidad al diseñar su indicador; México sí debe descartarlo primero.
- **Islandia — "no transferible en escala" para este pilar específico** (`fase4-agente5b`, sección 24): se cita explícitamente como el caso que **no** aplica — un país de tamaño tan pequeño que nunca necesitó construir infraestructura de datos y scouting, a diferencia de México, que si necesita la extensión de datos aquí diseñada precisamente por su escala 325-340 veces mayor.
- **Portugal/España (Agente 5A) — modelo de negocio de scouting internacional agresivo** (`fase4-agente5a`, sección 3): relevante solo como antecedente de que el scouting de datos y video es una práctica consolidada de clubes profesionales; no es un caso de sistema nacional de datos y no se usa como base de ninguna recomendación estructural de este pilar.
- **Corea del Sur/Japón (Agente 5E) — advertencia metodológica, no caso de datos**: el benchmark de Asia-Oceanía deja explícitamente pendiente, sin resolver, la misma pregunta PQ-P10 para Japón/Corea ("JFA/KFA no publican metodología de interoperabilidad verificable") — confirma que ningún país del benchmark completo de la Fase 4 documentó, con evidencia suficiente, un sistema de datos/scouting nacional que México pudiera copiar literalmente; el diseño de este pilar se apoya más en la arquitectura ya obligatoria de FIFA que en un caso de país replicable.

## 25. Adaptación a México

- **De FIFA Connect ID/DTMS:** se adopta como base técnica el identificador ya obligatorio, sin construir uno propio; se adapta extendiendo su alcance doméstico hacia academias, escuelas y universidades — un tramo que el mandato global de FIFA no cubre por diseño, porque FIFA Connect ID solo alcanza a quien ya está registrado en un sistema nacional integrado (Liga MX-Expansión-Premier-TDP en el caso mexicano, según lo verificado en este entregable).
- **De Dinamarca:** se adopta el principio de medir el efecto de edad relativa con datos propios, pero se antepone —a diferencia del caso danés— una etapa de verificación de identidad/edad reforzada (recomendación 11), porque el benchmark mexicano (vía Agente 5B) señala un riesgo de fraude de edad que Dinamarca no tuvo que resolver primero.
- **De Islandia:** se descarta explícitamente la lógica de que "el sistema es tan pequeño que no necesita infraestructura de datos" — es la razón misma por la que México sí necesita este pilar, y por la que la escala (325-340 veces mayor) se usa como justificación de la extensión de datos, no como obstáculo.
- **De ningún país en particular (patrón transversal del benchmark):** se adopta la conclusión repetida en las Fases 4 y 5 de que ningún país exitoso resolvió un problema de datos/formación creando una institución nueva y aislada de su federación — se aplica aquí con la misma lógica que los Agentes 6, 7, 8 y 9 aplicaron a sus propios pilares.

## 26. Preguntas pendientes

Ver sección "Preguntas nuevas para el registro maestro" a continuación, que consolida las preguntas identificadas a lo largo de este entregable que no pudieron resolverse con la información disponible.

---

## Preguntas nuevas para el registro maestro

| ID propuesto | Pregunta | Fuente esperada | Estado |
|---|---|---|---|
| PQ-10-01 | ¿Está el SIID de la FMF efectivamente integrado con el FIFA Connect ID Service, conforme al mandato FIFA vigente desde el 1 de julio de 2020, o solo cumple el requisito de tener un sistema doméstico propio sin la integración global? | FMF (Dirección de Sistemas/Tecnología), FIFA | Pendiente — condiciona si las recomendaciones 1-2 de este entregable son de verificación de bajo costo o de un proyecto de integración técnica mayor |
| PQ-10-02 | ¿El registro de personal técnico que ya administra el SIID incluye el nivel de licencia (D-C-B-A-PRO) de cada persona, o solo su identidad y función, sin ese campo? | FMF (Formación Académica/ENDIT, Dirección de Sistemas) | Pendiente — condiciona si la recomendación 4 (cierre de PQ-A05 del Agente 8) es de publicación inmediata o requiere agregar un campo nuevo al sistema |
| PQ-10-03 | ¿El SIID cubre hoy, de alguna forma, a las academias certificadas no afiliadas como club de Liga MX/Expansión/Premier/TDP, o su alcance se limita estrictamente a clubes de esas cuatro ligas? | FMF | Pendiente |
| PQ-10-04 | ¿Qué plataformas de análisis de video (comerciales o propias) usan hoy, si alguno, los clubes de Liga MX/Expansión para scouting, y estarían dispuestos a que sus datos se etiqueten con el identificador único de este pilar? | Clubes de Liga MX/Expansión, proveedores de tecnología deportiva | Pendiente |
| PQ-10-05 | ¿Existe evidencia documentada, aunque sea anecdótica o periodística, de fraude de edad o de identidad en categorías juveniles mexicanas (fuerzas básicas, academias, selecciones menores)? | FMF, prensa deportiva especializada, clubes | Pendiente — condiciona la urgencia real de la recomendación 11 (verificación reforzada) |
| PQ-10-06 | ¿CONDDE y CONADEIP tienen hoy algún sistema propio de registro/identificador de jugador universitario, y con qué campos (fecha de nacimiento, escuela de procedencia, posición)? | CONDDE, CONADEIP | Pendiente — insumo directo para diseñar el esquema común de datos (recomendación 5) |
| PQ-10-07 | ¿Qué porcentaje de los 11,000+ observados anualmente por el sistema de scouting de la FMF tiene hoy, aunque sea parcialmente, algún dato digital capturado (no solo una anotación en papel o criterio del ojeador)? | FMF (sistema de scouting nacional) | Pendiente — condiciona el costo real de la recomendación 12 |
| PQ-10-08 | ¿Qué lineamientos, guías o criterios, si alguno, tiene previsto emitir la Secretaría Anticorrupción y Buen Gobierno específicamente para datos de menores en el deporte, y en qué plazo? | Secretaría Anticorrupción y Buen Gobierno | Pendiente (ya formulada por el Agente 3 como PQ-C05; se reitera aquí aplicada específicamente al esquema de este pilar) |
| PQ-10-09 | ¿Existe ya algún mecanismo de verificación de identidad (CURP, biometría) en el registro actual del SIID, o el alta se realiza hoy solo con documentación en papel/PDF cargado por el club? | FMF | Pendiente — condiciona si la recomendación 11 es una mejora incremental o un cambio estructural del proceso de alta |
| PQ-10-10 | ¿Qué porcentaje del presupuesto de tecnología/sistemas de la FMF (distinto del de Formación Académica, ya preguntado por el Agente 8 en PQ-8-03) proviene de fondos FIFA Forward, y cuánto de ese monto podría redirigirse a la extensión del SIID sin afectar otros compromisos? | FMF, informes FIFA Forward | Pendiente |

---

## Supuestos y riesgos nuevos identificados

### Supuestos nuevos

| ID | Supuesto | Justificación | Sensibilidad | Consecuencia si es falso | Validación requerida |
|---|---|---|---|---|---|
| S-10-01 | La integración obligatoria de FIFA Connect ID (vigente globalmente desde 2020) ya fue implementada por la FMF, o puede completarse como trámite de cumplimiento normativo de bajo costo, sin requerir el desarrollo de un identificador propio desde cero | Inferencia razonable de que un mandato FIFA vigente desde hace más de cinco años debería estar, al menos parcialmente, cumplido por una federación que además ya opera el SIID de forma consolidada | Alta — si la FMF no ha avanzado en esta integración en absoluto, el costo y el plazo de las recomendaciones 1-2 (sección 12) se subestiman de forma importante, y el diagnóstico central de este entregable ("no hace falta un identificador nuevo") se debilitaría, aunque no necesariamente se invalidaría, porque el mandato seguiría existiendo como obligación pendiente de cumplir, no como alternativa a construir algo nuevo | Confirmar directamente con la FMF (PQ-10-01) antes del Control 4 (Diseño) |
| S-10-02 | El registro de personal técnico que el SIID ya administra (hallazgo de la sección 5) es suficientemente completo (incluye o puede incluir fácilmente el nivel de licencia) como para que la recomendación 4 sea de "publicar y vincular", no de "construir un campo nuevo" | Inferencia de que un sistema que ya registra formalmente a jugadores y personal técnico para efectos de elegibilidad en competencia probablemente ya captura, como mínimo, identidad y función de esa persona | Alta — si el sistema solo registra identidad/función sin nivel de licencia, cerrar PQ-A05 requeriría una integración de datos entre dos sistemas de la FMF (SIID y Formación Académica/ENDIT) que hoy podrían no estar conectados, elevando el costo y el plazo de la recomendación 4 | Confirmar con la FMF (PQ-10-02) antes de que el Agente 14 costee esta recomendación en Fase 7 |
| S-10-03 | No existe hoy, en México, un problema significativo de fraude de edad/identidad en categorías juveniles que la recomendación 11 (verificación reforzada) deba resolver con urgencia, más allá del riesgo hipotético señalado por el Agente 5B para la región | El benchmark y la línea base no documentan ningún caso mexicano concreto (a diferencia de otros países de América Latina mencionados de forma general por el Agente 5B); se trata como riesgo preventivo, no como problema ya diagnosticado | Media — si en realidad ya existe un problema documentado (no encontrado en esta investigación por no haberse buscado directamente), la prioridad de la recomendación 11 debería subir del corto al primer año, no al ciclo general de corto plazo | Confirmar con la FMF y con una revisión de prensa deportiva especializada (PQ-10-05) antes del Control 4 |
| S-10-04 | Los clubes de Liga MX/Expansión MX ya usan, de forma privada y comercial, alguna plataforma de análisis de video para scouting, por lo que la recomendación 10 (reconocimiento, no construcción) es viable sin desarrollo tecnológico mayor por parte de la FMF | Práctica estándar documentada en el fútbol profesional a nivel mundial (no verificada específicamente para México en esta sesión) | Media — si los clubes mexicanos no usan estas herramientas de forma consolidada, la recomendación 10 tendría que reformularse como un programa de adopción tecnológica, no solo de reconocimiento regulatorio | Confirmar con clubes de Liga MX/Expansión (PQ-10-04) antes de que el Agente 14 costee esta recomendación |

### Riesgos nuevos

| Riesgo | Probabilidad | Impacto | Señal temprana | Responsable | Mitigación | Contingencia |
|---|---|---|---|---|---|---|
| Que la extensión de datos de este pilar (biométricos, socioeconómicos, médicos de menores) se implemente antes de que existan los lineamientos sectoriales de la Secretaría Anticorrupción y Buen Gobierno (recomendación 19), operando en una zona gris de cumplimiento con la LFPDPPP general pero sin guía sectorial específica | Alta | Alto — riesgo legal y reputacional, además del riesgo de vulneración de derechos de menores ya señalado como el vacío más urgente del proyecto completo (línea base, resumen ejecutivo) | Implementación de módulos de datos sensibles de menores (sección 12, recomendaciones 7-9, 16, 18) sin que el esquema de acceso por niveles (recomendación 20) esté operando primero | Agente 0 (integración Fase 6), Agente 16 (Red Team) | Fijar como condición no negociable que ningún módulo de dato sensible de menores (pruebas físicas, lesiones, socioeconómico identificable) entre en operación antes de que la recomendación 20 (esquema de acceso por niveles) esté implementada, independientemente de si ya existen lineamientos sectoriales publicados | Suspender el módulo de dato sensible correspondiente hasta que el esquema de acceso esté verificado por el auditor externo |
| Que los indicadores de sesgo (RAE, socioeconómico, regional) se usen en fases posteriores (presupuesto, síntesis) como si fueran series históricas consolidadas, cuando en realidad su primer ciclo tendría, en el mejor de los casos, cobertura parcial y sin comparación temporal | Media | Alto — mismo patrón de riesgo ya señalado por el Agente 8 sobre el uso indebido de metas de política como si fueran hechos verificados | Cita de estos indicadores en documentos de Fase 7 o Fase 9 sin la etiqueta de confianza C ni la advertencia explícita de la sección 23.1/23.2 sobre cobertura parcial en los primeros ciclos | Agente 0 (integración Fase 6), Agente 17 (síntesis final) | Exigir que cualquier cita de estos indicadores en fases posteriores incluya el número de ciclos de datos disponibles y su nivel de cobertura real | Corregir en el Control 5 (síntesis) si se detecta uso indebido |
| Que la verificación de identidad reforzada (recomendación 11, CURP/biometría ligera) se perciba, por parte de familias de escasos recursos o de comunidades indígenas/rurales sin documentación oficial completa, como una barrera adicional de acceso al sistema de scouting, en vez de una salvaguarda | Media | Medio-Alto — podría profundizar, no reducir, el sesgo socioeconómico y regional que este mismo pilar busca medir y corregir | Tasa de rechazo o abandono de registro más alta en municipios de menor índice de desarrollo humano tras implementar la recomendación 11 | FMF, Programa de Analistas de Datos Regionales (recomendación 21) | Diseñar una vía de registro provisional (sin CURP, con verificación posterior asistida) para casos de documentación incompleta, en vez de excluir de origen; priorizar el apoyo del Programa de Analistas de Datos Regionales hacia estas comunidades | Si la tasa de exclusión sube, suspender el requisito estricto de CURP/biometría y sustituirlo temporalmente por verificación manual asistida hasta corregir el diseño |
| Que el reconocimiento regulatorio de plataformas comerciales de video (recomendación 10) transfiera de facto datos de menores mexicanos a servidores o gobernanza de datos fuera de la jurisdicción de la LFPDPPP, sin que la FMF tenga control real sobre su tratamiento posterior | Media | Alto | Ausencia de cláusulas contractuales de localización/control de datos en los acuerdos de reconocimiento de plataformas | FMF, Secretaría Anticorrupción y Buen Gobierno | Condicionar el reconocimiento de cualquier plataforma comercial a cláusulas contractuales de protección de datos de menores compatibles con la LFPDPPP, incluyendo derecho de auditoría de la FMF sobre el tratamiento de esos datos | Revocar el reconocimiento de la plataforma si incumple las cláusulas, sin que ello afecte al resto del sistema (el reconocimiento es por proveedor, no una dependencia estructural única) |
