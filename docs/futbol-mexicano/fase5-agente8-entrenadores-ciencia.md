# Fase 5 — Agente 8: Entrenadores y ciencia
## Pilar 8 — Sistema de capital humano técnico-científico del fútbol mexicano

**Fecha de entrega:** 2026-07-23
**Agente:** 8 (Diseño, Fase 5)
**Depende de:** `00-agente0-metodologia-y-plan.md`, `02-plantilla-entregable.md`, `05-fase3-linea-base-consolidada.md`, `08-fase4-benchmark-consolidado.md`, `fase2-agente1-capacidades-existentes.md`, `fase4-agente5b-benchmark-paises-pequenos.md`, `fase4-agente5e-benchmark-asia-oceania.md` (Control 2 y Control 3 superados)
**Alcance:** Pilar 8 de la taxonomía (`00`, sección 4) — licencias, certificaciones, becas, formación digital, mentoría, evaluación práctica, recertificación, especialización, entrenadores comunitarios, entrenadoras, directores deportivos, scouts, analistas, psicólogos, nutriólogos y árbitros, **construido sobre** la pirámide D→C→B→A→PRO de la FMF rediseñada en 2025 — no como sistema nuevo.
**Regla de intervención aplicada:** de las 20 recomendaciones numeradas de la sección 16, 18 (90%) caen en las categorías 1–6 de la jerarquía de intervención (aprovechar, corregir, integrar, escalar, redistribuir, cambiar reglas) y solo 2 (10%) requieren capacidad complementaria nueva, ambas con las 14 preguntas de justificación respondidas en la sección 15 — cumple el mínimo del 70% exigido por la sección 2 del manual metodológico.

---

## 1. Resumen ejecutivo

México ya tiene el activo central que este pilar necesita: una pirámide de licencias de entrenador D→C→B→A→PRO, rediseñada por la FMF en 2025 con vocación de aval de Concacaf y eventual equivalencia UEFA [HECHO, nivel B, según Agente 1]. El problema no es la ausencia de un sistema — es que (a) nadie sabe cuántos entrenadores hay certificados en cada nivel ni dónde (PQ-A05, dato incompleto declarado por el Agente 1); (b) la certificación no es obligatoria para entrenar en las más de 2,000 academias "certificadas" que atienden a ~168,000 niños, cuyo propio estándar de certificación no está definido públicamente (PQ-A07); (c) la recertificación trienal existente es solo temporal, sin evaluación práctica de habilidades; y (d) no existe ningún mecanismo formal de mentoría, especialización acreditada (ciencia del deporte, psicología, nutrición, scouting, dirección deportiva) ni protección de menores integrado a la licencia. Este entregable diseña el pilar completo **reformando, integrando y escalando** ese sistema existente, sin proponer una institución paralela. El caso de Islandia (certificación obligatoria incluso para entrenar niños de 10 años) se usa como **principio**, no como cifra literal: la diferencia de escala (~325–340x, según `fase4-agente5b`) hace inviable copiar el ratio islandés per cápita, así que este entregable fija metas propias de "entrenadores certificados por cada 1,000 jugadores en el sistema estructurado" con metodología explícita y nivel de confianza C, a falta de una cifra base verificada. La meta central: **de 0 (basal desconocida) a un piso de 40 entrenadores licenciados (D o superior) por cada 1,000 niños en programas estructurados hacia el año 8, y ≥90 hacia el año 20** en el nivel de iniciación, con metas decrecientes por nivel competitivo superior (ver sección 23). El cierre del vacío de datos (PQ-A05) no requiere un sistema nuevo: se resuelve integrando el registro de licencias que la FMF ya administra internamente con la arquitectura de identificador único que diseñará el Agente 10 (Pilar 9).

---

## 2. Objetivo

Diseñar, para el Pilar 8 de la taxonomía del proyecto, el sistema de capital humano técnico-científico del fútbol mexicano — licencias progresivas, certificación accesible, becas, formación digital, mentoría, evaluación práctica, recertificación, especialización (directores deportivos, scouts, analistas, psicólogos, nutriólogos), entrenadores comunitarios, entrenadoras, y su integración con la formación arbitral — construido explícitamente sobre la pirámide D→C→B→A→PRO ya existente, siguiendo la jerarquía de intervención de la sección 2 del manual metodológico y fijando metas concretas de densidad de entrenadores certificados por cada mil jugadores.

---

## 3. Preguntas del registro maestro abordadas

| ID | Pregunta | Estado tras este entregable |
|---|---|---|
| PQ-P08 | ¿Cuántos entrenadores certificados hay por cada mil jugadores federados? | No se puede responder con la línea de base actual (dato incompleto, PQ-A05); este entregable fija **metas** hacia adelante y el mecanismo para medir el punto de partida real (sección 9, 23) |
| PQ-A05 | ¿Cuántos entrenadores tiene la FMF certificados hoy en cada uno de los cinco niveles, con desagregación territorial? | No resuelta como dato — resuelta como **diseño de mecanismo de cierre** (integración con Agente 10, sección 9 y 12) |
| PQ-A07 | ¿Qué define exactamente la FMF como "academia certificada" y cuántas de las +2,000 cumplen el estándar de forma auditada? | Insumo directo: se propone que la licencia mínima del cuerpo técnico sea parte explícita de ese estándar (sección 13, recomendación 3) |
| PQ-E2-01 | ¿Cuántos entrenadores mexicanos tienen licencia por nivel, en unidad comparable a "por cada mil jugadores federados"? | Reformulada como meta de diseño (sección 23), no como hallazgo — sigue pendiente como dato (bloqueador, sección 8) |
| PQ-B10 | Cifras salariales reales de Liga MX Femenil (parcialmente relevante: brecha de recursos para formación de entrenadoras) | Insumo parcial: se incorpora como restricción de diseño en la sección de redistribución (sección 13, recomendación 6) |
| PQ-P13 | ¿Qué brecha separa a la Liga MX Femenil de la varonil? | Insumo parcial en el diseño de cuotas de mentoría/becas para entrenadoras (sección 13, recomendación 6); la auditoría transversal completa corresponde al Agente 13 |

Preguntas nuevas generadas por este entregable: ver sección final.

---

## 4. Metodología

**Fuentes usadas:** los seis documentos de insumo obligatorio listados en el encabezado (línea base consolidada, benchmark consolidado, benchmark de países pequeños y de Asia-Oceanía, capacidades existentes), más dos búsquedas web dirigidas (23 de julio de 2026) para verificar si existe una cifra internacional comparable de "entrenadores certificados por cada mil jugadores federados" que pudiera servir de referencia cuantitativa adicional a la de Islandia. Ninguna búsqueda produjo una cifra consolidada, actual y verificable de esa razón para España, Inglaterra o Alemania (fuentes encontradas: cifras de licencias UEFA por país de 2010-2017, sin desagregación por jugadores federados comparables, nivel C/D) ni una cifra pública y actualizada de entrenadores FMF certificados por nivel (portal `formacionacademica.fmf.mx` describe la estructura de las licencias, no el número de personas certificadas). Este resultado **confirma, no contradice**, el vacío de datos ya declarado por el Agente 1 (PQ-A05) y la limitación ya declarada por el Agente 5B (no hay conversión confiable entre "entrenadores por habitante" y "entrenadores por jugador federado"). Por tanto, las metas numéricas de este entregable (sección 23) se construyen como **objetivos de política pública**, no como extrapolación directa de una cifra internacional, y se etiquetan con su nivel de confianza correspondiente (mayoritariamente C).

**Clasificación de evidencia:** escala A–D de la sección 3.2 del manual metodológico, aplicada igual que en los entregables de Fase 2 y 4 que son insumo de este documento.

**Periodo cubierto:** estado actual (2025-2026) de la pirámide de licencias FMF; metas de diseño a 4, 8, 12 y 20 años, según la sección 3.4 del manual metodológico.

---

## 5. Hallazgos

- **[HECHO]** La pirámide de licencias D→C→B→A→PRO existe, fue rediseñada en 2025, tiene vigencia de 3 años por nivel, toma ~5 años completarla, y busca aval de Concacaf y equivalencia UEFA. Evidencia B (Agente 1, sección 5.3).
- **[DATO INCOMPLETO]** No existe cifra pública de cuántos entrenadores hay certificados por nivel ni su distribución territorial (PQ-A05). Este es el vacío más limitante para cualquier meta cuantitativa de este pilar.
- **[HECHO]** La licencia PRO es obligatoria únicamente para dirigir en Liga MX (el primer entrenador); no hay evidencia de que exista un requisito de licencia mínima para entrenar en las academias certificadas de fuerzas básicas, escuelas o comunidad. Evidencia B (Agente 1).
- **[DATO INCOMPLETO]** El estándar de "academia certificada" (+2,000 reportadas) no está públicamente definido — no se sabe si incluye un requisito de licencia del cuerpo técnico (PQ-A07, Agente 1).
- **[HECHO]** No existe evidencia de un canal de denuncia independiente de protección de menores en captación/pruebas — la línea base jurídica (`05`, Bloque C) lo señala como el vacío legal más urgente del proyecto completo, con casos documentados (Riodoce, 2025) sin consecuencia pública conocida.
- **[HECHO]** El benchmark islandés muestra que la certificación obligatoria de entrenadores —incluso para niños de 10 años— es una reforma de **regla**, no de infraestructura ni de escala poblacional, y es "aplicable con adaptación" a México según la matriz de transferibilidad del Agente 5B, **exclusivamente en ese componente**, no en su lógica de "conocer a cada niño" (inviable a escala 325-340x mayor).
- **[HECHO]** El benchmark de Asia-Oceanía documenta que Corea del Sur impuso la obligatoriedad de categorías juveniles certificadas en 2020 sobre una liga de 37 años (K League, fundada 1983) — el caso más análogo al punto de partida mexicano (liga profesional ya consolidada), y que el principio de "currícula técnica nacional integrada a las licencias ya existentes" (Bélgica, Japón "Japan's Way", Australia 2009) es la vía preferida sobre crear un instituto aparte.
- **[HECHO]** Dinamarca opera seis "Talent Coaches" de la DBU vinculados a clubes de primera y segunda división como mecanismo de integración federación-clubes sin crear una institución paralela — modelo directamente adaptable a la escala mexicana (sección 13, recomendación 10).
- **[HECHO]** Ningún caso del benchmark completo resolvió su problema sustituyendo su federación o creando una institución nueva (`fase4-agente5b`, punto 14; `fase4-agente5e`, punto 14) — refuerza la instrucción de construir sobre la pirámide FMF existente.

---

## 6. Evidencia (cifras citadas en este entregable)

| Cifra | Fuente | Fecha del dato | Alcance | Metodología | Limitaciones | Confianza |
|---|---|---|---|---|---|---|
| Pirámide D-C-B-A-PRO, ~5 años a PRO, vigencia 3 años/nivel | FMF (Formación Académica) vía Agente 1 | 2025 | Nacional | Anuncio institucional | Reglamento primario no verificado línea por línea | B |
| 728 entrenadores licencia UEFA A+B en Islandia (2013) para ~380,000 habitantes | Agente 5B, vía Tribuna.com/These Football Times | 2013 | Nacional (Islandia) | Recuento institucional (KSÍ) reportado por prensa | No convertible de forma confiable a "por jugador federado"; no usar como meta literal para México | B, con limitación explícita de conversión |
| +2,000 academias certificadas/en proceso, ~168,000 niños atendidos | FMF vía Agente 1 | 2025-2026 | Nacional | Declaración institucional | Sin desagregación territorial ni estándar de certificación público (PQ-A07) | B |
| 28,000+ escuelas, 1.13M estudiantes en programa de scouting escolar | FMF vía Agente 1 | 2026 | Nacional | Declaración institucional | Cifra autorreportada, no auditada | B |
| Costo de fuerzas básicas para familias: $0–$40,000 pesos/año | Profeco, vía línea base (`05`) | 2026 | Nacional | Encuesta de precios | No incluye costo de licenciamiento de entrenadores, que es un rubro distinto no documentado | B |
| Costo estimado de formar un jugador hasta primer equipo: $7–10 millones de pesos | Línea base (`05`, Bloque D) | 2026 | Nacional (estimación agregada) | No auditada | Evidencia C, no usar como base de diseño estructural sin verificación | C |
| Six "Talent Coaches" de la DBU vinculados a clubes daneses | Agente 5B | 2026 (reporte) | Nacional (Dinamarca) | Descripción institucional | Sin cifra de costo verificada | B |
| Cifra de licencias UEFA por país (Spain ~24,000 vs. Inglaterra ~2,700, año ~2010-2012) | Búsqueda web de este entregable (fuentes de prensa/estadística no consolidadas) | ~2010-2017 | Europa (varios países) | Recuento institucional por país, sin metodología unificada verificada en esta sesión | Cifra ampliamente citada en periodismo pero sin fuente primaria única verificada en esta búsqueda; no comparable directamente con jugadores federados de cada país | D — no se usa como base de ninguna meta de este entregable, solo como antecedente de que la disparidad de densidad de licenciamiento es un patrón documentado en el fútbol mundial |

---

## 7. Fuentes

- `00-agente0-metodologia-y-plan.md`, `02-plantilla-entregable.md`, `05-fase3-linea-base-consolidada.md`, `08-fase4-benchmark-consolidado.md`, `fase2-agente1-capacidades-existentes.md`, `fase4-agente5b-benchmark-paises-pequenos.md`, `fase4-agente5e-benchmark-asia-oceania.md` — documentos internos del proyecto, ya citados con su propia cadena de fuentes primarias/secundarias.
- Búsqueda web (23 de julio de 2026): "UEFA coaching licenses per number of registered players Spain England Germany ratio" — sin resultado consolidado y verificable; se documenta el vacío, no se usa ninguna cifra encontrada como base de diseño.
- Búsqueda web (23 de julio de 2026): "FMF entrenadores certificados licencia PRO A B C D cuántos 2025 2026" — confirma la estructura de horas/meses de cada licencia (`formacionacademica.fmf.mx`, portales de Licencia C/D) pero no aporta cifra de personas certificadas; consistente con el vacío ya declarado por el Agente 1 (PQ-A05).

---

## 8. Limitaciones

- La limitación más importante de este entregable es estructural, no metodológica: **no existe una cifra base (baseline) verificable** de entrenadores certificados por nivel en México (PQ-A05), por lo que ninguna meta numérica de la sección 23 puede expresarse como "aumentar X%" — solo como piso absoluto de política pública, con su nivel de confianza declarado.
- No fue posible verificar el reglamento primario completo de la pirámide D-C-B-A-PRO (solo el resumen ya reportado por el Agente 1); este entregable diseña sobre la estructura general (niveles, horas, vigencia) reportada, no sobre el texto íntegro del reglamento.
- La cifra islandesa de "entrenadores por habitante" no es convertible de forma confiable a "entrenadores por jugador federado" (limitación ya declarada por el Agente 5B) — este entregable no intenta forzar esa conversión; usa el caso islandés solo como referencia de **principio** (certificación obligatoria incluso a nivel comunitario), no de magnitud.
- No se investigó en esta sesión el costo real de emitir cada nivel de licencia en México (matrícula, materiales, evaluador) — los órdenes de magnitud de costo de la sección 18 son estimaciones preliminares (confianza C-D), a afinar por el Agente 14 en Fase 7.
- La brecha de recursos entre la rama varonil y femenil del sistema de licenciamiento (relevante para la meta de entrenadoras) no se investigó a fondo en este entregable — corresponde al Agente 13 (auditoría transversal); aquí solo se incorpora como restricción de diseño (cuota mínima en becas/mentorías).

---

## 9. Activos existentes

- Pirámide de licencias D→C→B→A→PRO (2025), con vigencia trienal, ruta de ~5 años a PRO, y proceso ya iniciado de aval de Concacaf/equivalencia UEFA.
- Portal digital de Formación Académica de la FMF (`formacionacademica.fmf.mx`), ya operando como plataforma de gestión de licencias por nivel (Licencia C, Licencia D documentadas públicamente).
- Red de +2,000 academias certificadas/en proceso (~168,000 niños) y red de scouting escolar (28,000+ escuelas, 1.13M estudiantes) — canales de distribución ya existentes para llevar certificación a escala, sin construir infraestructura nueva.
- Legado físico del Mundial 2026 (CAR del COM renovado con 390 millones de pesos, CNAR de Conade con 562 camas) — instalaciones ya disponibles para residencias de evaluación práctica y mentoría, sin inversión adicional de infraestructura.
- Flujo de fondos FIFA Forward ya destinado a formación de la FMF (evidenciado en la renovación del CAR) — fuente de financiamiento ya existente que puede redirigirse parcialmente, no un fondo por crear.
- Sistema de scouting nacional de la FMF (11,000+ observados/año, 315 invitaciones, 97 convocatorias en 2025) — base institucional ya operando sobre la cual certificar y profesionalizar el rol de scout.
- Programas universitarios de ciencias del deporte, psicología del deporte y nutrición en instituciones públicas y privadas (UNAM, IPN y otras, vía CONDDE) y en instituciones privadas (vía CONADEIP) — oferta formativa ya existente y acreditada, no construida por este proyecto.
- Comisión/estructura de formación arbitral de la FMF, operando en paralelo al sistema de entrenadores — activo existente que puede compartir infraestructura digital sin duplicarla.

---

## 10. Problemas

1. Vacío de datos: no se sabe cuántos entrenadores hay certificados por nivel ni dónde (PQ-A05) — impide medir si "hay suficiente capacidad instalada" (S-01 del registro de supuestos) para este pilar específico.
2. La certificación no es condición para entrenar en la mayoría del sistema de fuerzas básicas/academias — solo es obligatoria en la cúspide (PRO en Liga MX).
3. El estándar de "academia certificada" no define públicamente si incluye licenciamiento del cuerpo técnico (PQ-A07) — riesgo de que la certificación de academias sea, en la práctica, una certificación de instalaciones o de proceso administrativo, no de calidad de enseñanza.
4. La recertificación es solo temporal (cada 3 años) sin componente de evaluación práctica de habilidades documentado.
5. No existe una vía formal, acreditada y de bajo costo de especialización para directores deportivos, scouts, analistas, psicólogos o nutriólogos dentro del sistema FMF — la oferta existe (universidades) pero no está integrada al ecosistema de licencias.
6. No hay evidencia de un mecanismo de mentoría formal entre entrenadores certificados de alto nivel y entrenadores comunitarios/de academias pequeñas.
7. No hay evidencia de un requisito de verificación de antecedentes o código de conducta ligado a la licencia, en un contexto donde la línea base jurídica ya documenta el vacío de protección de menores como el más urgente del proyecto.
8. No hay evidencia de cuota, meta o mecanismo específico para cerrar la brecha de recursos de formación entre entrenadores y entrenadoras.
9. La formación arbitral y la formación de entrenadores parecen operar como sistemas paralelos, sin infraestructura compartida documentada — riesgo de duplicidad de esfuerzo administrativo.

---

## 11. Alternativa de mejora

Reformar (no sustituir) la pirámide D→C→B→A→PRO en cuatro puntos concretos: (a) hacerla obligatoria —no solo aspiracional— para el cuerpo técnico de toda academia que use el sello "academia certificada de la FMF"; (b) agregar un componente de evaluación práctica (no solo asistencia a horas) a la recertificación trienal ya existente; (c) publicar, como obligación de transparencia y no como proyecto nuevo, el número de personas certificadas por nivel y por estado, dato que la FMF ya debe tener internamente para poder emitir las licencias; (d) incorporar verificación de antecedentes y un código de conducta como requisito de emisión/renovación de cualquier nivel de licencia, aprovechando el marco legal ya existente (Ley General de NNA, SIPINNA) sin necesidad de una ley nueva.

## 12. Alternativa de integración

- Integrar el registro interno de licencias de la FMF (que debe existir para poder emitir y renovar licencias) con la arquitectura de identificador único de jugador/entrenador que diseñe el Agente 10 (Pilar 9, Datos y scouting) — **un solo registro interoperable**, no un sistema de datos nuevo para entrenadores y otro para jugadores. Esta es la respuesta directa al vacío de PQ-A05: no se propone construir un sistema nuevo de conteo, se propone que el sistema que ya emite las licencias publique y comparta lo que ya administra.
- Integrar la currícula técnica nacional (siguiendo el patrón de Bélgica y de Japón/Australia, documentado en el benchmark consolidado, sección 3, punto 3: "aplicable con adaptación... puede integrarse a los estándares ya existentes de licencias de entrenador D→PRO... en vez de crearse desde cero") **dentro** de los planes de estudio de cada nivel D-PRO, no como instituto aparte.
- Integrar la certificación de licencia mínima como criterio explícito y auditado del estándar de "academia certificada" (hoy indefinido, PQ-A07), cerrando así dos vacíos con una sola reforma administrativa.
- Integrar las vías de especialización (psicología, nutrición, análisis de datos, dirección deportiva) con la oferta universitaria ya acreditada de CONDDE/CONADEIP y universidades públicas/privadas, mediante convenios de equivalencia, en vez de que la FMF cree su propia oferta académica de posgrado.
- Integrar la formación arbitral a la misma plataforma digital de formación/recertificación que se escale para entrenadores (una sola infraestructura tecnológica compartida, con currículas distintas).
- Integrar el rol de scout/observador de talento a la red de scouting escolar/comunitario ya operando (11,000+ observados/año), certificando a quienes ya cumplen esa función informalmente en vez de crear un cuerpo de scouts aparte.

## 13. Alternativa de escalamiento

Recomendaciones concretas (numeradas para trazabilidad con la sección 16), clasificadas explícitamente por categoría de la jerarquía de intervención (sección 2 del manual metodológico):

| # | Recomendación | Categoría de intervención |
|---|---|---|
| 1 | Publicar el registro de entrenadores certificados por nivel y por estado que la FMF ya administra internamente | 1. Aprovechar |
| 2 | Vincular ese registro con la arquitectura de identificador único que diseñe el Agente 10 | 3. Integrar |
| 3 | Exigir licencia mínima D vigente del cuerpo técnico como criterio de auditoría de "academia certificada" | 2. Corregir |
| 4 | Escalar la Licencia D a modalidad digital/híbrida de bajo costo y baja conectividad sobre el portal ya existente | 4. Escalar |
| 5 | Beca/subsidio de arancel para Licencia D/C dirigida a entrenadores comunitarios, financiada redirigiendo un % ya presupuestado de fondos FIFA Forward/FMF de formación | 5. Redistribuir |
| 6 | Cuota mínima (piso, no techo) de mujeres en becas y en el cuerpo de mentores regionales | 5. Redistribuir |
| 7 | Extender gradualmente el requisito de licencia PRO del director técnico titular a todo el cuerpo técnico de Liga MX/Expansión (asistentes, preparador físico), siguiendo el patrón coreano de extensión gradual K1→K3 | 6. Cambiar reglas |
| 8 | Agregar evaluación práctica obligatoria a la recertificación trienal ya existente | 6. Cambiar reglas |
| 9 | Integrar una currícula técnica nacional dentro de los planes D→PRO ya existentes (patrón Bélgica/Japón/Australia) | 3. Integrar |
| 10 | Cuerpo de "entrenadores mentores" regionales (uno por asociación estatal o agrupación de estados), asignados por la FMF a academias certificadas y clubes de Liga Premier/TDP, con personal A/PRO ya existente | 3. Integrar / 4. Escalar |
| 11 | Reconocer diplomados/maestrías universitarias (CONDDE/CONADEIP, UNAM, IPN, y otras) como vía acreditada de especialización para psicólogos, nutriólogos, analistas y directores deportivos | 3. Integrar |
| 12 | Certificar como "scout FMF" a observadores ya activos en la red de 28,000 escuelas, con un módulo breve de acreditación | 4. Escalar |
| 13 | Requisito de verificación de antecedentes y código de conducta para emisión/renovación de cualquier licencia, apoyado en el marco legal ya existente (LGNNA/SIPINNA), sin ley nueva | 6. Cambiar reglas / 3. Integrar |
| 14 | Incluir a los árbitros en la misma infraestructura digital de formación y recertificación que se escale para entrenadores | 3. Integrar |
| 15 | Incentivo "entrenador de casa": puntaje o beneficio en el proceso de licenciamiento de clubes para quienes retengan y asciendan a entrenadores certificados formados en su propia cantera (adaptación del principio Homegrown/allocation money de la MLS, ya identificado como el elemento más transferible del benchmark completo) | 6. Cambiar reglas |
| 16 | Redirigir prioritariamente becas y mentorías hacia estados/regiones de menor densidad de academias certificadas, una vez que el registro (recomendación 1-2) permita identificarlas | 5. Redistribuir |
| 17 | **Ruta Comunitaria**: sub-modalidad de bajo costo y bajo umbral de acceso de la Licencia D, con brigadas móviles y evaluación simplificada, para entrenadores hoy fuera del sistema (Liga TDP, ligas municipales, zonas rurales) | 7. Crear complementario — requiere 14 preguntas (sección 15) |
| 18 | **Beca Nacional de Formación Técnica y Científica**: línea presupuestal etiquetada dentro del presupuesto ya existente de Formación Académica de la FMF, para becas de licencia y especialización | 7. Crear complementario — requiere 14 preguntas (sección 15) |
| 19 | Meta cuantitativa obligatoria de densidad de entrenadores certificados por cada 1,000 jugadores, por nivel de licencia, como indicador de política pública (sección 23) | 6. Cambiar reglas |
| 20 | Mecanismo de verificación externa (auditor deportivo independiente o convenio con una institución de educación superior) sobre la calidad real de la certificación de academias y de licencias, para evitar una "reforma de papel" (riesgo ya señalado por el Agente 5B) | 3. Integrar (usa capacidad de auditoría externa ya existente en el ecosistema educativo/de acreditación, no crea un organismo nuevo) |

**Verificación de la regla del 70%:** de las 20 recomendaciones, 18 (90%) caen en las categorías 1 a 6; únicamente las recomendaciones 17 y 18 (10%) requieren capacidad complementaria nueva, y ambas responden las 14 preguntas de justificación en la sección 15.

## 14. Alternativa de sustitución

No se identifica ningún activo existente que deba sustituirse por completo. La pirámide D→C→B→A→PRO, el portal de Formación Académica, la red de academias certificadas y la red de scouting escolar se conservan y se refuerzan; ninguna recomendación de este entregable elimina una institución o programa ya operando. Esto es consistente con el hallazgo transversal del benchmark completo: ningún país estudiado resolvió su problema de formación de entrenadores sustituyendo a su federación (`08-fase4-benchmark-consolidado.md`, sección 4).

## 15. Necesidad de nueva capacidad

Dos elementos de la sección 13 (recomendaciones 17 y 18) se clasifican como capacidad complementaria nueva y requieren, por instrucción de la sección 2.1 del manual metodológico, responder las 14 preguntas de justificación antes de pasar el Control 4.

### 15.1 "Ruta Comunitaria" (sub-modalidad de bajo costo de la Licencia D)

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Qué capacidad existe hoy que cubre esta función? | La Licencia D existente (20 horas/1 mes), pero en su formato actual no está documentado que llegue a entrenadores de ligas municipales, TDP o zonas rurales sin acceso a sedes de capacitación urbanas. |
| 2 | ¿Quién la controla hoy? | La FMF, vía Formación Académica/ENDIT. |
| 3 | ¿Por qué no cumple su función? | No hay evidencia de que la Licencia D actual tenga una modalidad de bajo costo, baja conectividad y evaluación itinerante — el formato documentado parece requerir asistencia presencial u online estándar. |
| 4 | ¿Por qué no puede reformarse en lugar de sustituirse? | Sí puede y debe reformarse: la "Ruta Comunitaria" **no sustituye** la Licencia D, es una modalidad de entrega adicional del mismo nivel D, con el mismo contenido mínimo y el mismo certificado — se trata como capacidad complementaria (no institución nueva) precisamente porque conserva el título y el nivel existentes; solo añade un canal de acceso. |
| 5 | ¿Cuánto costaría reformarla (modalidad estándar existente)? | No hay dato público del costo actual de emitir una Licencia D; se estima bajo (curso de 20 horas), pero sin escalamiento a brigadas móviles no llegaría a zonas sin sede fija. |
| 6 | ¿Cuánto costaría la modalidad complementaria (brigadas + digital offline)? | Orden de magnitud estimado en la sección 18 (confianza C-D); requiere afinarse por el Agente 14. |
| 7 | ¿Qué funciones asumiría? | Certificación de nivel D para entrenadores comunitarios/rurales/de ligas amateur hoy fuera del alcance práctico del sistema. |
| 8 | ¿Qué institución dejaría de cumplir esas funciones? | Ninguna — no reemplaza a nadie; hoy nadie certifica a esta población. |
| 9 | ¿Cómo se evitaría la duplicidad? | Mismo currículo, mismo registro (recomendación 1-2), mismo certificado D; solo cambia el canal de entrega (brigada móvil/offline vs. sede fija/online estándar). |
| 10 | ¿Cómo se financiaría de forma permanente? | Redirección de un porcentaje ya presupuestado de fondos FIFA Forward/FMF de formación (recomendación 5), no un impuesto ni fondo nuevo. |
| 11 | ¿Cómo se evaluaría? | Número de licencias D emitidas por esta vía por estado/año; tasa de aprobación de la evaluación práctica; densidad resultante por región (indicador de la sección 23). |
| 12 | ¿Quién la supervisaría? | La misma Dirección de Formación Académica/ENDIT de la FMF, con el mecanismo de auditoría externa de la recomendación 20. |
| 13 | ¿Bajo qué condiciones podría cerrarse? | Si la modalidad estándar de la Licencia D logra cobertura territorial equivalente sin brigadas dedicadas, o si la auditoría externa detecta una tasa de aprobación no comparable a la modalidad estándar (señal de certificación de menor calidad). |
| 14 | ¿Qué riesgo tiene de ser capturada por intereses particulares? | Riesgo medio: que la brigada se use como vehículo de clientelismo político-deportivo estatal/municipal. Mitigación: evaluación y certificado emitidos centralmente por la FMF, no por autoridades locales; auditoría externa obligatoria (recomendación 20). |

### 15.2 "Beca Nacional de Formación Técnica y Científica"

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Qué capacidad existe hoy que cubre esta función? | El presupuesto de Formación Académica de la FMF y los fondos FIFA Forward ya destinados a formación (evidenciados en la renovación del CAR, 390 millones de pesos, con participación FMF+FIFA Forward). No hay evidencia de que hoy exista una línea etiquetada específicamente para becas individuales de licencia/especialización. |
| 2 | ¿Quién la controla hoy? | La FMF (Formación Académica) y, en su componente FIFA Forward, la propia FIFA junto con la FMF como receptor. |
| 3 | ¿Por qué no cumple su función? | Porque no hay evidencia de que una parte de ese presupuesto esté explícitamente reservada y etiquetada para subsidiar el costo de licencia/especialización de entrenadores comunitarios, entrenadoras y personal de ciencia del deporte de bajos recursos. |
| 4 | ¿Por qué no puede reformarse en lugar de crearse? | Se diseña deliberadamente como una **reasignación etiquetada** dentro del presupuesto ya existente de Formación Académica, no como una entidad legal nueva, un fideicomiso nuevo ni un organismo con gobierno propio — se incluye en esta sección por precaución metodológica (la sección 2.1 exige responder las 14 preguntas para cualquier "fondo" nuevo, y una línea presupuestal etiquetada puede leerse como tal), pero su diseño concreto es de categoría 5 (redistribuir), no 7 (crear). |
| 5 | ¿Cuánto costaría reformar el presupuesto existente para etiquetar esta línea? | Bajo — es una decisión administrativa de reasignación, no de captación de nuevos recursos; costo de implementación administrativa estimado bajo (confianza D, sin cifra base). |
| 6 | ¿Cuánto costaría crear un vehículo financiero nuevo (fideicomiso u organismo aparte)? | No se recomienda esta vía — implicaría gobernanza, auditoría y costo de operación adicionales sin necesidad, y elevaría el riesgo de captura documentado en el benchmark (caso Mamić, Croacia). |
| 7 | ¿Qué funciones asumiría? | Subsidiar el costo de matrícula/evaluación de Licencia D/C para entrenadores comunitarios y entrenadoras de bajos recursos, y de diplomados de especialización (psicología, nutrición, análisis de datos, dirección deportiva) para personal ya activo en el sistema. |
| 8 | ¿Qué institución dejaría de cumplir esas funciones? | Ninguna — hoy nadie subsidia explícitamente este costo; las familias/entrenadores lo cubren de su bolsillo (o no acceden). |
| 9 | ¿Cómo se evitaría la duplicidad? | Administrada por la misma Dirección de Formación Académica que ya gestiona las licencias; no crea una segunda ventanilla. |
| 10 | ¿Cómo se financiaría de forma permanente? | Porcentaje fijo y públicamente reportado de los fondos FIFA Forward/FMF ya destinados a formación (no depende de presupuesto público federal/estatal, evitando cualquier riesgo de injerencia gubernamental según la decisión D-03 de la línea base). |
| 11 | ¿Cómo se evaluaría? | Número de becas otorgadas por año, por estado, por género; tasa de aprobación de los becarios; costo por becario vs. presupuesto total de formación (transparencia obligatoria). |
| 12 | ¿Quién la supervisaría? | La propia FMF, con reporte anual público (recomendación 1) y el mecanismo de auditoría externa de la recomendación 20. |
| 13 | ¿Bajo qué condiciones podría cerrarse? | Si el registro (recomendación 1-2) muestra que la brecha de acceso económico a la licencia ya no es una barrera relevante, o si la auditoría externa detecta uso indebido de los fondos. |
| 14 | ¿Qué riesgo tiene de ser capturada por intereses particulares? | Riesgo medio-alto, dado el patrón de opacidad financiera y personalización del poder ya documentado en la línea base (Bloque B): sin reporte público anual y auditoría externa, podría convertirse en un mecanismo de favoritismo hacia academias/clubes afines a la dirigencia en turno. Mitigación: reporte público anual obligatorio (recomendación 1) y auditoría externa (recomendación 20) como condiciones no negociables de operación, siguiendo la advertencia expresa del Agente 5B sobre el riesgo de captura de cualquier fondo dedicado inspirado en modelos internacionales. |

---

## 16. Recomendación

Priorización en tres horizontes, todas trazables a la numeración de la sección 13:

**Corto plazo (0-4 años) — bajo costo, no depende de resolver gobernanza primero:**
1. Publicar el registro de licencias existente (recomendación 1).
2. Vincular ese registro con el identificador único del Agente 10 (recomendación 2).
3. Exigir licencia mínima D del cuerpo técnico como criterio de "academia certificada" (recomendación 3).
4. Escalar la Licencia D a modalidad digital/híbrida (recomendación 4) y lanzar la Ruta Comunitaria (recomendación 17).
5. Requisito de verificación de antecedentes/código de conducta (recomendación 13).
6. Evaluación práctica obligatoria en la recertificación (recomendación 8).

**Mediano plazo (4-8 años) — requiere el registro y la auditoría del corto plazo funcionando:**
7. Beca Nacional de Formación Técnica y Científica, con cuota de género (recomendaciones 5, 6, 18).
8. Cuerpo de entrenadores mentores regionales (recomendación 10).
9. Currícula técnica nacional integrada a D-PRO (recomendación 9).
10. Certificación de scouts activos (recomendación 12) y reconocimiento de diplomados universitarios para especialización (recomendación 11).
11. Extensión gradual de licencia mínima al cuerpo técnico completo de Liga MX/Expansión (recomendación 7).
12. Incentivo "entrenador de casa" en el licenciamiento de clubes (recomendación 15).

**Largo plazo (8-20 años) — depende de que el mediano plazo produzca datos confiables:**
13. Redistribución territorial de becas/mentorías basada en el mapa de densidad ya medible (recomendación 16).
14. Metas de densidad certificadas por cada 1,000 jugadores como indicador nacional consolidado (recomendación 19, sección 23).
15. Integración plena de árbitros a la infraestructura digital compartida (recomendación 14).

## 17. Responsable

FMF — Dirección de Formación Académica / ENDIT (recomendaciones de licenciamiento, currícula, becas, mentoría, recertificación); Comisión de Certificación de Academias de la FMF (vínculo licencia-certificación de academia, recomendación 3); Agente 10 (arquitectura de datos e identificador único, recomendaciones 1-2); CONDDE/CONADEIP y universidades públicas/privadas (oferta de especialización, recomendación 11, vía convenio); Comisión Arbitral de la FMF (integración de infraestructura digital, recomendación 14); una institución de educación superior o auditor deportivo independiente por convenio (mecanismo de verificación externa, recomendación 20) — no un organismo público nuevo, para evitar el riesgo de injerencia ya señalado en la línea base (`05`, Bloque C, decisión D-03).

## 18. Costo

**[ESTIMACIÓN, confianza C-D — no hay cifra base pública para calibrar ninguno de estos montos; órdenes de magnitud ilustrativos, a afinar por el Agente 14 en Fase 7]:**

| Componente | Orden de magnitud estimado | Base del cálculo |
|---|---|---|
| Escalamiento digital/híbrido de Licencia D + Ruta Comunitaria (desarrollo y operación, año 1-4) | $5–15 millones de pesos, una vez, más operación anual menor | Aprovecha el portal ya existente (`formacionacademica.fmf.mx`); no se construye plataforma desde cero |
| Becas de Licencia D/C (10,000 becarios/año estimados, costo unitario estimado $1,500–3,000 pesos/becario) | $15–30 millones de pesos/año | Estimación por analogía con costos de capacitación vocacional de corta duración en México; sin cifra oficial FMF del costo real de emisión de licencia |
| Cuerpo de entrenadores mentores regionales (30-40 mentores nacionales, salario+viáticos) | $16–22 millones de pesos/año | Analogía con el modelo danés de "Talent Coaches" (6 para un país de ~6 millones de habitantes), escalado de forma no literal a la escala y organización territorial mexicana (33 asociaciones estatales) |
| Becas de especialización (psicología, nutrición, análisis, dirección deportiva) vía convenios universitarios | $10–20 millones de pesos/año | Costo estimado de matrícula parcial subsidiada en diplomados/posgrados ya existentes, no de programas nuevos |
| Auditoría externa anual (recomendación 20) | $3–6 millones de pesos/año | Honorarios de auditor/institución independiente, orden de magnitud comparable a auditorías sectoriales de tamaño medio en México |
| **Total estimado, años 1-4** | **~$50–90 millones de pesos/año** | Referencia de escala: menor al costo de una sola renovación de infraestructura ya realizada (CAR, 390 millones de pesos) y muy por debajo del rango de ingresos anuales de Liga MX (600-900 millones de USD/año, según línea base) |

Ningún monto de esta tabla requiere presupuesto público nuevo: se financia redirigiendo fondos FIFA Forward/FMF de formación ya existentes (dependencia explícita: transparencia financiera mínima de la FMF, hoy no verificada — riesgo ya documentado en la línea base, Bloque D).

## 19. Tiempo

- **Año 1-2:** publicación del registro existente, diseño de la modalidad digital/híbrida y de la Ruta Comunitaria, primeras auditorías de "academia certificada" con criterio de licencia mínima.
- **Año 4:** primera meta de densidad medible con datos propios (ver sección 23); primeras becas y mentores regionales operando.
- **Año 8:** extensión gradual de licencia mínima al cuerpo técnico completo de clubes profesionales; currícula técnica nacional plenamente integrada a los cinco niveles.
- **Año 12-20:** metas de densidad de "certificación masiva" adaptada (ver sección 23); resultado estructural profundo, en línea con el patrón temporal documentado en el benchmark (Japón: 25-30 años para exportación sistemática; Islandia: 14-16 años para primer resultado internacional mayor) — este pilar no debe prometer resultados de selección mayor antes de una década, aunque sí señales tempranas de cobertura de licenciamiento en 4 años.

## 20. Dependencias

1. Resolución de la relación de gobernanza FMF-Liga MX post-separación de abril de 2026 (`05`) — sin claridad sobre quién administra el licenciamiento de clubes, la recomendación 7 (extensión del requisito PRO al cuerpo técnico completo) no tiene un responsable único claro.
2. Transparencia financiera mínima de la FMF sobre los fondos FIFA Forward/de formación ya existentes, para poder redirigir un porcentaje de forma auditable (recomendaciones 5, 18) sin repetir el patrón de opacidad ya documentado.
3. Que el Agente 10 (Pilar 9) efectivamente diseñe la arquitectura de identificador único de jugador/entrenador — este pilar depende de ese entregable para cerrar el vacío de PQ-A05 sin construir un sistema de datos paralelo.
4. Que la FMF confirme (no se pudo verificar en esta investigación) si ya existe internamente un registro de licencias emitidas, condición necesaria para que la recomendación 1 (publicarlo) sea de bajo costo y no un proyecto de levantamiento de datos desde cero.
5. Voluntad de la Asamblea de Dueños de Liga MX de no bloquear la extensión gradual de requisitos de licenciamiento (recomendación 7) — el actor de mayor poder de veto documentado en la línea base.

## 21. Riesgos

- **Riesgo de "reforma de papel"** (ya señalado por el Agente 5B para todo el benchmark de países pequeños): certificar sin fiscalizar produce licencias sin cambio real en la calidad de enseñanza. Mitigación: mecanismo de auditoría externa (recomendación 20) como condición no negociable de cualquier reforma de este pilar.
- **Riesgo de captura de la Beca Nacional** por actores ya beneficiados por la opacidad financiera documentada en la línea base (Bloque B/D). Mitigación: reporte público anual y auditoría externa obligatorios (ver sección 15.2, pregunta 14).
- **Riesgo de que la Asamblea de Dueños de Liga MX bloquee o diluya** la extensión del requisito de licencia al cuerpo técnico completo (recomendación 7), replicando el patrón ya documentado de "es más barato pagar la sanción que desarrollar" (regla de menores) y el patrón de flexibilización del J.League japonés en 1999.
- **Riesgo de que la certificación de entrenadores se use como sustituto, no complemento, de un canal de protección de menores independiente** — la crisis institucional de la KSÍ islandesa (2021, denuncias de violencia sexual/física) es la advertencia directa documentada en el benchmark: ningún sistema de licenciamiento de entrenadores reemplaza un canal de denuncia. Mitigación: la recomendación 13 (verificación de antecedentes/código de conducta) debe ir acompañada, a nivel de todo el proyecto, del convenio FMF-SIPINNA ya identificado como pendiente en la línea base jurídica (no diseñado por este agente, pero señalado como dependencia crítica).
- **Riesgo de comparación de escala engañosa**: usar la cifra islandesa de forma literal (per cápita) en vez de como principio, produciendo una meta inalcanzable o mal calibrada. Mitigación: las metas de la sección 23 se construyen como objetivos de política propios, no como escalamiento directo del dato islandés (cumpliendo la instrucción explícita de la misión de este agente).
- **Riesgo de que la brecha de género en formación (entrenadoras) no se cierre** si las cuotas de la recomendación 6 no tienen mecanismo de verificación — requiere coordinación con el Agente 13 (auditoría transversal).

## 22. Bloqueadores

- La Asamblea de Dueños de Liga MX, si percibe cualquier extensión del requisito de licenciamiento como un costo no compensado (mismo patrón documentado con la regla de menores).
- La ausencia actual de un registro de licencias públicamente verificable — si la FMF no lo tiene internamente sistematizado (no confirmado en esta investigación), la recomendación 1 dejaría de ser de bajo costo y se convertiría en un proyecto de levantamiento de datos desde cero, cambiando su clasificación de "aprovechar" a "crear".
- Opacidad financiera de la FMF sobre fondos FIFA Forward/de formación, que podría impedir verificar que el porcentaje redirigido a becas (recomendación 5, 18) efectivamente se ejecuta.
- Ausencia de un canal de denuncia de protección de menores independiente (vacío legal ya señalado como el más urgente del proyecto) — sin resolverlo, el requisito de código de conducta (recomendación 13) queda sin mecanismo de aplicación real.

## 23. Indicadores

### 23.1 Indicador central (responde PQ-P08): entrenadores certificados por cada 1,000 jugadores en el sistema estructurado

**Definición operativa mientras no exista un censo verificado de jugadores federados (dependencia de PQ-A06/Agente 10):** "jugadores en el sistema estructurado" = niños y jóvenes en academias certificadas + fuerzas básicas de clubes de todos los niveles (Liga MX a Liga TDP), usando como denominador provisional la cifra ya reportada de ~168,000 niños en academias certificadas (evidencia B, autorreportada) hasta que el Agente 10 entregue un censo auditado.

**[RECOMENDACIÓN, confianza C — metas de política, no extrapolación de una cifra base verificada, dado el vacío de PQ-A05]:**

| Nivel de licencia | Población de referencia | Meta año 4 | Meta año 8 | Meta año 20 | Base de la meta |
|---|---|---|---|---|---|
| D o superior (iniciación, 5-14 años) | Niños en academias certificadas + programas escolares estructurados | ≥15 por cada 1,000 | ≥40 por cada 1,000 | ≥90 por cada 1,000 | Principio de certificación masiva de Islandia (adaptado, no copiado); meta año 20 aproxima cobertura casi universal en el nivel de iniciación, sin replicar el ratio poblacional islandés (325-340x mayor) |
| B (fuerzas básicas competitivas, 13-17 años) | Jugadores en categorías competitivas de clubes/Liga Premier/TDP | ≥3 por cada 1,000 | ≥8 por cada 1,000 | ≥20 por cada 1,000 | Extrapolación conservadora de la estructura piramidal (menos entrenadores por jugador a medida que sube el nivel competitivo, patrón estándar de cualquier sistema de licenciamiento deportivo) |
| A (Liga Expansión/Premier, cuerpo técnico ampliado) | Jugadores en plantillas de este nivel | — | ≥4 por cada 1,000 | ≥10 por cada 1,000 | Mismo principio, ajustado al tamaño de plantilla profesional |
| PRO (Liga MX/Expansión/Selecciones) | Cuerpo técnico completo (no solo director técnico titular) | 100% del director técnico titular (ya vigente) | 100% del cuerpo técnico con al menos licencia A | Mayoría del cuerpo técnico con licencia PRO | Extensión gradual del requisito ya obligatorio para el titular, siguiendo el patrón coreano de extensión gradual K1→K3 |

**Nota de confianza obligatoria:** estas metas **no** son una escala directa del dato islandés de 728 entrenadores licenciados para ~380,000 habitantes (que es una razón poblacional, no de jugadores, y no convertible de forma confiable según la propia limitación declarada por el Agente 5B). Son metas de política pública construidas por este agente, con nivel de confianza C, que deben recalibrarse en cuanto: (a) el Agente 10 entregue un censo auditado de jugadores federados/en sistema estructurado, y (b) la recomendación 1 (publicar el registro de licencias existente) revele la cifra base real de entrenadores certificados, hoy desconocida (PQ-A05).

### 23.2 Otros indicadores

- Número de estados/asociaciones con al menos un entrenador mentor regional activo (fuente: FMF, frecuencia anual).
- Porcentaje de "academias certificadas" cuyo cuerpo técnico tiene licencia D vigente o superior, verificado por auditoría externa, no autorreportado (fuente: auditor independiente, frecuencia anual).
- Número de becas otorgadas por año, desagregadas por género, estado y nivel de licencia (fuente: FMF, frecuencia anual).
- Porcentaje de becarias mujeres respecto al total de becas otorgadas, contra la meta piso fijada en la recomendación 6 (fuente: FMF, frecuencia anual).
- Número de personas certificadas como scout FMF, psicólogo/nutriólogo/analista acreditado vía convenio universitario (fuente: FMF, frecuencia anual).
- Tasa de aprobación de la evaluación práctica en la recertificación trienal, por nivel (fuente: FMF/auditor externo, frecuencia trienal por cohorte).
- Confirmación binaria (sí/no, con fecha) de si la FMF ya tenía internamente sistematizado el registro de licencias antes de esta reforma (fuente: FMF, una vez, como verificación de la recomendación 1).

## 24. Casos internacionales

Cada referencia se cita con el país exacto y su clasificación de transferibilidad, según la regla fijada en el benchmark consolidado (`08`, sección 6):

- **Islandia — "aplicable con adaptación solo en el componente de certificación de entrenadores"** (`fase4-agente5b`, sección 25): fundamenta el principio de certificación obligatoria incluso a nivel comunitario/grassroots (recomendaciones 3, 13, 17), **no** la magnitud per cápita (325-340x de diferencia de escala con México).
- **Corea del Sur — "aplicable con adaptación", licencia condicionada aplicada sobre liga madura (2020, 37 años después de fundado el K League)** (`fase4-agente5e`, sección 25): fundamenta la recomendación 7 (extensión gradual del requisito de licencia al cuerpo técnico completo de una liga ya consolidada, el punto de partida más análogo al de México, más que el caso japonés de 1993).
- **Bélgica y Japón/Australia — "aplicable con adaptación", currícula técnica nacional integrada a licencias ya existentes** (`08-fase4-benchmark-consolidado.md`, sección 2, y `fase4-agente5e`, sección 25): fundamenta directamente la recomendación 9 y la instrucción explícita de la misión de este agente de no crear un instituto técnico aparte.
- **Dinamarca — "aplicable con adaptación", modelo de "Talent Coaches"** (`fase4-agente5b`, sección 12): fundamenta la recomendación 10 (cuerpo de entrenadores mentores regionales vinculados a academias/clubes, sin crear institución paralela).
- **Estados Unidos — "aplicable con adaptación", Homegrown Player Rule/allocation money** (`08-fase4-benchmark-consolidado.md`, sección 3, elemento más transferible del benchmark completo): fundamenta la recomendación 15, adaptada de jugadores a entrenadores ("entrenador de casa").
- **Australia — "aplicable directamente como criterio de diagnóstico"** (`fase4-agente5e`, matriz de transferibilidad): la advertencia de que el crecimiento de la base sin currícula y licenciamiento vinculados no produce élite (caída de minutos europeos pese a duplicar participación juvenil, 1997-2017) se usa como criterio obligatorio de diseño: las +2,000 academias mexicanas no bastan por sí solas sin la reforma de licenciamiento de este pilar.
- **Croacia — "no recomendable sin salvaguardas explícitas"** (`fase4-agente5b`, sección 25): advertencia directa contra concentrar el cuerpo de mentores o la administración de becas en pocas manos sin contrapesos, dado el patrón de personalización del poder ya documentado en la línea base mexicana (caso Mamić como advertencia, no como modelo).
- **Uruguay — "aplicable con adaptación", continuidad metodológica juvenil-mayor** (`fase4-agente5b`, sección 25): relevante como principio de coherencia curricular entre niveles de licencia (un entrenador certificado en la Ruta Comunitaria debe compartir principios metodológicos con el nivel PRO), aunque el diseño de continuidad de selecciones en sí corresponde al Agente 11.
- **Noruega — "aplicable con adaptación menor" en el componente de reglamento (no tablas de posición antes de los 13 años)** (`fase4-agente5b`, sección 25): relevante para el contenido de la currícula técnica nacional integrada (recomendación 9), no como elemento de financiamiento (esa parte del caso noruego se clasifica "difícil de aplicar").

## 25. Adaptación a México

- **De Islandia:** se adopta la obligatoriedad de certificación incluso a nivel comunitario/grassroots; se descarta la lógica de "conocer a cada niño personalmente" y la cifra per cápita, reemplazándolas por metas propias basadas en la población de jugadores en el sistema estructurado (sección 23), con nivel de confianza C explícito.
- **De Corea del Sur:** se adopta el patrón de imposición gradual sobre una liga ya madura (más realista que el japonés de 1993), ajustado a que en México la relación FMF-Liga MX está fragmentada desde abril de 2026 — la extensión del requisito de licencia requiere primero claridad sobre quién administra el licenciamiento de clubes (dependencia 1).
- **De Bélgica/Japón/Australia:** se adopta la currícula nacional integrada a las licencias existentes; se descarta cualquier vehículo de financiamiento por lotería estatal (Japón) o comité de revisión de gobernanza por mandato gubernamental directo (Australia, Crawford Report), ambos clasificados "difícil de aplicar" por el riesgo de injerencia FIFA ya documentado en la línea base.
- **De Dinamarca:** se adopta el número reducido de mentores vinculados directamente a clubes/academias (no una estructura burocrática grande), escalado de 6 (Dinamarca, ~6 millones de habitantes) a un rango de 30-40 (México, 33 asociaciones estatales) — escalamiento por unidad territorial de gobernanza (asociaciones estatales), no por población, dado que la población no es la variable relevante para este mecanismo.
- **De Estados Unidos (MLS):** se adopta el principio de incentivo positivo (premiar, no solo sancionar) aplicado a la formación de entrenadores, coherente con el hallazgo transversal de la línea base económica de que el sistema mexicano hoy castiga sin premiar la formación de jugadores (`05`, Bloque D) — se extiende la misma lógica al capital humano técnico.
- **De Australia:** se adopta la advertencia empírica como filtro de diseño obligatorio, no como práctica a copiar: cualquier expansión de la red de academias certificadas debe ir acompañada, no sustituida, por la reforma de licenciamiento de este pilar.

---

## 26. Preguntas pendientes

Ver sección "Preguntas nuevas para el registro maestro" a continuación, que consolida las preguntas identificadas a lo largo de este entregable que no pudieron resolverse con la información disponible.

---

## Preguntas nuevas para el registro maestro

| ID propuesto | Pregunta | Fuente esperada | Estado |
|---|---|---|---|
| PQ-8-01 | ¿Existe hoy, internamente en la FMF (Formación Académica/ENDIT), un registro sistematizado de licencias emitidas por nivel y por estado, aunque no sea público? | FMF, Formación Académica/ENDIT | Pendiente — condiciona si la recomendación 1 de este entregable es de bajo costo ("publicar lo que ya existe") o de alto costo ("levantar el dato desde cero") |
| PQ-8-02 | ¿Qué costo real tiene hoy, para un aspirante, obtener cada nivel de licencia (D, C, B, A, PRO): matrícula, materiales, evaluación, desplazamiento? | FMF, aspirantes/egresados de los cursos | Pendiente |
| PQ-8-03 | ¿Qué porcentaje del presupuesto de Formación Académica de la FMF proviene de fondos FIFA Forward, y qué porcentaje de ese monto se destina hoy a licenciamiento de entrenadores frente a otros rubros (infraestructura, selecciones, otros)? | FMF, informes FIFA Forward | Pendiente |
| PQ-8-04 | ¿Qué proporción de mujeres tiene hoy cada nivel de licencia (D a PRO), y existe alguna barrera de acceso documentada distinta a la de los hombres? | FMF, Formación Académica | Pendiente |
| PQ-8-05 | ¿La certificación actual de "academia certificada" (+2,000 reportadas) incluye ya, de facto, algún requisito de licencia mínima del cuerpo técnico, aunque no esté publicado como criterio? | FMF, Certificación de Academias | Pendiente — insumo directo para saber si la recomendación 3 es una reforma o una formalización de una práctica ya existente |
| PQ-8-06 | ¿Existe ya un mecanismo interno de verificación de antecedentes penales o de conducta para quienes solicitan una licencia de entrenador en México? | FMF, Formación Académica | Pendiente |
| PQ-8-07 | ¿Qué convenios, si existen, tiene hoy la FMF con universidades (UNAM, IPN, u otras vía CONDDE/CONADEIP) para reconocer diplomados o posgrados en ciencias del deporte, psicología o nutrición como equivalencia dentro del sistema de licencias? | FMF, CONDDE, CONADEIP, universidades | Pendiente |
| PQ-8-08 | ¿Qué avance real tiene el proceso de aval de Concacaf y de búsqueda de equivalencia UEFA de la pirámide D-C-B-A-PRO anunciado en 2025? | FMF, Concacaf | Pendiente |
| PQ-8-09 | ¿Existe hoy alguna estructura formal de formación o certificación para directores deportivos y analistas de datos dentro de clubes mexicanos, o esta función se ejerce sin credencial específica? | Clubes de Liga MX/Expansión, FMF | Pendiente |
| PQ-8-10 | ¿Qué relación formal, si alguna, existe entre la Comisión Arbitral de la FMF y la Dirección de Formación Académica, en términos de infraestructura de formación compartida? | FMF | Pendiente |

---

## Supuestos y riesgos nuevos identificados

### Supuestos nuevos

| ID | Supuesto | Justificación | Sensibilidad | Consecuencia si es falso | Validación requerida |
|---|---|---|---|---|---|
| S-15 | La FMF ya administra internamente, aunque no lo publique, un registro de quién tiene cada nivel de licencia vigente (porque necesita saberlo para emitir/renovar licencias) | Inferencia razonable de cómo opera cualquier sistema de licenciamiento con vigencia trienal | Alta — si es falso, la recomendación 1 (publicar el registro existente) se convierte en un proyecto de levantamiento de datos desde cero, cambiando de categoría 1 (aprovechar) a categoría 7-8 (crear) | Confirmar directamente con FMF (PQ-8-01) antes de que el Agente 10 diseñe la integración (recomendación 2) |
| S-16 | Redirigir un porcentaje ya presupuestado de fondos FIFA Forward/FMF de formación hacia becas de licencia (recomendaciones 5, 18) es viable sin requerir aprobación de un nuevo donante o de FIFA | Se basa en que el CAR ya fue renovado con fondos FIFA Forward + FMF sin mecanismo nuevo aparente | Media — si FIFA Forward tiene reglas de uso restringidas a ciertos rubros (infraestructura, no becas individuales), la fuente de financiamiento propuesta no sería viable tal como está diseñada | Verificar con la FMF/FIFA Forward las reglas de elegibilidad del fondo antes de que el Agente 14 costee esta recomendación en Fase 7 |
| S-17 | El "sistema estructurado" (academias certificadas + fuerzas básicas de clubes, ~168,000 niños reportados) es una aproximación razonable del universo real de jugadores que este pilar debe cubrir, mientras no exista el censo del Agente 10 | Es la única cifra de denominador disponible en la línea base, aunque autorreportada y sin auditoría (S-06 ya registrado) | Alta — si el universo real es mucho mayor (por ejemplo, si se incluyen los 1.13 millones de estudiantes del programa de scouting escolar, no solo los 168,000 de academias), todas las metas de densidad de la sección 23 estarían calculadas sobre un denominador equivocado, requiriendo recalibración completa | Recalibrar en cuanto el Agente 10 entregue una definición y un censo auditado de "jugador en el sistema estructurado" |

### Riesgos nuevos

| Riesgo | Probabilidad | Impacto | Señal temprana | Responsable | Mitigación | Contingencia |
|---|---|---|---|---|---|---|
| Que la meta de densidad de entrenadores certificados (sección 23) se cite en fases posteriores (Fase 7, presupuesto; Fase 9, síntesis) como si fuera una cifra verificada, y no una meta de política con confianza C construida a falta de dato base | Media | Alto — erosiona la credibilidad de todo el pilar si se presenta como hecho | Uso de la cifra en documentos posteriores sin la etiqueta de confianza C ni la nota de la sección 23.1 | Agente 0 (integración Fase 6), Agente 17 (síntesis final) | Exigir que cualquier cita de esta meta en fases posteriores incluya explícitamente su nivel de confianza y la dependencia de PQ-A05/censo del Agente 10 | Corregir en el Control 5 (síntesis) si se detecta uso indebido |
| Que la Beca Nacional de Formación Técnica y Científica (recomendación 18) se implemente sin el reporte público anual ni la auditoría externa que este entregable fija como condición no negociable, replicando el patrón de opacidad ya documentado en la línea base (Bloque D) | Media-Alta | Alto | Ausencia de reporte público en el primer año de operación de la beca | Agente 0, Agente 16 (Red Team) | Bloquear el paso del Control 4 de esta recomendación específica si el diseño final (Fase 7) no incluye el mecanismo de reporte/auditoría | Suspender la línea presupuestal hasta que se implemente el reporte |
| Que la extensión gradual del requisito de licencia al cuerpo técnico completo de Liga MX/Expansión (recomendación 7) sea bloqueada o diluida por la Asamblea de Dueños de Liga MX, replicando el patrón ya documentado con la regla de menores (más barato pagar/incumplir que desarrollar) y la flexibilización del J.League en 1999 | Alta | Medio-Alto — no elimina el resto del pilar, pero deja sin efecto su componente de mayor impacto en el profesionalismo | Ausencia de avance en el reglamento de licenciamiento de clubes tras el primer ciclo de negociación | Agente 2 (gobernanza), Agente 15 (implementación) | Diseñar la extensión de forma gradual y por categoría (siguiendo el patrón coreano K1→K3), no como imposición única, para reducir el costo político de aceptarla de una sola vez | Si se bloquea, mantener el resto del pilar (licencias comunitarias, becas, mentoría, currícula) operando de forma independiente, ya que no dependen de la aprobación de la Asamblea de Dueños |
| Que la certificación de scouts, analistas, directores deportivos y personal de ciencia del deporte se perciba como una carga administrativa sin beneficio claro para clubes pequeños (Liga Premier/TDP), generando baja adopción voluntaria | Media | Medio | Baja tasa de inscripción en los módulos de acreditación de la recomendación 11-12 en su primer ciclo | FMF, Formación Académica | Vincular la acreditación a un beneficio tangible (acceso a la red de mentores, prioridad en becas, reconocimiento en el proceso de certificación de academias) en vez de hacerla puramente obligatoria desde el inicio | Revisar el diseño de incentivos si la adopción es baja tras el primer ciclo, antes de considerar hacerla obligatoria |
