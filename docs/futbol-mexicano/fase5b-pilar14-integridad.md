# Fase 5 (ronda de cierre, post Fase 5-7) — Pilar 14: Integridad
## Diseño del mecanismo operativo de integridad del fútbol mexicano

**Fecha de entrega:** 2026-07-25.
**Motivo de esta ronda:** el prompt maestro original no asignó agente de diseño propio al Pilar 14 en la Fase 5 (vacío señalado en `09-fase6-integracion-preliminar-diseno.md`, sección 8, junto con los Pilares 1, 2, 6 y 7). Esta ronda cierra ese vacío específico para Integridad, ejecutándose después de las Fases 5-7, en paralelo con las rondas de cierre de Gobernanza (Pilar 1) y Marco jurídico (Pilar 2), que este documento no puede leer todavía (se entregan en paralelo) y con las que deberá reconciliarse en la próxima integración del Agente 0.
**Insumos recibidos:** `00-agente0-metodologia-y-plan.md`, `02-plantilla-entregable.md`, `fase2-agente3-derecho-y-regulacion.md`, `fase2-agente2-gobernanza-y-poder.md`, `07-registro-decisiones.md` (criterio D-03), y de forma auxiliar `fase7-agente14-finanzas.md` (riesgo transversal de opacidad financiera) y `04-registro-supuestos-riesgos.md`.
**Alcance de este documento:** diseña el mecanismo **operativo** de integridad (cómo se investiga, quién sanciona, quién audita, quién protege al denunciante), no el instrumento legal de fondo. La eventual formalización del convenio FMF-SIPINNA como instrumento legal para protección de menores es responsabilidad del Pilar 2 (Marco jurídico), según instrucción explícita de esta misión; este documento **asume** que ese convenio existe como base legal y diseña el mecanismo de integridad que opera sobre él (investigación de casos, protección del denunciante, sanciones a academias). No presupuesta (eso es Fase 7, Agente 14, ya entregado) ni calendariza en detalle (Fase 7, Agente 15, ya entregado); donde ya existen partidas relevantes en `fase7-agente14-finanzas.md`, se referencian, no se recalculan.
**Restricción obligatoria aplicada en todo el documento:** criterio D-03 del registro de decisiones — leyes/mecanismos generales de aplicación neutral (competencia económica, fiscal, datos personales, derechos de la niñez, trabajo, prevención de lavado de dinero) sí pueden aplicarse a la FMF/Liga MX sin riesgo de sanción FIFA; cualquier mecanismo que intervenga gobernanza, elecciones, disciplina deportiva o estructura de propiedad de clubes por mandato público específico al deporte, no. Cada recomendación de este documento se etiqueta explícitamente con qué lado de esa línea ocupa.

---

## 1. Resumen ejecutivo

**[RECOMENDACIÓN]** México no necesita una nueva autoridad de integridad del fútbol: necesita **conectar y hacer cumplir** siete mecanismos que, en distinto grado, ya existen — el Código de Ética y la Comisión Disciplinaria de la FMF (que ya suspendió a 7 jugadores por apuestas en febrero de 2025), el Comité de Evaluación de árbitros con contrapesos (creado octubre de 2025), la alianza de monitoreo de apuestas Liga MX-Genius Sports (vigente desde noviembre de 2020), el Reglamento Nacional sobre Agentes de Fútbol de la FMF (2023, con carné de registro obligatorio), la obligación fiscal de "beneficiario controlador" ante el SAT vigente para toda persona moral mexicana desde 2022, las facultades de requerimiento de información y estudios de mercado de COFECE (ya ejercidas contra la FMF en 2021), y el propio canal global de denuncias de FIFA (BKMS). El problema no es la ausencia de reglas, sino que operan de forma aislada, sin protocolo común, sin verificación cruzada y —en el caso más grave documentado (Riodoce, julio 2025: firmas irregulares a niños de 12 años; y el caso Grupo Caliente: discrepancia entre propiedad formal ante la FMF y control real percibido)— sin consecuencia pública verificable. Este documento diseña un **Protocolo Nacional de Integridad del Fútbol Mexicano**: no una institución nueva, sino un convenio de coordinación entre organismos y facultades ya existentes, que (a) da al mecanismo operativo de protección de menores un procedimiento de investigación y sanción a academias con canal de denuncia independiente de la FMF; (b) blinda a árbitros/VAR con protocolo de evaluación y reporte de presión externa; (c) formaliza y da consecuencia sancionadora a la alianza de monitoreo de apuestas ya contratada; (d) hace pública la supervisión de agentes/representantes vinculándola al sistema de transferencias (SIID) ya existente; (e) cruza el registro de propietarios de clubes de la FMF contra el beneficiario controlador declarado al SAT, con escalamiento a COFECE ante discrepancia; (f) enruta denuncias de integridad hacia el canal global de FIFA (BKMS) y las de menores hacia SIPINNA, en vez de crear un canal nuevo; y (g) condiciona el acceso a beneficios públicos y capital privado (caso Apollo, que ya exige auditorías a los 18 clubes) a un resumen financiero público anual, aprovechando la facultad de requerimiento de información de COFECE como mecanismo de última instancia si la vía voluntaria falla. De 15 recomendaciones sustantivas, 13 (87%) están en las categorías 1-6 de la jerarquía de intervención; ninguna requiere una institución, consejo u organismo público nuevo — el único elemento nuevo es el propio convenio de coordinación (integración de sistemas existentes), que por su naturaleza (acuerdo administrativo, no institución/liga/academia/plataforma/certificación/universidad/competencia/centro/fondo/consejo/organismo público/sistema de scouting) no está sujeto a las 14 preguntas de justificación de la sección 2.1, aunque este documento las responde de forma preventiva en la sección 15 para dejar constancia expresa de por qué no aplican.

---

## 2. Objetivo

Diseñar el mecanismo operativo del Pilar 14 (Integridad) en sus siete componentes encargados por esta misión —protección de menores, árbitros/VAR, apuestas y amaño, agentes/representantes, transparencia de propiedad de clubes, protección de denunciantes y auditorías financieras—, siguiendo estrictamente la jerarquía de intervención de la sección 2 del manual metodológico y el estándar jurídico D-03 ya fijado por el Agente 0, cerrando el vacío de diseño identificado en `09-fase6-integracion-preliminar-diseno.md` (sección 8) sin contradecir las decisiones ya tomadas en Fases 5-7.

---

## 3. Preguntas abordadas

| ID | Pregunta | Tratamiento en este entregable |
|---|---|---|
| PQ-C01 | ¿Existe hoy un marco legal de protección de menores aplicable a fuerzas básicas? | Se retoma (Agente 3: no de forma específica y pública) y se diseña el mecanismo operativo sobre el convenio FMF-SIPINNA que el Pilar 2 formaliza (sección 9-16 parte A) |
| PQ-C03 | ¿Qué mecanismo público puede recibir y resolver denuncias de cobros irregulares o abuso en captación de menores? | Respondida operativamente: Procuradurías de Protección de NNA vía convenio FMF-SIPINNA, con protocolo de investigación diseñado aquí (parte A) |
| PQ-C08 | ¿Cuál es el mecanismo legal más viable para condicionar beneficios públicos al cumplimiento de estándares de protección de menores, sin riesgo FIFA? | Se aplica el mismo criterio de condicionalidad administrativa a academias con cobros irregulares (parte A) y a transparencia financiera (parte G) |
| PQ-C10 | ¿Cómo ha domesticado la FMF los FFAR para agentes que operan solo en transferencias domésticas? | Parcialmente respondida: se ubicó el Reglamento Nacional sobre Agentes de Fútbol (FMF, 2023, carné obligatorio) — su contenido íntegro sigue sin verificar (ver limitaciones); se diseña el mecanismo de transparencia sobre esa base (parte D) |
| PQ-B02 | ¿Qué conflictos de interés existen por multipropiedad de clubes? | Se retoma para diseñar verificación de beneficiario final (parte E) |
| PQ-B07 | ¿Coincide el registro formal de propiedad de cada club ante la FMF con el control económico real reportado por prensa? | Se diseña el mecanismo de verificación cruzada (parte E), sin resolver el caso Grupo Caliente en sí — eso requiere ejecutar el mecanismo |
| PQ-B11 | ¿Qué papel informal juegan los agentes de jugadores en decisiones de la Selección? | Se diseña mecanismo de transparencia de contratos de representación (parte D); no se investiga el hecho en sí (excede el alcance de un agente de diseño) |
| — (nueva) | ¿Qué mecanismo puede detectar amaño de partidos aprovechando alianzas ya contratadas con casas de apuestas/proveedores de datos? | Respondida (parte C) |
| — (nueva) | ¿Cómo proteger la integridad arbitral/VAR sin crear un organismo nuevo? | Respondida (parte B) |
| — (nueva) | ¿Quién audita a la FMF/Liga MX, con qué mandato y qué consecuencia si se niega información? | Respondida (parte G), conectada al riesgo transversal ya documentado por el Agente 14 (Finanzas) |

Preguntas nuevas generadas por este agente: ver "Preguntas nuevas para el registro maestro" al final.

---

## 4. Metodología

**Fuentes usadas:** los tres documentos obligatorios de lectura (`00`, `02`, `fase2-agente3`, `fase2-agente2`, `07-registro-decisiones.md`), más búsquedas dirigidas (WebSearch) para verificar el estado operativo actual de los mecanismos que el Agente 3 había dejado como `[DATO INCOMPLETO]` (reglamento de agentes, sanciones por apuestas, alianza de monitoreo, jurisprudencia del TJUE sobre FFAR) y para identificar mecanismos legales generales existentes no explorados por los Agentes 2/3 (obligación fiscal de beneficiario controlador, regulación de casas de apuestas por la Dirección General de Juegos y Sorteos de SEGOB, prevención de lavado de dinero). El acceso directo (WebFetch) a varias páginas de prensa deportiva (ESPN Deportes) devolvió HTTP 403, replicando el patrón de bloqueo ya documentado por los Agentes 2 y 3; esa evidencia se cita por fragmento indexado, nivel B, con la misma advertencia de re-verificación antes de uso normativo.

**Clasificación de evidencia:** escala A-D de la sección 3.2 del manual. Se etiqueta cada afirmación con `[HECHO]`, `[ESTIMACIÓN]`, `[HIPÓTESIS]`, `[INFERENCIA]`, `[OPINIÓN]`, `[RECOMENDACIÓN]`, `[DATO INCOMPLETO]`.

**Periodo cubierto:** estado vigente a julio de 2026, sobre la línea base consolidada en Fase 3 y las decisiones D-01 a D-05 del registro de decisiones.

**Nota sobre coordinación con agentes paralelos:** este documento no puede leer las rondas de cierre de Gobernanza (Pilar 1) ni Marco jurídico (Pilar 2), que se producen en paralelo. Donde este documento asume decisiones de esos pilares (p. ej., que el Pilar 2 formaliza el convenio FMF-SIPINNA como instrumento legal), se marca explícitamente como supuesto de coordinación, no como hecho verificado, y debe reconciliarse en la siguiente integración del Agente 0.

---

## 5. Hallazgos

### 5.1 Protección de menores (mecanismo operativo)

1. `[HECHO, heredado, nivel B]` Riodoce (20 de julio de 2025) documentó firmas irregulares a niños de 12 años; el Agente 3 no pudo verificar el texto completo (bloqueo 403) ni si involucra clubes afiliados o academias no afiliadas.
2. `[HECHO, heredado, nivel A]` La Ley General de los Derechos de Niñas, Niños y Adolescentes crea SIPINNA y las Procuradurías de Protección de NNA estatales, con mandato genérico de recibir denuncias de vulneración de derechos de la niñez, pero sin protocolo específico para academias de fútbol (Agente 3, hallazgo 5.5).
3. `[HECHO, heredado, nivel B]` El Agente 3 recomendó (prioridad alta, sección 16.2) un convenio FMF-SIPINNA/Procuradurías como instrumento administrativo, sin necesidad de ley, para designar un canal de denuncia independiente de la FMF.
4. `[DATO INCOMPLETO, heredado]` No existe evidencia pública de un reglamento de "salvaguarda"/safeguarding de menores en la FMF equivalente al de otras federaciones (FA inglesa, RFEF).
5. `[HIPÓTESIS, nueva]` Dado que el convenio FMF-SIPINNA (si el Pilar 2 lo formaliza) resuelve el **canal de recepción** de denuncias pero no necesariamente el **procedimiento de investigación, sanción a la academia y protección del denunciante**, existe un vacío operativo distinto del vacío legal ya cerrado por el Agente 3 — este es el vacío que corresponde exactamente a esta misión.

### 5.2 Árbitros y VAR

6. `[HECHO, nivel B, verificado vía búsqueda propia]` La FMF creó en octubre de 2025 una nueva estructura de la Comisión de Árbitros, con un "Comité de Evaluación" integrado por un exárbitro, un exjugador y un exdirector técnico, explícitamente diseñado para agregar "pesos y contrapesos" a las evaluaciones y designaciones arbitrales, con procedimientos "claros y documentados" (Récord, 16-oct-2025).
7. `[HECHO, nivel B]` La propia Comisión de Árbitros de la FMF declara públicamente que busca formar "guardianes de las reglas y referentes de integridad" y fortalecer transparencia mediante herramientas tecnológicas (VAR, SAOT — sistema semiautomatizado de fuera de lugar).
8. `[DATO INCOMPLETO, nueva]` No se encontró evidencia pública de un protocolo específico de reporte de presión externa (de dueños de clubes, patrocinadores, aficionados organizados) sobre árbitros o del proceso disciplinario si esa presión se detecta — el "Comité de Evaluación" parece enfocado en desempeño técnico, no en integridad ante presión externa.
9. `[HECHO, nivel B]` La FMF ya sanciona conductas de integridad (apuestas, amaño) vía el Código de Ética (Art. 11) y el Reglamento de Sanciones (Apéndice IV) aplicado por la Comisión Disciplinaria — el mismo marco disciplinario podría extenderse explícitamente a presión externa sobre árbitros sin crear un reglamento nuevo (ver hallazgo 5.3.4).

### 5.3 Apuestas y amaño de partidos

10. `[HECHO, nivel B, verificado vía búsqueda propia]` Liga MX firmó en noviembre de 2020 una alianza con Genius Sports Group, otorgándole derechos exclusivos de captura de datos en vivo de **todas las divisiones** (Liga MX, Liga MX Femenil, Liga de Expansión, Copa MX), con el objetivo explícito de proteger al fútbol mexicano del amaño de partidos y las apuestas ilegales — un mecanismo de monitoreo de patrones anómalos **ya contratado y vigente**, no algo por crear.
11. `[HECHO, nivel B]` Según Sportradar (empresa que también trabaja con FIFA en esta materia), el fútbol mexicano en todas sus divisiones está catalogado con un índice de riesgo "alto y elevado" de apuestas ilegales, cumpliendo 5 de 7 condiciones asociadas a la operación de mafias de amaño de partidos; el volumen de apuestas asociado a partidos de Liga MX se estima en ~4,857 millones de dólares anuales (fuente: Sportradar/Sports Betting Integrity, vía Forbes México, nivel C — cifra de proveedor comercial con metodología no pública, no verificable de forma independiente en este ejercicio).
12. `[HECHO, nivel B]` La FMF ya sancionó, en febrero de 2025, a 7 jugadores con más de 50 años de suspensión combinada por participación en apuestas/amaño, aplicando el Art. 11(b) del Código de Ética de la FMF ("quien participa directa o indirectamente en apuestas... que influya de manera indebida en el resultado...") y los Arts. 27/30 del Código de Ética de FIFA — evidencia de que el régimen sancionador **ya existe y ya se aplicó**, no es un vacío de reglamento.
13. `[HECHO, nivel C, fuente única indexada]` Una nota de ESPN reporta 5 casos de manipulación de resultados investigados en Liga Premier, Liga de Expansión y Liga MX Femenil — es decir, la detección/sanción documentada se concentra en categorías **no** de Liga MX varonil de primera división, lo que sugiere que el riesgo (y posiblemente la vigilancia real) es mayor en categorías de menor visibilidad mediática y menor recurso de integridad. `[DATO INCOMPLETO]`: no se pudo verificar la fecha exacta de esos 5 casos ni si la alianza con Genius Sports cubre con la misma intensidad esas categorías inferiores que la primera división.
14. `[HECHO, nivel B]` México regula las casas de apuestas mediante la Ley Federal de Juegos y Sorteos y su Reglamento, a través de la Dirección General de Juegos y Sorteos (DGJS) de la Secretaría de Gobernación (SEGOB), que otorga permisos ("permisionarios") y exige solvencia financiera, auditorías de antecedentes y prohibición de otorgar crédito a apostadores; los operadores pagan un impuesto sobre ingresos brutos de juego (GGR) del 30% — es decir, **ya existe un regulador público con jurisdicción sobre las casas de apuestas reguladas**, distinto de la FMF/Liga MX.
15. `[HECHO, nivel A, general no verificado línea por línea]` Las actividades de juegos con apuesta, concursos y sorteos son una "actividad vulnerable" bajo la Ley Federal para la Prevención e Identificación de Operaciones con Recursos de Procedencia Ilícita (LFPIORPI), con obligación de reporte de operaciones inusuales/relevantes a la Unidad de Inteligencia Financiera (UIF) de la Secretaría de Hacienda — un canal público ya existente, ajeno a la FMF, que en teoría podría recibir alertas de patrones de apuesta anómalos vinculados a partidos específicos.

### 5.4 Agentes/representantes

16. `[HECHO, nivel B, verificado vía búsqueda propia]` Existe un "Reglamento Nacional sobre Agentes de Fútbol" de la FMF (versión 2023, documento público en fmf.mx/assets/Reglamento_Sobre_Intermediarios.pdf) que exige que todo intermediario contratado por un club o jugador esté registrado ante la FMF y cuente con un carné de registro expedido por la Federación — esto **cierra parcialmente** el `[DATO INCOMPLETO]` que el Agente 3 había dejado abierto en PQ-C10 (no se había localizado el reglamento vigente); sigue sin verificarse si el registro resultante es público y consultable.
17. `[HECHO, nivel B, verificado vía búsqueda propia]` El Tribunal de Justicia de la Unión Europea (TJUE) confirmó en julio de 2026 la "autoridad y legitimidad" de FIFA para regular la actividad de los agentes, incluido el tope de comisión, pero declaró ilegal la restricción de dos meses para que un agente contacte a un jugador ya vinculado por contrato de exclusividad con otro agente — la incertidumbre jurídica de los FFAR que el Agente 3 señaló como total (sección 5.4) se ha reducido parcialmente: el núcleo (licencia, tope de comisión) está confirmado; un artículo específico (regla de los dos meses) no.
18. `[DATO INCOMPLETO, heredado]` Sigue sin verificarse si el carné de registro de la FMF es consultable públicamente (registro abierto) o solo interno, y cuántos agentes operan formalmente licenciados en México — la cifra "111 agencias, 12 con licencia FIFA" citada por el Agente 2 se marca expresamente como potencialmente desactualizada (previa a la reforma FFAR de 2023).
19. `[HIPÓTESIS, heredada]` El Agente 2 documentó una posible influencia informal de al menos un agente (Christian Bragarnik/Score Futbol) en decisiones relacionadas con la Selección Nacional, vía presencia en palcos directivos — no verificado formalmente, y este documento no lo investiga a fondo (excede el alcance de diseño), pero diseña el mecanismo de transparencia que permitiría, en el futuro, contrastarlo con datos (parte D).

### 5.5 Transparencia de propiedad de clubes

20. `[HECHO, heredado, nivel C, marcado dato incompleto por el propio Agente 2]` Existe una discrepancia documentada entre el control real percibido de Xolos de Tijuana (asociado públicamente a Jorge Hank Rhon/Grupo Caliente) y la negación pública de la FMF de que Hank Rhon sea su dueño formal — "la propiedad formal registrada ante la FMF puede no coincidir con quién ejerce el control real de un club" (Agente 2, hallazgo central).
21. `[HECHO, nivel A, verificado vía búsqueda propia]` Desde el 1 de enero de 2022, el Artículo 32-B Ter del Código Fiscal de la Federación obliga a **toda persona moral** (incluidos clubes de fútbol constituidos como sociedades o asociaciones civiles) a obtener, conservar y, cuando el SAT lo requiera, proporcionar información fidedigna y actualizada de sus "beneficiarios controladores" (personas físicas que en última instancia poseen o controlan la entidad); el incumplimiento se sanciona con multas de $500,000 a $2,000,000 MXN. Es una obligación fiscal general, no específica del deporte — cumple el estándar D-03.
22. `[HECHO, heredado, nivel B]` COFECE ya ejerció, en 2021, su facultad de requerir información y sancionar a la FMF y 17 clubes sin que ello activara una reacción de FIFA (precedente central del criterio D-03).
23. `[DATO INCOMPLETO, heredado]` No hay evidencia de que COFECE haya abierto expediente posterior a 2021 sobre multipropiedad de clubes (Agente 3, PQ-C09).

### 5.6 Protección de denunciantes

24. `[HECHO, nivel B, verificado vía búsqueda propia]` FIFA opera un sistema de denuncia global, confidencial y anónimo (BKMS, bkms-system.net/FIFA) para reportar amaño de partidos y conductas de integridad, gestionado directamente por el Departamento de Integridad de FIFA, aplicable a cualquier caso bajo jurisdicción de FIFA (incluidas sus confederaciones/federaciones miembro) — un canal **ya existente y externo a la FMF**, no utilizado ni publicitado de forma documentada en México en las fuentes consultadas.
25. `[HECHO, nivel B, verificado vía búsqueda propia]` La Ley General de Responsabilidades Administrativas de México contempla protección a denunciantes, pero —según análisis de organizaciones de la sociedad civil (Mexicanos Contra la Corrupción e Impunidad)— es "deficiente" en regular canales de denuncia y protección contra represalias, y su alcance es primordialmente para servidores públicos, no para el sector privado/asociativo donde opera la FMF. No existe, hasta donde permitió verificar esta investigación, una ley federal general de protección al denunciante aplicable al sector privado mexicano.
26. `[INFERENCIA, nueva]` La combinación de los hallazgos 24-25 significa que, para integridad deportiva (apuestas, amaño, presión sobre árbitros, irregularidades de agentes), el canal más robusto y ya operativo no es mexicano sino de FIFA (BKMS); para protección de menores, el canal ya diseñado por el Pilar 2 es SIPINNA/Procuradurías; el vacío real no es la ausencia de canal, sino que **ninguno de los dos está claramente publicitado en español, en México, como vía independiente de la FMF**, ni existe protección formal contra represalia laboral para quien denuncia desde dentro del sistema (jugador, entrenador, empleado de academia).

### 5.7 Auditorías y transparencia financiera

27. `[HECHO, heredado, nivel B]` El Agente 14 (Finanzas, Fase 7) identificó la opacidad financiera de FMF/Liga MX como "el riesgo financiero más determinante de todo el proyecto": mientras persista, el escenario presupuestal transformador no puede ejecutarse en firme y la precisión de todo el presupuesto permanece en nivel C-D (`fase7-agente14-finanzas.md`, sección 11, fila de mayor probabilidad e impacto).
28. `[HECHO, heredado, nivel B]` El fondo de capital privado Apollo Global Management condicionó su propuesta de inversión (~1,300 millones de dólares, diciembre de 2024) a, entre otras cosas, "auditorías a los 18 clubes" y "buen gobierno" (Agente 2, hallazgo INFERENCIA sección 5) — es decir, **la presión de mercado por auditoría externa ya existe y ya fue exigida por un actor privado**, sin que el Estado tuviera que intervenir.
29. `[HECHO, heredado, nivel B]` COFECE tiene, bajo la Ley Federal de Competencia Económica, la facultad de realizar estudios de mercado (Art. 12, fracción XX) y de requerir información bajo apercibimiento de multa (Art. 34) — facultad ya ejercida en el expediente de 2021 — que no requiere que exista una investigación de sanción abierta para solicitarse.
30. `[HECHO, heredado, nivel B]` La nueva estructura de gobierno corporativo de Liga MX (abril de 2026) creó un "Comité de Certificación, Ética y Buen Gobierno" entre sus cuatro comités estratégicos, explícitamente para "institucionalizar procesos, establecer controles, fortalecer transparencia"; una nota de julio de 2026 (Récord) señala que el "Comité Deportivo... sigue sin definirse" — es decir, la estructura ya existe formalmente pero su mandato operativo, incluido el de auditoría, aún no está desarrollado en la práctica.
31. `[HECHO, heredado, nivel B]` El Agente 14 ya diseñó y costeó un "vehículo de auditoría consolidado" con tres módulos (academias, entrenadores, datos/scouting) — pero ese vehículo audita **cumplimiento de programas del proyecto**, no los estados financieros institucionales de la FMF/Liga MX como organizaciones; son objetos de auditoría distintos y no deben confundirse (`fase7-agente14-finanzas.md`, Anexo A.13).

---

## 6. Evidencia

| # | Cifra/afirmación | Fuente | Fecha | Alcance | Metodología | Limitaciones | Nivel |
|---|---|---|---|---|---|---|---|
| E1 | 7 jugadores sancionados con más de 50 años de suspensión combinada por apuestas/amaño | Infobae, vía Comisión Disciplinaria FMF (Código de Ética Art. 11, Reglamento de Sanciones Apéndice IV) | 15-feb-2025 | Nacional, fútbol profesional | Nota periodística sobre resolución disciplinaria de la FMF | No se verificó el expediente disciplinario primario (posible bloqueo de acceso no probado en este ejercicio) | B |
| E2 | Alianza exclusiva Liga MX-Genius Sports para captura de datos en vivo y monitoreo antiamaño en todas las divisiones | Sportico.com, ESPN Deportes (indexado) | nov-2020 | Liga MX, Liga MX Femenil, Expansión MX, Copa MX | Comunicado de negocio replicado en prensa especializada | No se verificó el contrato primario ni si sigue vigente en 2026 (han pasado casi 6 años) | B — **requiere verificación de vigencia antes de basar recomendación en firme** |
| E3 | Índice de riesgo "alto y elevado" de apuestas ilegales en fútbol mexicano; ~4,857 millones USD/año en apuestas asociadas a partidos de Liga MX | Sportradar/Sports Betting Integrity, vía Forbes México | Sin fecha exacta verificada, cita periodística reciente | Todas las divisiones del fútbol mexicano | Metodología propietaria de proveedor comercial de datos de apuestas, no pública | Cifra no verificable de forma independiente; posible interés comercial del proveedor en magnificar el riesgo que su propio producto mitiga | C |
| E4 | Obligación de beneficiario controlador (Art. 32-B Ter CFF), vigente desde el 1-ene-2022, multas de $500,000 a $2,000,000 MXN por incumplimiento | SAT (documento oficial de preguntas y respuestas), ECIJA, BDO México | 2022, con obligación continua | Nacional, toda persona moral mexicana | Disposición fiscal de aplicación general | No se verificó si la FMF/clubes ya cumplen esta obligación en la práctica, ni si el SAT audita activamente al sector deportivo | A (existencia de la norma) / D (cumplimiento real por clubes de fútbol, no verificado) |
| E5 | Comité de Certificación, Ética y Buen Gobierno como uno de cuatro comités estratégicos de la nueva Liga MX AC | Récord, El Universal, La Jornada | 23-24 abr-2026, seguimiento jul-2026 | Liga MX (18 clubes) | Cobertura periodística de la Asamblea de Dueños | Mandato operativo del comité "sigue sin definirse" según fuente de julio de 2026 — estructura formal sin función verificada todavía | B |
| E6 | Condiciones de Apollo Global Management a su propuesta de inversión: fin de multipropiedad, fin de descenso, auditorías a los 18 clubes, "buen gobierno" | Inside World Football, ESPN Colombia, pe-insights.com (vía Agente 2) | dic-2024 | Liga MX | Cobertura de negocio deportivo especializada | No hay declaración pública que confirme si las auditorías ya se están ejecutando o siguen siendo solo una condición de negociación | B |
| E7 | Multa COFECE-028-2021 a FMF y 17 clubes: $177.6 millones MXN (reutilizada del Agente 3, ancla de precedente D-03) | COFECE-028-2021 | 23-sep-2021 | Nacional, mercado de fichajes | Investigación administrativa de competencia económica | No cubre multipropiedad ni TV | A |

---

## 7. Fuentes

Se reutilizan íntegramente las fuentes ya citadas en `fase2-agente2-gobernanza-y-poder.md` y `fase2-agente3-derecho-y-regulacion.md` (secciones 6-7 de cada uno). Fuentes nuevas de esta ronda: Récord ("FMF presenta nueva estructura de la Comisión de Árbitros", 16-oct-2025); Infobae ("FMF sanciona con más de 50 años de suspensión a 7 jugadores involucrados en apuestas", 15-feb-2025); ESPN Deportes (notas sobre amaño de partidos y reglamento de sanciones, sin fecha exacta verificable, acceso directo bloqueado HTTP 403 en dos intentos); Sportico.com ("Mexico's LigaMX Taps Genius Sports As Exclusive Gambling Data Partner", 2020); Forbes México ("La Liga MX: casi 5,000 mdd en apuestas y alto riesgo de amaño de partidos", sin fecha exacta verificada); fmf.mx/assets/Reglamento_Sobre_Intermediarios.pdf (Reglamento Nacional sobre Agentes de Fútbol FMF, 2023, referenciado, no leído en su totalidad); Infobae ("La FIFA aplaude que el TJUE reconozca su autoridad y legitimidad en la norma sobre agentes", 16-jul-2026); inside.fifa.com ("Reporting Mechanisms" — sistema BKMS); Servicio de Administración Tributaria, "Preguntas y respuestas sobre beneficiarios controladores" (omawww.sat.gob.mx); ECIJA y BDO México (análisis de despacho legal/fiscal sobre Art. 32-B Ter CFF); Dirección General de Juegos y Sorteos, SEGOB (juegosysorteos.gob.mx); Ley Federal para la Prevención e Identificación de Operaciones con Recursos de Procedencia Ilícita (referenciada, no leída en su totalidad); Mexicanos Contra la Corrupción e Impunidad, "Proteger a denunciantes en México" (contralacorrupcion.mx); Récord, El Universal, La Jornada, Excélsior (cobertura del nuevo gobierno corporativo de Liga MX, abril-julio 2026).

---

## 8. Limitaciones

- El acceso directo (WebFetch) a notas específicas de ESPN Deportes sobre casos de amaño y reglamento de sanciones devolvió HTTP 403 en dos intentos durante esta investigación, replicando el patrón ya documentado por los Agentes 2 y 3; esa evidencia se basa en fragmentos indexados por el buscador, no en el artículo completo.
- No se verificó si la alianza Liga MX-Genius Sports (firmada en 2020) sigue vigente en sus términos originales en 2026, ni su cobertura real sobre categorías inferiores (Liga Premier, Expansión, Femenil), donde —según el hallazgo 5.3.13— se concentran los casos de manipulación detectados recientemente. Esto es una limitación importante: la recomendación de "formalizar" esta alianza (sección 16, parte C) asume que sigue activa; si no lo está, la recomendación cambia de "formalizar" a "renovar/recontratar".
- No se pudo leer el texto completo del Reglamento Nacional sobre Agentes de Fútbol de la FMF (2023) más allá de su existencia y el requisito de carné — su contenido detallado (topes de comisión, doble representación, régimen sancionador específico) debe verificarse directamente antes de diseñar cualquier reforma sobre él.
- No se verificó si la FMF y los clubes de Liga MX ya presentan su declaración de beneficiario controlador al SAT en cumplimiento del Art. 32-B Ter CFF, ni si el SAT ha fiscalizado activamente al sector — el mecanismo de la parte E de este documento asume que la obligación existe (hecho verificado) pero no que se cumple en la práctica (no verificado).
- El mandato operativo real del "Comité de Certificación, Ética y Buen Gobierno" de Liga MX no está definido públicamente a la fecha de este documento (julio de 2026) — cualquier recomendación que dependa de darle función de auditoría (parte G) debe tratarse como una propuesta de qué debería hacer ese comité, no como una descripción de lo que ya hace.
- Este documento no puede leer, por instrucción de la misión, las rondas paralelas de cierre de los Pilares 1 (Gobernanza) y 2 (Marco jurídico); cualquier supuesto sobre lo que esos pilares diseñan (en particular, la formalización del convenio FMF-SIPINNA) debe reconciliarse en la siguiente integración del Agente 0.
- No se investigó a fondo, por exceder el alcance de un agente de diseño, la veracidad del caso específico de Grupo Caliente/Jorge Hank Rhon ni la influencia informal reportada de agentes sobre la Selección Nacional; este documento diseña el mecanismo que permitiría, en el futuro, verificar ambos casos con datos, no los resuelve.

---

## 9. Activos existentes

Organizados por los siete componentes de la misión:

- **Protección de menores:** Ley General de los Derechos de NNA + SIPINNA + Procuradurías de Protección de NNA estatales; recomendación ya hecha por el Agente 3 de convenio FMF-SIPINNA (asumido como formalizado por el Pilar 2); Convenio de Actividades Deportivas 14-16 años de la FMF; Ley Federal del Trabajo Capítulo XII y Título Quinto Bis.
- **Árbitros/VAR:** Comisión de Árbitros de la FMF con nueva estructura (octubre 2025) y Comité de Evaluación con contrapesos (exárbitro, exjugador, exdirector técnico); VAR y SAOT como herramientas tecnológicas ya desplegadas; Código de Ética FMF (Art. 11) y Reglamento de Sanciones (Apéndice IV) ya aplicables a cualquier persona con licencia FMF, incluidos árbitros.
- **Apuestas y amaño:** alianza Liga MX-Genius Sports (monitoreo de datos en vivo, desde 2020); Código de Ética FMF Art. 11(b) y precedente sancionador ya ejercido (7 jugadores, febrero 2025); Dirección General de Juegos y Sorteos (SEGOB) como regulador de casas de apuestas; obligación de reporte de "actividad vulnerable" a la UIF bajo la LFPIORPI.
- **Agentes/representantes:** Reglamento Nacional sobre Agentes de Fútbol de la FMF (2023, carné obligatorio); SIID como sistema de registro de transferencias ya existente; sentencia TJUE de julio de 2026 que confirma la autoridad de FIFA sobre licencia y tope de comisión.
- **Transparencia de propiedad de clubes:** Registro Público de Comercio (Secretaría de Economía); obligación de beneficiario controlador ante el SAT (Art. 32-B Ter CFF, vigente desde 2022); facultades de requerimiento de información y estudios de mercado de COFECE (Arts. 12-XX y 34 LFCE), ya ejercidas en 2021.
- **Protección de denunciantes:** sistema BKMS de FIFA (canal global, confidencial, anónimo, ya operativo); Procuradurías de Protección de NNA (para menores, vía convenio FMF-SIPINNA); protecciones generales contra despido injustificado de la Ley Federal del Trabajo.
- **Auditorías y transparencia financiera:** Comité de Certificación, Ética y Buen Gobierno de Liga MX (creado abril 2026, mandato operativo aún por definir); condición de auditoría a los 18 clubes ya exigida por Apollo Global Management como parte de su propuesta de capitalización; facultad de estudios de mercado y requerimiento de información de COFECE; vehículo de auditoría consolidado ya diseñado por el Agente 14 para academias/entrenadores/datos (objeto distinto, pero mismo tipo de instrumento contractual reutilizable).

---

## 10. Problemas

1. El canal de denuncia de menores recae, en la práctica actual, en la propia FMF (juez y parte), y aunque el Agente 3 ya diseñó la salida (convenio SIPINNA), no existe todavía un **procedimiento operativo** publicado de investigación de caso, plazo de resolución, ni catálogo de sanciones a academias por cobros irregulares o fraude en captación.
2. El Comité de Evaluación de árbitros (creado octubre 2025) está orientado a desempeño técnico, no hay evidencia de un protocolo específico de reporte y sanción de presión externa (dueños, patrocinadores, grupos organizados) sobre árbitros.
3. La alianza Liga MX-Genius Sports, si sigue vigente, opera sin que exista evidencia pública de un protocolo de escalamiento claro (qué pasa cuando se detecta un patrón anómalo: quién investiga, en cuánto tiempo, con qué consecuencia) ni de que su cobertura alcance con la misma intensidad a las categorías donde se han detectado más casos recientes (Liga Premier, Expansión, Femenil).
4. El Reglamento de Agentes de la FMF exige registro, pero no hay evidencia de que ese registro sea público/consultable — sin transparencia del registro, no se puede verificar la fragmentación del mercado (111 agencias, 12 con licencia FIFA, cifra potencialmente desactualizada) ni contrastar la hipótesis de influencia informal sobre la Selección.
5. La obligación de beneficiario controlador ante el SAT existe desde 2022 mediante ley fiscal general, pero no hay evidencia de que se haya cruzado nunca contra el registro de propiedad de clubes de la FMF — dos sistemas de información que podrían resolver la discrepancia del caso Grupo Caliente no se hablan entre sí.
6. No existe, en México, un canal de denuncia de integridad deportiva (distinto al de menores) que sea (a) independiente de la FMF, (b) protegido contra represalia laboral, y (c) conocido públicamente — el canal más robusto disponible (FIFA BKMS) es global y no está publicitado localmente en las fuentes consultadas.
7. La FMF/Liga MX no publican estados financieros auditados de forma pública y recurrente; el "Comité de Certificación, Ética y Buen Gobierno" de Liga MX existe formalmente desde abril de 2026 pero su mandato operativo de auditoría no está definido, y la presión más fuerte por auditoría hasta ahora proviene de un actor privado (Apollo) condicionando su propia inversión, no de un mecanismo público o de cumplimiento estable.

---

## 11. Alternativa de mejora

- **Menores (A):** reformar el procedimiento interno de la FMF para que, en cuanto el convenio FMF-SIPINNA esté formalizado (Pilar 2), toda denuncia recibida por SIPINNA/Procuraduría contra una academia o club dispare automáticamente un expediente paralelo en la Comisión Disciplinaria de la FMF, con plazo máximo de resolución y catálogo de sanciones (desde amonestación hasta desafiliación) — sin crear un órgano investigador nuevo, usando el que ya existe (Comisión Disciplinaria) con un gatillo externo (SIPINNA) que hoy no tiene.
- **Árbitros (B):** ampliar el mandato ya escrito del Comité de Evaluación (creado octubre 2025) para incluir explícitamente presión externa como categoría de reporte, con la misma composición de contrapesos (exárbitro, exjugador, exdirector técnico) ya diseñada, sin crear un comité paralelo.
- **Apuestas (C):** formalizar por escrito (memorando de entendimiento, no ley) el protocolo de escalamiento de la alianza Genius Sports: qué patrón dispara alerta, a quién llega (Comisión Disciplinaria FMF), en cuánto tiempo se resuelve, y verificar/renovar su cobertura a categorías inferiores donde se concentran los casos detectados.
- **Agentes (D):** reformar el Reglamento Nacional sobre Agentes de Fútbol para que el registro/carné sea públicamente consultable (nombre del agente, jugadores representados, club), vinculado al SIID existente para transferencias domésticas.
- **Propiedad de clubes (E):** no requiere reforma de ley — requiere un convenio de intercambio de información (SAT-FMF o SAT-COFECE) para cruzar beneficiario controlador declarado contra el padrón de propietarios de clubes de la FMF, con escalamiento a COFECE si hay discrepancia no explicada.
- **Denunciantes (F):** que la FMF publicite activamente, en español y en los canales de comunicación de la Selección/Liga MX, el canal BKMS de FIFA como vía independiente para integridad deportiva, y que el convenio FMF-SIPINNA (Pilar 2) incluya expresamente protección contra represalia laboral (aprovechando protecciones ya existentes en la Ley Federal del Trabajo contra despido injustificado, aplicadas explícitamente a quien denuncie).
- **Auditorías (G):** que el Comité de Certificación, Ética y Buen Gobierno de Liga MX (ya creado, sin mandato operativo definido) adopte como su primer mandato explícito la publicación de un resumen financiero anual auditado de Liga MX y sus 18 clubes — la misma auditoría que Apollo ya exige como condición de inversión, formalizada como práctica institucional y no solo como condición de negociación privada.

## 12. Alternativa de integración

- Integrar los siete mecanismos en un **Protocolo Nacional de Integridad del Fútbol Mexicano** (convenio de coordinación, no institución nueva — ver sección 15) entre: Comisión Disciplinaria y Código de Ética de la FMF, Comité de Evaluación de árbitros, Comité de Certificación, Ética y Buen Gobierno de Liga MX, SIPINNA/Procuradurías de Protección de NNA, COFECE, SAT, Dirección General de Juegos y Sorteos (SEGOB), UIF, y el proveedor de monitoreo de apuestas ya contratado (Genius Sports u otro). El protocolo no sustituye ninguna facultad legal existente; solo establece quién avisa a quién, en qué plazo y con qué formato — mismo principio de integración que el Agente 3 usó para el convenio FMF-SIPINNA.
- Integrar la verificación de beneficiario controlador (SAT) con el padrón de propietarios de clubes de la FMF, y con la facultad de requerimiento de información de COFECE como mecanismo de escalamiento si la FMF no puede o no quiere reconciliar una discrepancia por sí sola.
- Integrar el canal BKMS de FIFA (ya existente, global) como la vía primaria de denuncia de integridad deportiva no relacionada con menores, en vez de crear un canal mexicano paralelo — evita duplicidad y aprovecha un sistema ya confidencial, anónimo y con departamento dedicado.

## 13. Alternativa de escalamiento

- Escalar el Comité de Evaluación de árbitros (ya creado) para que sus criterios de "pesos y contrapesos" se documenten y publiquen como estándar de referencia para las demás comisiones disciplinarias de la FMF (agentes, apuestas), sin crear estructuras paralelas.
- Escalar la alianza de monitoreo de apuestas (Genius Sports u otro proveedor) de "todas las divisiones" (ya contratado en 2020) a un protocolo de reporte público agregado anual (número de alertas generadas, número de casos escalados, número de sanciones resultantes) — visibilidad, no expansión de facultades.
- Escalar la condición de auditoría que ya exige Apollo Global Management (privada, para su propia inversión) a un estándar institucional permanente de Liga MX, independiente de si la capitalización de Apollo se concreta o no.
- Escalar la obligación de beneficiario controlador (ya universal para personas morales mexicanas desde 2022) a una verificación sistemática y periódica del padrón de propiedad de clubes, no solo reactiva ante un caso mediático como el de Grupo Caliente.

## 14. Alternativa de sustitución

- Sustituir la ambigüedad actual sobre quién recibe una denuncia de integridad (hoy, por defecto, la propia FMF) por una regla explícita de bifurcación: denuncias de menores → SIPINNA/Procuraduría (vía convenio del Pilar 2); denuncias de integridad deportiva de adultos (apuestas, amaño, presión sobre árbitros, irregularidad de agentes) → canal BKMS de FIFA, con copia informativa obligatoria a la Comisión Disciplinaria de la FMF para que pueda actuar en paralelo bajo su propio reglamento. No se crea un canal nuevo; se sustituye la ambigüedad por una regla de enrutamiento.
- Sustituir la exigencia de auditoría externa hoy dependiente de la voluntad de un solo inversionista privado (Apollo) por un mandato explícito y permanente del Comité de Certificación, Ética y Buen Gobierno de Liga MX — mismo comité, mandato más claro y menos dependiente de que una negociación de capital específica se concrete.

## 15. Necesidad de nueva capacidad

`[RECOMENDACIÓN]` Ninguno de los siete componentes de esta misión requiere, por sí solo, una institución, liga, academia, plataforma, certificación, universidad, competencia, centro de alto rendimiento, fondo, consejo, organismo público o sistema de scouting nuevo — todos son resolubles mediante reforma de reglamento privado (FMF/Liga MX), convenio interinstitucional (FMF-SIPINNA ya en curso por el Pilar 2; SAT-FMF/COFECE nuevo), activación de facultades ya existentes y no ejercidas de forma sistemática (COFECE, UIF, DGJS), o adopción de un canal ya operativo (FIFA BKMS). El único elemento nuevo de este documento es el **Protocolo Nacional de Integridad del Fútbol Mexicano** (sección 12), que es un convenio de coordinación —no pertenece a ninguna de las categorías listadas en la sección 2.1 del manual (no es institución, no es liga, no es plataforma tecnológica nueva, no es consejo con facultades propias: no decide, no sanciona, no administra presupuesto; solo documenta quién avisa a quién y en qué plazo, ejecutado por las instituciones ya existentes)— y por tanto no está formalmente sujeto a las 14 preguntas de justificación. No obstante, y siguiendo la misma disciplina que aplicó el Agente 3 a su "mecanismo de coordinación permanente" (sección 15 de `fase2-agente3`), se responden aquí de forma preventiva para que el Control 4 no lo devuelva por omisión:

| # | Pregunta | Respuesta |
|---|---|---|
| 1 | ¿Qué capacidad existe hoy que cubre esta función? | Cada una de las siete: Comisión Disciplinaria FMF, Comité de Evaluación de árbitros, alianza de monitoreo de apuestas, Reglamento de Agentes FMF, obligación fiscal de beneficiario controlador, canal BKMS de FIFA, Comité de Ética y Buen Gobierno de Liga MX |
| 2 | ¿Quién la controla hoy? | FMF, Liga MX, SAT, FIFA y el proveedor de datos de apuestas contratado, cada uno de forma independiente |
| 3 | ¿Por qué no cumple su función? | No porque falte la facultad, sino porque no hay protocolo común de aviso/escalamiento entre ellas — el problema es de coordinación, no de facultad |
| 4 | ¿Por qué no puede reformarse en lugar de sustituirse? | No se sustituye nada; el protocolo no reemplaza ninguna facultad, solo la conecta |
| 5 | ¿Cuánto costaría reformarla? | No aplica — no se reforma ninguna institución, se documenta un flujo de coordinación entre las existentes |
| 6 | ¿Cuánto costaría sustituirla? | No aplica — no hay sustitución |
| 7 | ¿Qué funciones asumiría la nueva estructura? | Ninguna función decisoria propia; es un documento de coordinación (protocolo), no un ente con facultades |
| 8 | ¿Qué institución dejaría de cumplir esas funciones? | Ninguna — todas conservan sus facultades actuales |
| 9 | ¿Cómo se evitaría la duplicidad? | El protocolo existe precisamente para evitarla, fijando una sola vía de escalamiento por tipo de caso |
| 10 | ¿Cómo se financiaría de forma permanente? | Costo administrativo bajo (redacción y firma de un convenio/memorando, no una operación nueva); no requiere presupuesto recurrente propio — ver sección 18 |
| 11 | ¿Cómo se evaluaría? | Con los indicadores de la sección 23 (número de casos enrutados correctamente, tiempo de respuesta, ausencia de casos "perdidos" entre instituciones) |
| 12 | ¿Quién la supervisaría? | Cada institución firmante supervisa su propio tramo; el Agente 0 (o su sucesor de integración) supervisa la coherencia del conjunto en la siguiente revisión |
| 13 | ¿Bajo qué condiciones podría cerrarse? | Si alguna de las instituciones firmantes deja de existir o cambia de facultades (p. ej., si la separación Liga MX-FMF de abril 2026 reconfigura competencias), el protocolo se renegocia, no se necesita "cerrarlo" como a una institución |
| 14 | ¿Qué riesgo tiene de ser capturado por intereses particulares? | Bajo, porque no administra presupuesto ni tiene poder de decisión propio; el riesgo de captura recae en las instituciones que sí deciden (FMF, Liga MX), ya analizado por el Agente 2 (mapa de poder) |

---

## 16. Recomendación

Organizadas por componente, con prioridad y lado de la línea D-03 explícito (**[Ley general — permitido]** vs. **[Autorregulación privada FMF/Liga MX — no es intervención estatal]**):

**A. Protección de menores**
1. **[Prioridad alta] [Autorregulación privada]** La Comisión Disciplinaria de la FMF adopta un procedimiento escrito: toda denuncia recibida por SIPINNA/Procuraduría vía el convenio del Pilar 2 dispara un expediente paralelo en la FMF, con plazo máximo de 60 días naturales para resolución y catálogo de sanciones a academias (amonestación, suspensión de afiliación, desafiliación) según gravedad.
2. **[Prioridad alta] [Ley general — permitido]** El convenio FMF-SIPINNA (Pilar 2) incluye cláusula expresa de protección contra represalia laboral para quien denuncie, apoyada en las protecciones ya existentes de la Ley Federal del Trabajo contra despido injustificado.

**B. Árbitros y VAR**
3. **[Prioridad media] [Autorregulación privada]** Ampliar el mandato escrito del Comité de Evaluación de árbitros (ya creado, octubre 2025) para incluir explícitamente "presión externa indebida" como categoría de reporte, con ruta de escalamiento a la Comisión Disciplinaria.
4. **[Prioridad media] [Autorregulación privada]** Publicar anualmente (sin exponer casos individuales) el número de reportes de presión externa recibidos y resueltos, como indicador de transparencia del propio sistema arbitral.

**C. Apuestas y amaño**
5. **[Prioridad alta] [Autorregulación privada + alianza comercial]** Verificar la vigencia de la alianza de monitoreo de apuestas (Genius Sports u otro proveedor) y formalizar por escrito su protocolo de escalamiento (patrón que dispara alerta → Comisión Disciplinaria FMF → plazo de resolución → sanción según Art. 11 del Código de Ética, ya vigente).
6. **[Prioridad alta] [Ley general — permitido]** Establecer, vía memorando de entendimiento (no ley), un canal de intercambio de alertas entre el proveedor de monitoreo de apuestas, la Dirección General de Juegos y Sorteos (SEGOB, regulador de casas de apuestas legales) y la UIF (receptor ya obligatorio de reportes de "actividad vulnerable" de casas de apuestas bajo la LFPIORPI) — aprovecha tres piezas regulatorias públicas ya existentes sin crear una nueva.
7. **[Prioridad media] [Autorregulación privada]** Extender/verificar la cobertura de monitoreo a Liga Premier, Liga de Expansión y Liga MX Femenil, categorías donde se concentran los casos detectados recientemente.

**D. Agentes/representantes**
8. **[Prioridad media] [Autorregulación privada]** Hacer público y consultable el registro de agentes/intermediarios de la FMF (nombre, jugadores representados, club), vinculándolo al SIID ya existente para transferencias domésticas.
9. **[Prioridad baja] [Autorregulación privada]** Adoptar, en el Reglamento Nacional sobre Agentes de Fútbol de la FMF, el estándar ya confirmado por el TJUE en julio de 2026 (licencia obligatoria, tope de comisión), y suspender/revisar cualquier disposición equivalente a la regla de los dos meses que el mismo TJUE invalidó.

**E. Transparencia de propiedad de clubes**
10. **[Prioridad alta] [Ley general — permitido]** Convenio de intercambio de información entre SAT (beneficiario controlador, obligatorio desde 2022) y la FMF (padrón de propietarios de clubes), con escalamiento a COFECE (requerimiento de información, Art. 34 LFCE) si existe discrepancia no explicada — aplica directamente al caso Grupo Caliente sin necesidad de ley nueva ni de que el Estado intervenga en la gobernanza de la FMF.
11. **[Prioridad media] [Ley general — permitido]** Solicitar a COFECE (recomendación ya hecha por el Agente 3) actualizar su postura sobre multipropiedad de clubes, aprovechando la misma facultad y precedente de 2021.

**F. Protección de denunciantes**
12. **[Prioridad alta] [Autorregulación privada + adopción de sistema FIFA]** La FMF/Liga MX publicitan activamente, en español, el canal BKMS de FIFA como vía independiente de denuncia de integridad deportiva de adultos, en comunicaciones oficiales dirigidas a jugadores, árbitros, entrenadores y personal de academias.
13. **[Prioridad alta] [Ley general — permitido]** El convenio FMF-SIPINNA (Pilar 2) es, para menores, el canal ya diseñado; este documento solo añade la cláusula de protección contra represalia laboral (recomendación 2).

**G. Auditorías y transparencia financiera**
14. **[Prioridad alta] [Autorregulación privada]** El Comité de Certificación, Ética y Buen Gobierno de Liga MX (ya creado, mandato operativo por definir) adopta como primer mandato explícito la publicación de un resumen financiero anual auditado por despacho externo, de Liga MX y sus 18 clubes — formalizando como práctica institucional lo que hoy solo Apollo exige como condición de inversión privada.
15. **[Prioridad media] [Ley general — permitido]** Si la vía voluntaria (recomendación 14) no se ejecuta en un plazo razonable (sugerido: 24 meses desde la formalización de este protocolo), activar la facultad de estudio de mercado y requerimiento de información de COFECE (Art. 12-XX y 34 LFCE) como mecanismo de última instancia — misma facultad, mismo estándar D-03, ya ejercida sin reacción de FIFA en 2021.

---

## 17. Responsable

FMF (Comisión Disciplinaria, Comisión de Árbitros, Dirección Jurídica/Secretaría General para la coordinación del Protocolo Nacional de Integridad) para las recomendaciones 1, 3, 4, 5, 8, 9, 12; Liga MX (Comité de Certificación, Ética y Buen Gobierno) para las recomendaciones 14 y 7; SAT y COFECE para las recomendaciones 10, 11, 15; Pilar 2 (Marco jurídico) para las recomendaciones 2 y 13, en coordinación con este documento; Agente 0 (o su función de integración sucesora) para reconciliar este documento con los cierres paralelos de Gobernanza y Marco jurídico.

## 18. Costo

`[ESTIMACIÓN]`, nivel de confianza C-D (no hay cifra oficial, análogo al criterio ya usado por el Agente 14 para partidas de coordinación/convenio): las recomendaciones de coordinación (1, 3, 6, 10, 12) son de costo bajo — redacción de protocolos/convenios y ajuste de reglamentos internos, sin presupuesto recurrente propio, comparable a las partidas de "bajo costo directo" que el Agente 3 estimó para su convenio FMF-SIPINNA. La recomendación 14 (auditoría externa anual de Liga MX/18 clubes) es la única con costo directo estimable por analogía: el propio Agente 14 costeó auditorías externas de academias en $8,000-18,000 MXN por visita (confianza D); una auditoría financiera institucional de Liga MX/clubes es de naturaleza distinta (estados financieros completos, no cumplimiento de programa) y no tiene ancla de mercado verificada en este ejercicio — se marca como **no costeado en firme**, en la misma categoría que los cinco rubros ya señalados por el Agente 14 como condicionados a resolver la opacidad financiera. Corresponde al Agente 14 (en su próxima recalibración, ya prevista para el año 2 según su propia recomendación 6) incorporar esta partida una vez exista una cotización real.

## 19. Tiempo

`[ESTIMACIÓN]`, nivel de confianza C: protocolos de coordinación (recomendaciones 1, 3, 6, 8, 10, 12) — 3 a 9 meses, comparable al calendario de convenios estimado por el Agente 3; publicación del resumen financiero anual de Liga MX (recomendación 14) — depende de que el Comité de Certificación, Ética y Buen Gobierno defina su mandato operativo (sección 8, limitación), estimado en 12-24 meses; activación de la vía COFECE como última instancia (recomendación 15) — condicionada a que la vía voluntaria no se cumpla en 24 meses.

## 20. Dependencias

- Que el Pilar 2 (Marco jurídico) formalice efectivamente el convenio FMF-SIPINNA — supuesto de coordinación no verificado por este documento (sección 4).
- Que el Pilar 1 (Gobernanza) no rediseñe la relación FMF-Liga MX de forma que invalide los roles asignados aquí a la Comisión Disciplinaria de la FMF y al Comité de Certificación, Ética y Buen Gobierno de Liga MX.
- Verificación de vigencia y cobertura real de la alianza de monitoreo de apuestas (Genius Sports u otro), pendiente de confirmación directa con Liga MX.
- Verificación de si la FMF/clubes ya cumplen la obligación de beneficiario controlador ante el SAT, pendiente de solicitud de información.
- El propio Protocolo Nacional de Integridad depende de la voluntad de firma de todas las instituciones involucradas (FMF, Liga MX, SAT, COFECE, SEGOB/DGJS) — ninguna tiene obligación legal de suscribirlo, es un mecanismo de coordinación voluntario por diseño (para no cruzar el estándar D-03).

## 21. Riesgos

Ver sección "Supuestos y riesgos nuevos identificados" al final de este documento.

## 22. Bloqueadores

- Falta de voluntad de la FMF/Liga MX para publicar registros (agentes, propiedad de clubes) o estados financieros, dado que no existe obligación legal de transparencia plena sobre estos temas al ser asociaciones privadas — el mismo bloqueador ya señalado por el Agente 3 para el reglamento de agentes.
- Que el "Comité de Certificación, Ética y Buen Gobierno" de Liga MX, cuyo mandato operativo aún no está definido (hallazgo 5.7.30), termine sin facultad real de exigir auditoría a los 18 clubes si la negociación de capital con Apollo no se concreta y pierde su principal palanca de presión.
- Sensibilidad política y económica de cruzar el registro de propiedad de clubes contra el beneficiario controlador fiscal, en particular en el caso Grupo Caliente, dado el peso mediático y político de la persona involucrada (ya señalado por el Agente 2, mapa de poder).
- Que la alianza de monitoreo de apuestas no esté, en la práctica, vigente o cubriendo categorías inferiores — bloqueador que solo se puede confirmar con información directa de Liga MX, no disponible en esta ronda.
- Cualquier intento de convertir el Protocolo Nacional de Integridad en un organismo con facultad decisoria propia (en vez de coordinación) cruzaría el estándar D-03 si se hiciera por mandato público — el diseño de este documento lo evita deliberadamente, pero una implementación descuidada podría no respetar esa línea.

## 23. Indicadores

- Número de casos de protección de menores recibidos por SIPINNA/Procuradurías vía el convenio con la FMF, y proporción resuelta dentro del plazo de 60 días fijado en la recomendación 1 (fuente: FMF/SIPINNA, frecuencia trimestral).
- Número de reportes de presión externa sobre árbitros recibidos y resueltos por el Comité de Evaluación (fuente: Comisión de Árbitros FMF, frecuencia anual) — hoy inexistente como indicador; su sola publicación sería ya un avance de transparencia.
- Número de alertas de patrones anómalos de apuesta generadas por el proveedor de monitoreo, número escaladas a la Comisión Disciplinaria, y número de sanciones resultantes (fuente: FMF/proveedor de monitoreo, frecuencia anual).
- Publicación (sí/no) del registro consultable de agentes/intermediarios de la FMF (fuente: FMF, frecuencia: verificación única tras publicación, luego seguimiento anual).
- Resultado de la verificación cruzada beneficiario controlador (SAT) vs. padrón de propiedad de clubes (FMF): número de discrepancias detectadas, número resueltas, número escaladas a COFECE (fuente: convenio SAT-FMF-COFECE, frecuencia anual).
- Publicación (sí/no) del resumen financiero anual auditado de Liga MX y sus 18 clubes por el Comité de Certificación, Ética y Buen Gobierno (fuente: Liga MX, frecuencia anual) — el indicador de mayor peso de este documento, directamente ligado al riesgo transversal ya identificado por el Agente 14.
- Ausencia de cartas de advertencia o suspensión de FIFA/Concacaf a México durante la implementación de cualquiera de estos mecanismos (mismo indicador ya fijado por el Agente 3, reutilizado aquí porque el criterio D-03 aplica igual a este pilar).

## 24. Casos internacionales

No aplica de forma sistemática en este entregable — corresponde a la Fase 4 (Agentes 5A-5E), ya cerrada, que no tuvo a Integridad como pilar de enfoque explícito en ninguno de sus cinco bloques regionales (vacío de benchmark, ver sección 26). El único caso comparativo usado en este documento es transversal: el sistema BKMS de FIFA (sección 5.6.24), que por operar globalmente es directamente aplicable a México sin necesidad de adaptación regional, y el criterio de injerencia FIFA (Kuwait, Indonesia, Pakistán, Guatemala, Kenia, Nepal, Chile 2025) ya sistematizado por el Agente 3 y adoptado como D-03, que se reutiliza aquí sin repetir la evidencia completa.

## 25. Adaptación a México

`[INFERENCIA]` El patrón más directamente adaptable es el propio patrón mexicano ya en marcha, no uno extranjero: la condición de auditoría que Apollo Global Management exige como parte de su negociación de capital (sección 5.7.28) es, en sustancia, el mismo estándar de transparencia financiera que un regulador público impondría — la adaptación recomendada no es "copiar" un modelo de otro país, sino **formalizar como práctica institucional permanente** una exigencia que el propio mercado de capital ya está imponiendo a México, antes de que dependa exclusivamente de que esa negociación específica se concrete.

## 26. Preguntas pendientes

Ver sección siguiente.

---

## Preguntas nuevas para el registro maestro

| ID | Pregunta | Fuente esperada | Estado |
|---|---|---|---|
| PQ-14-01 | ¿Sigue vigente en 2026 la alianza Liga MX-Genius Sports (o equivalente) para monitoreo de apuestas, y cubre con la misma intensidad a Liga Premier, Expansión MX y Liga MX Femenil, donde se concentran los casos de manipulación recientemente detectados? | Liga MX, proveedor de monitoreo | Pendiente |
| PQ-14-02 | ¿Es públicamente consultable el registro/carné de agentes e intermediarios de la FMF, y cuántos agentes operan formalmente licenciados en México a julio de 2026 (para actualizar la cifra potencialmente desactualizada de "111 agencias, 12 con licencia FIFA")? | FMF (Reglamento Nacional sobre Agentes de Fútbol) | Pendiente |
| PQ-14-03 | ¿Cumple la FMF y cada uno de los 18 clubes de Liga MX con la obligación de beneficiario controlador ante el SAT (Art. 32-B Ter CFF), y coincide esa información con el padrón de propiedad de clubes que administra la FMF, específicamente en el caso de Xolos de Tijuana/Grupo Caliente? | SAT, FMF | Pendiente |
| PQ-14-04 | ¿Qué mandato operativo tiene, en la práctica (no solo en el anuncio de abril de 2026), el Comité de Certificación, Ética y Buen Gobierno de Liga MX, y ha ordenado o recibido ya alguna auditoría externa de los 18 clubes? | Liga MX | Pendiente |
| PQ-14-05 | ¿Existe un protocolo escrito de reporte de presión externa indebida sobre árbitros dentro de la Comisión de Árbitros de la FMF, distinto de la evaluación de desempeño técnico? | FMF, Comisión de Árbitros | Pendiente |
| PQ-14-06 | ¿Ha recibido la FMF o algún jugador/entrenador/árbitro mexicano alguna denuncia procesada vía el sistema BKMS de FIFA, y existe algún protocolo de coordinación entre FIFA y la FMF cuando esto ocurre? | FIFA (Departamento de Integridad), FMF | Pendiente |
| PQ-14-07 | ¿Qué contenido específico tiene el Reglamento Nacional sobre Agentes de Fútbol de la FMF (2023) respecto a tope de comisión, doble representación y régimen sancionador, y lo ha actualizado la FMF tras la sentencia del TJUE de julio de 2026? | FMF | Pendiente |
| PQ-14-08 | ¿Ha recibido la Dirección General de Juegos y Sorteos (SEGOB) o la UIF alguna vez un reporte de patrón de apuesta anómalo vinculado a un partido de fútbol mexicano, y qué protocolo existe (si alguno) para compartir esa alerta con la FMF? | SEGOB/DGJS, UIF | Pendiente |

## Supuestos y riesgos nuevos identificados

### Supuestos nuevos

| ID | Supuesto | Justificación | Sensibilidad | Consecuencia si es falso | Validación requerida |
|---|---|---|---|---|---|
| S-14-01 | El Pilar 2 (Marco jurídico), en su ronda de cierre paralela a esta, formaliza efectivamente el convenio FMF-SIPINNA como instrumento legal de protección de menores, tal como fue instruido a este documento asumir | Instrucción explícita de la misión de esta ronda | Alta — si el Pilar 2 no lo formaliza o lo diseña de forma distinta, todo el componente A (protección de menores) de este documento pierde su base legal asumida | Reconciliar contra el entregable real del Pilar 2 en la siguiente integración del Agente 0 |
| S-14-02 | Es posible usar la obligación fiscal de beneficiario controlador (SAT), las facultades de requerimiento de información de COFECE, y la regulación de casas de apuestas (SEGOB/DGJS) y prevención de lavado (UIF) como palancas de integridad deportiva sin activar el mecanismo de no injerencia de FIFA, por ser todas leyes de aplicación general (fiscal, competencia económica, juegos y sorteos, prevención de lavado), no específicas del deporte | Extensión directa del criterio D-03 ya adoptado por el Agente 0 a partir del precedente COFECE 2021 | Alta — si FIFA interpretara de forma más amplia qué cuenta como injerencia, este documento completo (componentes C, E, G) quedaría en riesgo | Monitorear cualquier reacción de FIFA/Concacaf durante la implementación, igual que el Agente 3 recomendó para su propio criterio |
| S-14-03 | La alianza de monitoreo de apuestas Liga MX-Genius Sports (o un proveedor equivalente) sigue vigente y operando en 2026 | Único hallazgo verificado data de noviembre de 2020; no se encontró confirmación de renovación o continuidad hasta julio de 2026 | Alta — si ya no está vigente, la recomendación 5 pasa de "formalizar" a "recontratar", con costo e implicación distintos | Confirmación directa con Liga MX antes de ejecutar la recomendación 5 |
| S-14-04 | El "Comité de Certificación, Ética y Buen Gobierno" de Liga MX, aunque sin mandato operativo definido a julio de 2026, es la instancia correcta —y no otra por crear— para asumir la función de auditoría financiera institucional | Es la única estructura de gobierno corporativo de Liga MX explícitamente orientada a ética/transparencia ya creada (abril 2026) | Media-Alta — si ese comité resulta ser solo nominal (como sugiere la nota de julio 2026 sobre el "Comité Deportivo... sigue sin definirse"), la recomendación 14 necesitaría replantearse sobre otra instancia ya existente, no una nueva | Verificar el estatuto/reglamento interno del comité en cuanto se publique |

### Riesgos nuevos

| Riesgo | Probabilidad | Impacto | Señal temprana | Responsable | Mitigación | Contingencia |
|---|---|---|---|---|---|---|
| El Protocolo Nacional de Integridad (sección 12) queda como documento firmado sin ejecución real, porque ninguna de las instituciones involucradas tiene obligación legal de cumplirlo (es voluntario por diseño, para no cruzar D-03) | Media-Alta | Alto — reproduciría exactamente el patrón ya documentado por el Agente 2 de que Liga MX ignoró una resolución del TAS cuando no convenía a sus intereses | Ausencia de reportes anuales de los indicadores de la sección 23 dentro de los primeros 12 meses | Agente 0 (integración), Agente 16 (Red Team) | Vincular el cumplimiento del protocolo a la condicionalidad de beneficios públicos/legado del Mundial 2026 (mecanismo ya identificado por el Agente 3, PQ-C08) como palanca adicional de cumplimiento sin necesidad de ley nueva | Escalar a COFECE (recomendación 15) si la vía voluntaria de auditoría (recomendación 14) no se cumple en 24 meses |
| La verificación cruzada de propiedad de clubes (beneficiario controlador SAT vs. padrón FMF) expone información fiscal sensible sin el marco de confidencialidad adecuado, generando litigio o resistencia legal de los grupos propietarios | Media | Medio-Alto | Amparos o solicitudes de confidencialidad ante cualquier intento de cruce de información | SAT, COFECE, Agente 3 (seguimiento jurídico) | Diseñar el convenio de intercambio de información (recomendación 10) para que solo confirme "coincide/no coincide" sin exponer el detalle fiscal completo, similar a los mecanismos de verificación de identidad que no revelan datos subyacentes | Limitar el alcance inicial del cruce a casos ya mediáticamente documentados (Grupo Caliente) antes de generalizarlo |
| El canal BKMS de FIFA, al ser gestionado directamente por FIFA y no por una autoridad mexicana, podría no dar seguimiento efectivo a denuncias de bajo perfil mediático de México, dejando un vacío real de protección pese a la existencia formal del canal | Media | Alto — si el canal recomendado (F) resulta inefectivo en la práctica, la protección de denunciantes de integridad deportiva de adultos queda, de nuevo, sin vía real | Ausencia de casos mexicanos documentados públicamente como procesados vía BKMS en los primeros 24 meses | FMF, Agente 16 (Red Team) | Monitorear el volumen y resultado de denuncias mexicanas vía BKMS y, si resulta inefectivo, escalar la necesidad de un canal doméstico complementario como pregunta para una futura ronda de diseño (no resuelto por este documento) | Usar el mismo mecanismo de protección laboral de la recomendación 2, extendido a integridad de adultos, como respaldo mientras se evalúa BKMS |
| La cifra de riesgo de apuestas (~4,857 millones USD/año, fuente comercial Sportradar) se usa en discusiones públicas sin la advertencia de nivel C y conflicto de interés potencial del proveedor, inflando la percepción de urgencia y presionando hacia soluciones más caras de lo necesario | Baja-Media | Medio | Uso de la cifra en presentaciones o presupuestos sin la calificación de nivel C ya hecha en este documento | Agente 0, Agente 16 | Mantener la etiqueta de nivel C explícita en cualquier reutilización de la cifra (sección 6, E3) | Solicitar la metodología completa a Sportradar antes de usarla como base de cualquier decisión presupuestal |

---

**Nota de cierre para integración:** este documento no debe editarse en los archivos maestros compartidos (`00`-`07`) para evitar conflictos con los otros dos agentes de esta ronda de cierre (Gobernanza — Pilar 1, y Marco jurídico — Pilar 2), que trabajan en paralelo. Las preguntas y los supuestos/riesgos nuevos aquí listados, junto con el supuesto de coordinación S-14-01 (que depende directamente de lo que el Pilar 2 entregue), deben ser incorporados y reconciliados por el Agente 0 (o su función de integración sucesora) en la próxima ronda de integración, antes de que el Agente 16 (Red Team) evalúe el proyecto completo.
