# Fase 8 — Agente 16: Red Team
## Crítica independiente del diseño construido en Fases 1–7

**Fecha de revisión:** 2026-07-25
**Insumos recibidos:** paquete completo de traspaso descrito en `10-fase6b-integracion-pilares-faltantes.md`, sección 5 — metodología (`00`), línea base consolidada (`05`) y sus registros (`03`, `04`, `06`, `07`), benchmark consolidado (`08`), integración de diseño (`09`, `10`), los 13 entregables de pilar (`fase5-agente6` a `13`, `fase5b-pilar1/2/6/7/14`), y los dos entregables de Fase 7 (`fase7-agente14-finanzas.md`, `fase7-agente15-implementacion.md`).
**Función de este documento:** cerrar el Control 7 (Red Team) — atacar el proyecto ya construido, no defenderlo. Cada crítica cierra con problema, evidencia, gravedad, consecuencia, corrección propuesta y veredicto (**mantener** / **modificar** / **eliminar**) sobre la recomendación criticada.

---

## 1. Resumen ejecutivo

Este proyecto es inusualmente autocrítico: buena parte de las fallas que un Red Team típico señalaría primero (opacidad financiera como riesgo transversal, advertencia contra depender de la buena voluntad de la Asamblea de Dueños, prohibición de lugares comunes, disciplina de niveles de evidencia A–D) ya fueron declaradas explícitamente por sus propios agentes, con lenguaje casi idéntico al que usaría este Red Team. Eso reduce el número de críticas "de bulto" disponibles, pero no elimina el trabajo: quedan **quince críticas sustantivas**, la mayoría sobre supuestos no verificados que el proyecto reconoce como abiertos pero trata, en la práctica, como si estuvieran resueltos al secuenciar y calendarizar sobre ellos; sobre una desincronización real de proceso entre las Fases 5b/6b/7 que deja el presupuesto y el cronograma incompletos justo al llegar a este control; y sobre el hecho de que la "advertencia central" del propio proyecto (ninguna reforma puede depender de que la Asamblea de Dueños decida portarse bien) se cumple en el diseño de secuenciación, pero no en el fondo: las piezas que sí requieren el voto de la Asamblea —el fondo con dinero, la transparencia financiera de Liga MX, la cláusula TAS, la redistribución hacia el fútbol femenil— siguen sin ningún mecanismo vinculante real, solo presión reputacional y la esperanza de que el capital privado (Apollo) empuje en la misma dirección que el proyecto.

**Las tres críticas más graves** (detalladas abajo): (1) toda la estrategia de secuenciación de 20 años descansa en un supuesto —que la Asamblea de Dueños no tiene poder de veto sobre los reglamentos de la FMF— que dos agentes distintos (15 y Pilar 1) marcan como "de sensibilidad muy alta" y dejan sin verificar; (2) el Programa de Transparencia Financiera, la pieza de la que depende casi todo lo demás según el propio `10`, es voluntario, agregado y sin mecanismo de cumplimiento real para Liga MX; y (3) el presupuesto (Agente 14) y el cronograma (Agente 15) que llegan a este Red Team **no incluyen** las recomendaciones de los cinco pilares diseñados después de ellos (1, 2, 6, 7, 14) — el proyecto se presenta a Control 7 con dos de sus documentos de cierre más importantes desactualizados por construcción.

**Veredicto general (sección final):** el proyecto **no pasa el Control 7 tal como está** — no porque el diseño sea deficiente en su mayoría (no lo es), sino porque tiene un vacío de proceso concreto y verificable (crítica 3) que el propio manual metodológico definiría como bloqueador del control, y porque al menos dos supuestos de máxima sensibilidad (críticas 1 y 2) se están usando como base de secuenciación sin la validación que el propio proyecto se exigió a sí mismo. Ninguna de las quince críticas amerita **eliminar** una recomendación completa; la mayoría son **modificar** con corrección concreta y plazo, lo cual es coherente con que la Fase 9 ("Corrección del borrador") ya estaba prevista en el propio calendario del Agente 0.

---

## 2. Metodología de revisión

Siguiendo la instrucción de la misión, no se releyeron línea por línea los ~30 documentos de línea base, benchmark y diseño (miles de líneas). Se leyeron completos los ocho documentos de integración/metodología (`00`, `05`, `06`, `07`, `08`, `09`, `10`, `04`) y ambos entregables de Fase 7 (`fase7-agente14`, `fase7-agente15`) en su totalidad. Para los 13 pilares de diseño (`fase5-agente6` a `13`, `fase5b-pilar1/2/6/7/14`) se leyeron específicamente las secciones 1 (resumen ejecutivo), 15/15bis (necesidad de nueva capacidad), 16 (recomendación) y 21 (riesgos) de cada uno, que en este proyecto son suficientes: cada agente de diseño ya declara ahí su propio nivel de confianza, sus condicionantes y sus riesgos reconocidos, lo que permite verificar si el propio proyecto respetó sus propias advertencias sin necesidad de leer las 21 secciones completas de cada entregable.

Cada crítica de la sección 3 cita el documento y, cuando aplica, la sección exacta de la que proviene la evidencia — no se aceptaron críticas genéricas ("el presupuesto parece bajo") sin anclaje textual. Se priorizaron 15 críticas sustantivas sobre un número mayor de objeciones superficiales, conforme a la regla de la misión.

---

## 3. Registro de críticas

### Crítica 1 — La premisa de la que depende toda la secuencia de implementación no está verificada, y dos agentes distintos ya advirtieron que si es falsa, hay que rediseñar todo

**Problema:** El cronograma completo de 20 años (`fase7-agente15`) y el diseño de gobernanza (Pilar 1) reposan en el supuesto S-I01: que la mayoría de las reformas prioritarias (certificación de academias, licencias, SIID, convenios) son competencia reglamentaria propia de la FMF y **no requieren** el voto de la Asamblea de Dueños de Liga MX, incluso cuando se aplican a clubes de Liga MX. Este supuesto es el fundamento cuantitativo de toda la "estrategia de coalición" (sección 19.2 de `fase7-agente15`) y de la matriz de dependencia del Pilar 1 (sección 16.1).

**Evidencia:** `fase7-agente15-implementacion.md`, sección "Supuestos y riesgos nuevos", S-I01 ("sensibilidad: Muy alta — es la base de toda la secuencia de este documento") y el riesgo asociado ("Que la premisa central... resulte falsa... obligando a rediseñar la secuencia completa de implementación", probabilidad Media, impacto "Muy alto"). La misma incertidumbre reaparece, sin resolverse, en `fase5b-pilar1-gobernanza.md`, sección 20 ("Resolución de si la Asamblea General de la FMF puede reformar su propio Estatuto sin requerir aprobación de la Asamblea de Dueños de Liga MX (supuesto nuevo de este documento)"). Es decir: dos agentes, en dos momentos distintos del proyecto, tropiezan con la misma pregunta sin resolverla — y ambos siguen diseñando sobre el supuesto favorable.

**Gravedad:** Crítica (la más alta del documento). No es un supuesto secundario: si es falso, invalida la lógica de secuenciación de 11 de 15 clústeres de acción del cronograma general y de 8 de 10 líneas del Pilar 1.

**Consecuencia si no se corrige:** El proyecto podría ejecutar dieciocho meses de "año 1" (certificaciones, comités, convenios) creyendo que avanza sin necesitar a la Asamblea, y descubrir a mitad de camino que Liga MX puede bloquear retroactivamente cualquier reglamento de la FMF que le aplique a sus 18 clubes — obligando a renegociar desde una posición más débil que si se hubiera sabido desde el inicio.

**Corrección propuesta:** Responder PQ-I05 (verificación directa del Estatuto Social de la FMF y del nuevo estatuto de Liga MX, abril 2026) como la primera acción del proyecto, antes de cualquier otra del "año 1" — no en paralelo, como sugiere el propio riesgo ya registrado. Mientras no se responda, todo el cronograma debe presentarse con una nota de contingencia explícita: "secuencia válida solo bajo S-I01; ver plan B si se refuta."

**Veredicto: modificar.** La estrategia de secuenciación (explotar la asimetría de autoridad) es la decisión de diseño más inteligente de todo el proyecto y no debe abandonarse — pero no puede presentarse como un hecho fijado; debe presentarse condicionada, con la verificación de PQ-I05 como bloqueador explícito del inicio real de ejecución, no como una tarea más del año 1.

---

### Crítica 2 — El Programa de Transparencia Financiera, la pieza de la que depende casi todo lo demás, no tiene mecanismo de cumplimiento real para Liga MX

**Problema:** `10-fase6b-integracion-pilares-faltantes.md` (sección 5) instruye explícitamente al Red Team a evaluar "con especial rigor si es realista que ambos brazos (FMF y Liga MX) lo adopten voluntariamente" el Programa de Transparencia Financiera, del que dependen el fondo con dinero del Pilar 6, la redistribución hacia el fútbol femenil (Pilar 13) y la credibilidad de los Pilares 1 y 14. La respuesta, tras revisar el diseño: para el brazo FMF/ligas menores sí hay mecanismo (Comité de Inversión y Certificación, sin necesitar Asamblea); para el brazo Liga MX, el único mecanismo no voluntario es el Club Licensing System de Concacaf/FIFA — que exige transparencia agregada solo como condición de licencia continental, no como obligación doméstica general — y el propio Pilar 1 ya advierte que el nivel de agregación permitido ("no exponer información competitivamente sensible en la primera fase") podría ser insuficiente para lo que el Agente 14 necesita para desbloquear sus cinco rubros condicionados.

**Evidencia:** `fase5b-pilar1-gobernanza.md`, sección 21, riesgo: "El estándar mínimo de transparencia financiera agregada resulta insuficiente para desbloquear los cinco rubros presupuestales... si el nivel de agregación es demasiado alto, no genera la verificabilidad real que el Agente 14 necesita" (probabilidad Media, impacto Alto). `fase7-agente14-finanzas.md`, sección 11: "Falta de respuesta de FMF/Liga MX a solicitudes de transparencia... es el riesgo financiero más determinante de todo el proyecto." La auditoría financiera institucional de Liga MX/18 clubes (Pilar 14, recomendación 14) ni siquiera tiene costo estimado — sección 18 de `fase5b-pilar14-integridad.md` la marca "no costeada en firme", en la misma categoría que los rubros que ella misma debería desbloquear.

**Gravedad:** Crítica. Es un punto único de fallo con al menos tres consecuencias en cascada (fondo Pilar 6, fondo femenil Pilar 13, escenario transformador del Agente 14).

**Consecuencia si no se corrige:** El proyecto podría cumplir "en el papel" (publicar un resumen financiero agregado mínimo) sin resolver la opacidad real, dando la apariencia de que la condición de desbloqueo se cumplió cuando en realidad no aporta la verificabilidad que los otros tres pilares necesitan — exactamente el patrón de "reforma de papel" que el propio benchmark (`08`, sección 4) identificó como la causa más común de fracaso.

**Corrección propuesta:** Fijar, antes de la Fase 9, el nivel mínimo de desagregación que el Agente 14 necesita para considerar "cumplida" la condición de desbloqueo (no dejarlo abierto a que Liga MX decida su propio estándar de agregación) y establecer que la auditoría financiera institucional de Liga MX (Pilar 14, recomendación 14) tenga plazo y consecuencia explícitos si no se ejecuta en 24 meses (ya sugerido, pero como "recomendación media", no como condición dura).

**Veredicto: modificar.** El diseño en dos brazos (FMF + Liga MX) es razonable; lo que falta es una definición operacional de "transparencia suficiente" acordada entre el Pilar 1 y el Agente 14 antes de que cualquier fondo condicionado se dé por desbloqueable.

---

### Crítica 3 — El presupuesto y el cronograma que llegan a este Red Team no incluyen los cinco pilares diseñados después de ellos

**Problema:** `fase7-agente14-finanzas.md` (23-jul-2026) y `fase7-agente15-implementacion.md` (24-jul-2026) se completaron **antes** de que `fase5b-pilar1/2/6/7/14` (24–25-jul-2026) cerrara el vacío de diseño de Gobernanza, Marco jurídico, Reforma de competencias, Exportación e Integridad. El propio `09` (sección 8) había pedido que ese vacío se cerrara "antes del inicio del Año 1... no en paralelo con el Red Team" para que este control no evaluara "un proyecto con dos pilares completos de vacío de diseño" — pero nadie regresó a actualizar el presupuesto ni el cronograma con las ~40 recomendaciones nuevas de esos cinco pilares una vez diseñados.

**Evidencia:** `fase5b-pilar1-gobernanza.md`, sección 16.1: "deben incorporarse a la matriz RACI de `fase7-agente15-implementacion.md`, sección 19.1, **en la próxima actualización de ese documento**" (no ha ocurrido). Sección 18 del mismo documento: "No se estima una cifra consolidada en este documento porque corresponde al Agente 14... integrarla en su próximo ciclo de recalibración presupuestal (ya programado para el año 2)" — es decir, el propio Pilar 1 admite que su costo no está en ningún presupuesto vigente hasta dentro de dos años. Lo mismo ocurre, con idéntico lenguaje, en `fase5b-pilar6-reforma-competencias.md` (sección 18) y no se verificó lo contrario en Pilar 2, 7 y 14.

**Gravedad:** Crítica. No es un defecto de contenido sino un defecto de proceso que el propio manual metodológico (Control 6: "inversión, operación, fuente permanente, sensibilidad") y Control 4 exigen resuelto antes de avanzar — y once acciones nuevas de gobernanza/integridad (Carta de Funciones, regla de enfriamiento, Comité de Ética FMF, registro de beneficiario final, licencia de directivo, criterios del sistema de certificación, Protocolo Nacional de Integridad) compiten, sin estar calendarizadas, por el mismo "año 1" ya saturado que diseñó el Agente 15 para los ocho pilares originales.

**Consecuencia si no se corrige:** El documento ejecutivo final (Fase 10, Agente 17) podría presentar un presupuesto y un cronograma que se leen como completos pero que estructuralmente excluyen 5 de 13 pilares — exactamente el riesgo que el propio Agente 14 ya advirtió para otro caso ("que los cinco rubros no costeados se presenten como si ya tuvieran presupuesto resuelto, por presión de mostrar un proyecto completo").

**Corrección propuesta:** Antes de cerrar la Fase 9 (corrección del borrador), el Agente 14 y el Agente 15 deben producir un adendum explícito que (a) integre el costo de las ~40 recomendaciones de los Pilares 1, 2, 6, 7 y 14 al presupuesto de tres escenarios ya existente, y (b) inserte sus acciones de "año 1 sin depender de la Asamblea" (que son numerosas: 8 solo del Pilar 1) en el cronograma de primeros 100 días/año 1 ya saturado, verificando que no haya colisión de capacidad con las 19 acciones que ya tenía asignadas ese mismo periodo (ver Crítica 6).

**Veredicto: modificar.** Es un bloqueador de proceso, no un error de contenido — no invalida ninguna recomendación individual, pero sí invalida la afirmación implícita de que el proyecto "tiene diseño, presupuesto y cronograma completos de los 13 pilares" al llegar a este control.

---

### Crítica 4 — El rubro de mayor magnitud absoluta de todo el presupuesto descansa en tres capas de evidencia débil apiladas, no en una sola

**Problema:** La rehabilitación de patios escolares es, en los tres escenarios del Agente 14, el rubro más grande en pesos absolutos (hasta $810-820M MXN/año en el escenario transformador, de un total de $1,450-1,550M). Esa cifra se construye sobre: (1) una estadística general de INEGI ("32.9% de escuelas sin instalación deportiva") que mide infraestructura deportiva en general, no infraestructura de fútbol específicamente — un salto de categoría que ningún documento del proyecto reconoce explícitamente; (2) un costo unitario ($200,000-$300,000 por escuela) que el propio Agente 14 admite no tiene cotización real del paquete exacto propuesto, solo una inferencia por comparación con canchas completas; y (3) un universo de escuelas no auditado, dependiente de un inventario que todavía no existe.

**Evidencia:** `fase7-agente14-finanzas.md`, Anexo A.1, nota de escala, y sección "Supuestos y riesgos nuevos", S-F14-02: "es el supuesto detrás del rubro de mayor magnitud absoluta de todo el presupuesto; si el costo real es igual o mayor al de una cancha completa, el escenario intermedio podría acercarse al transformador solo en este rubro" (sensibilidad Alta). La fuente de mercado que calibra el costo es "una muestra pequeña y no aleatoria" (sección 8, limitaciones). La cifra de INEGI se hereda sin verificar si mide instalaciones deportivas en general o de fútbol (`fase5-agente9-infraestructura.md`, sección 3, PQ-A02 sigue sin respuesta).

**Gravedad:** Grave. No es que el rubro esté mal calculado dentro de su propia lógica — es que su lógica descansa en tres eslabones débiles simultáneos, cada uno ya señalado por separado por el propio proyecto, pero nunca sumados como un solo riesgo compuesto sobre la partida más grande del presupuesto.

**Consecuencia si no se corrige:** El escenario "intermedio" —el recomendado por el propio Agente 14 como referencia— podría, sin que nadie lo note hasta ejecutarlo, terminar costando lo mismo que el "transformador" únicamente por error en esta partida, distorsionando la comparación de escenarios que el Agente 14 construyó cuidadosamente.

**Corrección propuesta:** Antes de comprometer presupuesto plurianual en este rubro (ya recomendado por el propio Agente 14, sección 11: "cotización real de 10-20 casos piloto... antes de comprometer el escalamiento a 1,000+ escuelas/año"), verificar además si la estadística INEGI del 32.9% es representativa de la necesidad específica de fútbol o si sobreestima/subestima el universo real aplicable.

**Veredicto: modificar.** El propio Agente 14 ya recomienda el piloto de verificación; se agrega aquí la instrucción explícita de verificar también la aplicabilidad de la estadística base, no solo el costo unitario.

---

### Crítica 5 — La advertencia central del benchmark (`08`, sección 4) se cumple en la secuencia, pero no en el fondo: lo que sí depende de la Asamblea sigue sin mecanismo vinculante

**Problema:** La pregunta que el propio proyecto se hizo a sí mismo — ¿el diseño del Pilar 1 tiene dientes reales, o depende de que la Asamblea "decida portarse bien"? — tiene una respuesta mixta. Para el 73-80% de las acciones que **no** requieren a la Asamblea, sí hay mecanismos reales (mandatos FIFA Connect ID, Club Licensing de Concacaf/FIFA, reputación vía boletín). Pero para el subconjunto que sí requiere su voto —reforma del Comité de Ética y Buen Gobierno de Liga MX, cláusula de incorporación vinculante de resoluciones TAS, fondo con dinero, redistribución hacia el fútbol femenil, coeficiente de desarrollo en el reparto de TV—, el único mecanismo de presión es "presentarlo como beneficio de adopción" apostando a que el capital privado (Apollo) valore la señal de buen gobierno. No hay ninguna consecuencia real si la Asamblea simplemente no actúa, más allá del costo reputacional de un boletín trimestral.

**Evidencia:** `fase5b-pilar1-gobernanza.md`, sección 21: "La Asamblea de Dueños de Liga MX bloquea indefinidamente las dos líneas que dependen de su voto... el mismo patrón ya documentado de ignorar al TAS" (probabilidad Alta). La mitigación propuesta es enteramente blanda: "presentarlas como beneficio de adopción... avanzar primero en FMF y ligas menores para generar presión competitiva." `fase7-agente15-implementacion.md`, sección 24, riesgo: "Que el 'efecto demostración' de Expansión MX/Liga Premier/TDP no genere presión competitiva real... si la brecha de recursos entre ligas es demasiado amplia" (probabilidad Media-Alta, impacto Alto) — el propio proyecto reconoce que su plan B para este escenario ("escalar directamente la presión de licencia de club Concacaf/FIFA") solo se activaría en la revisión intermedia del año 9-12, es decir, casi una década después de que el mecanismo hipotéticamente falle.

**Gravedad:** Grave. Es precisamente la advertencia que el proyecto se hizo a sí mismo en `08`, sección 4, y que instruyó como "criterio obligatorio de diseño" para el Pilar 1 y el Pilar 6.

**Consecuencia si no se corrige:** Si el efecto de demostración no funciona (probabilidad ya calificada como Media-Alta por el propio Agente 15), el proyecto podría llegar al año 9-12 sin haber corregido ni la opacidad financiera de Liga MX ni el fondo de incentivo — es decir, exactamente el resultado que el benchmark identificó como el patrón de fracaso más común (Bélgica: consenso sin incentivo corregido).

**Corrección propuesta:** No basta con el indicador tardío de la sección 19.2 del Agente 15 (medido recién en el año 4, escalado en el año 9-12). Se recomienda fijar un punto de control más temprano (año 2) con una consecuencia predefinida si el indicador de "reformas replicadas de ligas menores a Liga MX" es 0 — no solo "elevarlo como hallazgo" sino activar de inmediato la vía de presión Concacaf/FIFA en vez de esperar a la revisión intermedia.

**Veredicto: modificar.** La estrategia de secuenciación por sí sola no es un mecanismo de cumplimiento — es una apuesta razonada, no una garantía; el documento debe dejar de presentarla, incluso implícitamente, como una solución al problema que el benchmark identificó, y presentarla explícitamente como mitigación de probabilidad, con un plan de contingencia más rápido que el actual (año 9-12).

---

### Crítica 6 — La capacidad administrativa real de la FMF para absorber todo lo que se le encarga en el año 1 nunca se verificó

**Problema:** El propio Agente 15 formula la pregunta correcta (PQ-I03: "¿Qué capacidad operativa administrativa tiene hoy la FMF para absorber la coordinación de ocho pilares simultáneos?") y la deja sin respuesta. Con los cinco pilares adicionales de la ronda 5b (que además recaen desproporcionadamente en la FMF: Carta de Funciones, regla de enfriamiento, Comité de Ética y Transparencia, registro de beneficiario final, licencia de directivo, criterios de certificación, Protocolo Nacional de Integridad, formalización del convenio SIPINNA), el "año 1" pasa de las 19 acciones ya diseñadas por el Agente 15 a más de 30 acciones institucionales simultáneas, casi todas con la misma área jurídica/Comité Ejecutivo de la FMF como responsable.

**Evidencia:** `fase7-agente15-implementacion.md`, sección "Preguntas nuevas para el registro maestro", PQ-I03: "¿Qué capacidad operativa administrativa tiene hoy la FMF... para absorber la coordinación de ocho pilares simultáneos sin que la Mesa Técnica de Seguimiento se convierta, en la práctica, en una estructura más grande de lo diseñado?" — sin fuente de respuesta identificada, marcada como pregunta abierta. La línea base (`05`, Bloque B) ya documentó que el poder en la FMF está personalizado (caso Arriola) y que casi ninguna cifra de capacidad instalada es auditable — es decir, tampoco hay evidencia de que la FMF tenga hoy el personal/presupuesto administrativo para ejecutar simultáneamente lo que 13 pilares le encargan.

**Gravedad:** Grave, agravada por la Crítica 3 (el volumen real del año 1 creció sin que nadie revisara la capacidad de ejecutarlo).

**Consecuencia si no se corrige:** Riesgo de que la Mesa Técnica de Seguimiento —diseñada deliberadamente pequeña (3-5 personas) para no convertirse en la institución nueva que el proyecto evita crear— termine absorbiendo por necesidad funciones ejecutivas que no le corresponden, o que varias de las 30+ acciones del año 1 simplemente no se ejecuten por falta de personal, sin que quede claro cuáles se sacrificaron y por qué.

**Corrección propuesta:** Responder PQ-I03 con una auditoría rápida (no una investigación completa) del organigrama y presupuesto administrativo actual de la FMF antes de aprobar el cronograma consolidado del año 1, y priorizar explícitamente (no dejar implícito) qué acciones se posponen si la capacidad real es menor a la asumida.

**Veredicto: modificar.** No se recomienda reducir el número de reformas — la mayoría son de bajo costo y alto valor — sino secuenciar dentro del año 1 (no todo en los primeros 100 días) y verificar la capacidad real antes de comprometer fechas públicas.

---

### Crítica 7 — El mecanismo de protección de menores es más lento y más estrecho de lo que el caso Riodoce exige, y la contingencia inmediata que el propio proyecto propuso no se convirtió en una acción real

**Problema:** El registro de riesgos (`04`) ya identificó, desde antes del diseño de los pilares, que el caso Riodoce (julio 2025, firmas irregulares a niños de 12 años) exigía una contingencia inmediata: "Activar la Procuraduría de Protección de NNA existente mientras se formaliza el convenio [FMF-SIPINNA]." Sin embargo, en el cronograma real (`fase7-agente15`, sección 17.1, acción 6), la primera acción de los primeros 100 días es solo "iniciar negociación (no firma)" del convenio, con firma proyectada para el año 1 (hasta 12 meses después). No hay ninguna acción explícita, en ningún pilar, que active la Procuraduría de forma independiente del convenio mientras este se negocia — la contingencia que el propio proyecto se recomendó a sí mismo se perdió entre la Fase 1 y la Fase 7.

**Evidencia:** `04-registro-supuestos-riesgos.md`, sección 5: "La protección de menores... depende casi enteramente de autorregulación privada de la FMF... con casos ya documentados (Riodoce, 2025) sin consecuencia pública conocida... Contingencia: Activar la Procuraduría de Protección de NNA existente mientras se formaliza el convenio." Comparar con `fase7-agente15-implementacion.md`, sección 17.1, acción 6, que solo programa el inicio de negociación, y `fase5b-pilar2-marco-juridico.md`, sección 19, que fija 3-6 meses para el convenio (el tramo más optimista, no el cronograma real de Agente 15 que lo fija en hasta 12 meses).

Además, el mecanismo diseñado (suspensión de certificación como consecuencia administrativa) solo tiene efecto sobre **academias certificadas** — la proporción de academias que realmente supervisa la FMF sigue sin respuesta (PQ-C06, citada como bloqueador explícito en `fase5b-pilar2`, sección 22). Si el caso Riodoce u otros similares ocurren en academias no certificadas o informales (lo cual no se descartó en ningún documento), el mecanismo central de este pilar no tiene ninguna palanca sobre ellas — solo queda el canal general de SIPINNA, que ya existía antes del proyecto.

**Gravedad:** Grave, por tratarse del riesgo de mayor sensibilidad social del proyecto según su propia clasificación ("máxima prioridad social, aunque no la de mayor impacto competitivo", `fase7-agente15`, sección 17.1, acción 6).

**Consecuencia si no se corrige:** Un caso mediático mayor durante los 6-12 meses de negociación del convenio —exactamente el escenario que el registro de riesgos advirtió como "activar antes de que escale a un caso mediático mayor durante el proyecto"— dejaría al proyecto sin ninguna acción concreta que mostrar más allá de "estamos negociando," y sin ninguna cobertura real sobre academias no certificadas en ningún escenario.

**Corrección propuesta:** Incorporar como acción explícita de los primeros 100 días (no como nota de riesgo) la activación pública del canal ya existente de la Procuraduría de Protección de NNA para el ámbito futbolístico, de forma independiente y previa a la firma del convenio FMF-SIPINNA; y responder PQ-C06 con carácter de urgencia dado que condiciona el alcance real de la única consecuencia sancionadora diseñada.

**Veredicto: modificar.** El diseño del convenio (Pilar 2, sección 15) es sólido y bien fundamentado jurídicamente; lo que falta es una acción-puente inmediata que el propio proyecto ya había identificado como necesaria y que se perdió en la traducción de la Fase 1 a la Fase 7.

---

### Crítica 8 — El incentivo positivo de la regla de menores puede ser cosmético: nunca se verificó si los clubes están realmente limitados por su cupo de extranjeros

**Problema:** El diseño central del Pilar 6 (y la pieza de mayor consenso del benchmark, según `08`) es dar a los clubes que superen el mínimo de formación un cupo adicional de extranjeros como "holgura." Ese incentivo solo tiene valor real para un club si su cupo actual de extranjeros es efectivamente una restricción vinculante — es decir, si el club ya está usando todos sus cupos y querría más. Ningún documento del proyecto verifica si los 18 clubes de Liga MX están, en la práctica, limitados por su cupo (9 registrados/7 en cancha) o si tienen margen sin usar. Si la mayoría de los clubes grandes no agotan su cupo actual, ofrecerles "un cupo adicional" no cambia ningún cálculo económico real.

**Evidencia:** `fase5-agente6-formacion-fuerzas-basicas.md`, sección 15.2, pregunta 14, ya advierte el riesgo de captura ("la Asamblea de Dueños podría diseñar el fondo para beneficiar a los clubes grandes que ya cumplen, sin mover la aguja"), pero ese riesgo se refiere a la fórmula de reparto, no a si el incentivo mismo tiene valor. `fase7-agente15-implementacion.md`, Piloto 2 (sección 18), sí diseña una prueba con criterio de cancelación explícito ("que el beneficio solo favorezca a clubes que ya cumplían con holgura, sin mover a los que cumplen al límite") — lo cual es una mitigación correcta del riesgo de *reparto*, pero el piloto no incluye, como paso previo, verificar si el cupo de extranjeros es una restricción vinculante para los clubes objetivo antes de diseñar el incentivo sobre esa base.

**Gravedad:** Moderada-grave. No invalida el mecanismo, pero expone que su premisa de diseño (que un cupo adicional de extranjeros tiene valor suficiente para cambiar el comportamiento de un club que hoy prefiere pagar la sanción) nunca se verificó empíricamente, pese a que la propia línea base (S-12) ya identificó como pregunta abierta si el incumplimiento es por cálculo económico o por escasez real de cantera.

**Consecuencia si no se corrige:** El Piloto 2 (un torneo completo, 6 meses) podría "fallar" no porque el principio del incentivo positivo esté mal, sino porque el vehículo elegido (cupos de extranjeros) no tenga valor real para los clubes que más importa mover — desperdiciando el ciclo de prueba sin aprender la lección correcta.

**Corrección propuesta:** Antes de ejecutar el Piloto 2, verificar con datos ya disponibles (o solicitables a la FMF/Liga MX) qué proporción de clubes de Liga MX utiliza actualmente su cupo completo de extranjeros de alto puntaje — si la mayoría tiene margen sin usar, rediseñar el incentivo de fase 1 hacia algo con valor real y verificable (p. ej., prioridad de horarios de transmisión, prioridad en trámites de licencia) antes de gastar el ciclo de piloto en un vehículo potencialmente vacío.

**Veredicto: modificar.** El principio (premiar, no solo sancionar) es correcto y está bien fundamentado en el benchmark (MLS); el vehículo específico de la fase 1 necesita una verificación previa que hoy no existe.

---

### Crítica 9 — Posible cuarta duplicidad de auditoría no reconciliada: el auditor financiero del Pilar 1 no se fusionó explícitamente con el vehículo tri-modular ya consolidado

**Problema:** `09` y `fase7-agente15` (Hallazgo 3) ya consolidaron tres auditores externos rotativos diseñados por separado (Agente 6 – academias, Agente 8 – entrenadores, Agente 10 – datos/scouting) en un solo vehículo de tres módulos. El Pilar 1 (sección 16.4, diseñado después de esa consolidación) propone "el mismo tipo de instrumento" —un auditor externo rotativo— para transparencia financiera agregada de FMF y ligas menores, sin indicar explícitamente si se trata de una extensión del mismo contrato tri-modular o de un cuarto contrato separado. Ningún documento de integración posterior (no existe una "Fase 6c") resolvió esta pregunta, porque el Pilar 1 se diseñó después de que se cerraran las integraciones de duplicidades (`09`, `10`).

**Evidencia:** `fase5b-pilar1-gobernanza.md`, sección 16.4: "el mismo tipo de instrumento que el Agente 6 ya diseñó y costeó para la certificación de academias... aplicado ahora a estados financieros en vez de a estándares técnico-deportivos" — la frase "el mismo tipo" sugiere una analogía de diseño, no necesariamente el mismo contrato. `fase7-agente15-implementacion.md`, Hallazgo 3 y sección 12, documenta la fusión de tres (no cuatro) mandatos técnicos.

**Gravedad:** Moderada. Bajo impacto financiero individual (el propio Pilar 1 estima "decenas de millones de pesos/año, no cientos"), pero es exactamente el tipo de duplicidad de coordinación que el proyecto se enorgullece de haber evitado en los otros cuatro casos ya reconciliados.

**Consecuencia si no se corrige:** Cuatro procesos de licitación y rotación de auditor en paralelo en vez de uno, con el riesgo adicional (ya señalado por el propio Agente 15 para el caso de tres auditores) de que un auditor sectorial de finanzas no tenga visibilidad de patrones de captura que sí vería un auditor único con mandato integral.

**Corrección propuesta:** El Agente 0 (o su función de integración sucesora en Fase 9) debe resolver explícitamente si el mandato de transparencia financiera del Pilar 1 se integra como un cuarto módulo del mismo vehículo de auditoría ya consolidado, o si se justifica mantenerlo separado (por ejemplo, por requerir perfil de auditor financiero distinto al técnico-deportivo) — pero la decisión debe quedar documentada, no implícita.

**Veredicto: modificar.** Recomendación: fusionar como cuarto módulo del mismo vehículo, salvo que exista una razón técnica documentada (perfil de auditor financiero vs. deportivo) para mantenerlo separado — y esa razón, si existe, debe hacerse explícita.

---

### Crítica 10 — El uso de COFECE como "última instancia" para forzar transparencia financiera es un uso más específico y dirigido que el precedente de 2021, y no se exploró a fondo el riesgo de que se lea como injerencia

**Problema:** El precedente que sostiene todo el criterio D-03 (COFECE 2021) fue una sanción por colusión salarial —una infracción de competencia económica clásica, de aplicación general— sin reacción de FIFA. La recomendación 15 del Pilar 14 propone usar la facultad de "estudio de mercado y requerimiento de información" de COFECE, específicamente dirigida al sector fútbol, como mecanismo de última instancia si Liga MX no publica voluntariamente su información financiera en 24 meses. Esto es un uso más targeted del aparato regulatorio estatal —no una sanción por una infracción ya cometida, sino una amenaza de activar una facultad pública específicamente como palanca de negociación sobre una práctica de transparencia que la Asamblea de Dueños no está obligada a adoptar—, y el proyecto no exploró si FIFA podría leer esta secuencia (aviso explícito + plazo + activación condicionada de un requerimiento estatal) de forma distinta a una sanción posterior por una infracción ya consumada.

**Evidencia:** `fase5b-pilar14-integridad.md`, sección 16, recomendación 15: "misma facultad, mismo estándar D-03, ya ejercida sin reacción de FIFA en 2021" — la equivalencia se afirma pero no se argumenta en detalle por qué una amenaza condicionada y dirigida específicamente al sector es jurídicamente idéntica a una sanción aplicada después del hecho por una conducta anticompetitiva ya verificada. `fase5b-pilar2-marco-juridico.md`, sección 15bis, pregunta 14, sí identifica el riesgo de "vagón legislativo" para la vía legislativa, pero ese análisis no se extendió al uso instrumental de COFECE como palanca de negociación.

**Gravedad:** Moderada. El riesgo no es que la actividad sea ilegal (probablemente no lo es, dado que COFECE ya tiene esa facultad de forma general), sino que el proyecto podría estar subestimando cómo FIFA interpreta la intención y el patrón de uso de una facultad pública, no solo su base legal formal.

**Consecuencia si no se corrige:** Si FIFA interpreta el uso instrumental y anunciado de COFECE como una forma de presión estatal coordinada sobre el gobierno del fútbol (aunque técnicamente sea una ley general), podría generar la misma reacción que el proyecto entero busca evitar, justo en el mecanismo diseñado para proteger la integridad del sistema.

**Corrección propuesta:** Antes de anunciar públicamente el plazo de 24 meses y la amenaza de activación de COFECE (recomendación 15), obtener una opinión jurídica específica sobre este uso instrumental —no solo reutilizar la validación general de D-03— y considerar si es preferible no anunciar el plazo/amenaza públicamente, dejando la facultad como respaldo silencioso en vez de palanca de negociación declarada.

**Veredicto: modificar.** No eliminar la opción de que COFECE ejerza su facultad si corresponde —eso es legítimo bajo D-03—, pero sí modificar la forma de presentarla: como posibilidad general y no como amenaza anunciada y cronometrada específicamente contra el fútbol.

---

### Crítica 11 — El calendario se calibra contra Corea del Sur, pero el propio proyecto admite que México parte en peor posición que Corea para el mecanismo central, sin ajustar el horizonte

**Problema:** El cronograma (`fase7-agente15`) usa el caso coreano (licencia de club condicionada, aplicada en 2020 sobre liga madura desde 1983) como la referencia de plazo más análoga al punto de partida mexicano, fijando "resultados juveniles medibles" hacia el año 9-12. Pero el propio documento reconoce, en su sección de adaptación (28), que "México, a diferencia de Corea 2020, tiene un actor de veto (Asamblea de Dueños) sin precedente de aceptar condiciones impuestas verticalmente... Corea no necesitó [un mecanismo de presión competitiva] porque su federación tenía más autoridad directa sobre la liga." Es decir: el proyecto usa el plazo de Corea sin ajustar por el hecho, que él mismo documenta, de que la gobernanza mexicana es estructuralmente más adversa para el mecanismo que sostiene ese plazo.

**Evidencia:** `fase7-agente15-implementacion.md`, sección 28 ("Adaptación a México"), párrafo sobre Corea del Sur. Comparar con sección 17.5, que fija "años 9-12" para "resultados juveniles medibles" citando explícitamente el "patrón de plazo del benchmark (Corea, Islandia)" sin nota de ajuste por gobernanza más débil.

**Gravedad:** Moderada. No es un error de cálculo sino una inconsistencia entre el propio análisis cualitativo del documento (México parte peor que Corea) y la cifra numérica que usa (el mismo plazo que Corea).

**Consecuencia si no se corrige:** Expectativas públicas ancladas a un plazo (año 9-12) que el propio análisis del proyecto sugiere que podría ser optimista, generando presión política prematura para mostrar resultados antes de que la estructura de gobernanza —más lenta que la coreana por diseño propio del proyecto— pueda producirlos.

**Corrección propuesta:** Ampliar la banda de confianza del hito "año 9-12" a un rango más amplio (p. ej., año 9-15) o presentar explícitamente dos escenarios de plazo —uno si el mecanismo de presión competitiva de la sección 19.2 funciona, otro más lento si no— en vez de un solo punto de calibración.

**Veredicto: modificar.** No cambiar la elección de Corea como referencia (sigue siendo el caso más análogo disponible), pero sí ajustar la comunicación del plazo para reflejar la propia advertencia de gobernanza que el documento ya hizo.

---

### Crítica 12 — Las piezas más redistributivas del diseño son, sistemáticamente, las que quedan sin financiamiento firme; las piezas que refuerzan ventajas existentes se autofinancian y arrancan primero

**Problema:** Al comparar qué recomendaciones tienen fuente de financiamiento resuelta contra cuáles quedan "condicionadas" (sección 10.4 de `fase7-agente14`), aparece un patrón: la certificación de academias (que beneficia primero a los clubes/academias que ya pueden pagar cuotas escalonadas), la auditoría técnica y la captación binacional (orientada a mercado estadounidense, no a talento rural doméstico) tienen fuente de financiamiento resuelta o autofinanciable y arrancan en el año 1. En cambio, el fondo de desarrollo femenil, la redistribución de derechos comerciales hacia la Liga MX Femenil, el fondo con dinero de la regla de menores y el fútbol adaptado —las cuatro piezas más orientadas a corregir desigualdad (de género, de recursos, de discapacidad)— son exactamente las cinco que el Agente 14 marca como "no costeadas en firme" por depender de la misma transparencia financiera que aún no existe.

**Evidencia:** `fase7-agente14-finanzas.md`, sección 10.4 (los cinco rubros no costeados: fondo con dinero, fondo femenil + redistribución TV femenil, fútbol adaptado, contenido comunitario en TV, solidaridad FIFA como fuente activa) — tres de los cinco son explícitamente de equidad (género, discapacidad). Comparar con Anexo A.2 (Academias, autofinanciable desde el año 1) y `fase5-agente11-selecciones.md`, sección 18 (Unidad de Captación Binacional, costo medio pero sin condicionar a transparencia financiera). Además, los tres estados ilustrativos del Piloto 1 (`fase7-agente15`, sección 18) son, en dos de tres casos, mercados de clubes grandes ya consolidados (Nuevo León/Tigres-Rayados, Hidalgo/Pachuca), con el tercero (rural/sureste) marcado como "confianza D — selección ilustrativa, pendiente de confirmación."

**Gravedad:** Moderada. No es una decisión deliberada de ningún agente —cada uno, individualmente, aplicó la misma disciplina correcta de "no costear sin fuente verificable"— pero el patrón agregado, no analizado por ningún documento del proyecto hasta ahora, es que esa disciplina cae desproporcionadamente sobre las piezas de equidad.

**Consecuencia si no se corrige:** El proyecto podría avanzar visiblemente en los primeros 4 años (certificación, auditoría, captación binacional) mientras las piezas de equidad de género y discapacidad permanecen indefinidamente en "presupuesto contingente" — reproduciendo, sin intención explícita, el patrón de desigualdad urbana/de clubes grandes que el proyecto se propuso evitar.

**Corrección propuesta:** El Agente 17 (integración final) debe presentar explícitamente este patrón agregado como parte del documento ejecutivo (no dejarlo disperso en cinco secciones distintas de tres documentos), y considerar si al menos una fuente de financiamiento no condicionada a la transparencia de Liga MX (p. ej., un porcentaje menor pero cierto de los fondos FIFA Forward, ya identificados como fuente de "realismo medio-alto") puede destinarse a un piloto mínimo del fondo femenil o del fútbol adaptado, para no dejar toda la agenda de equidad como rehén de un solo desbloqueador.

**Veredicto: modificar.** No es una falla de ningún pilar individual — es un efecto agregado no observado a nivel de proyecto que debe corregirse en la síntesis final, no en el rediseño de ningún pilar.

---

### Crítica 13 — El proyecto trata el apetito de Apollo por "buena gobernanza" como un aliado de la transparencia, sin someter a escrutinio lo que Apollo ya obtuvo

**Problema:** El Pilar 1 usa explícitamente el argumento de que el capital privado externo (Apollo, ~1,300 mdd) "ya condicionó su entrada a estándares de buen gobierno" como palanca para vender las reformas de transparencia a la Asamblea de Dueños —tratando el interés de Apollo como alineado con el desarrollo. Pero la propia línea base documenta que las condiciones que Apollo ya obtuvo (fin del ascenso/descenso, fin de multipropiedad) reducen, no aumentan, la disciplina competitiva del sistema, y el registro de riesgos (`04`) clasifica la "captura del sistema por capital privado sin representación en los órganos formales" como riesgo de probabilidad Media-Alta e impacto Alto. Ningún pilar diseña un mecanismo que verifique si las futuras condiciones de Apollo seguirán alineadas con desarrollo juvenil, o si en algún punto divergen (por ejemplo, presionando por mayor extracción comercial de corto plazo en vez de inversión en formación).

**Evidencia:** `fase5b-pilar1-gobernanza.md`, sección 16.3: "la evidencia ya documentada... muestra que capital institucional externo ya condicionó su entrada a estándares de 'buen gobierno' — [esto] alinea el interés de la propia Asamblea (atraer inversión) con la reforma." `04-registro-supuestos-riesgos.md`, sección 5: "Captura del sistema por capital privado sin representación en los órganos formales de gobierno del fútbol mexicano (fondo tipo Apollo)... condicionaría reglas de competencia sin pasar por la Asamblea General de la FMF ni el Sector Amateur" (Media-Alta/Alto). La mitigación registrada ahí ("documentar y hacer público el vínculo... recomendar mecanismos de transparencia obligatoria sobre condicionamientos de capital externo") no se convirtió en ninguna recomendación explícita de ningún pilar de diseño posterior.

**Gravedad:** Moderada. Es un riesgo ya identificado por el propio proyecto en la Fase 1 que se "perdió" en el diseño de Fase 5b — el Pilar 1 lo usa como argumento de venta sin retomar la mitigación que el registro de riesgos ya había propuesto para el mismo actor.

**Consecuencia si no se corrige:** El proyecto podría depender, para su pieza de gobernanza más difícil de conseguir (aprobación de la Asamblea), del alineamiento continuado de un actor cuyo interés de fondo (retorno de inversión) no es idéntico al del proyecto (desarrollo juvenil de largo plazo), sin ningún mecanismo de verificación de ese alineamiento a lo largo del tiempo.

**Corrección propuesta:** Incorporar, como parte del registro de beneficiario final ya diseñado (Pilar 1, 16.8) o como extensión del Comité de Ética y Transparencia, la obligación de hacer público cualquier condicionamiento de reglamento vinculado a la entrada de capital externo (la mitigación que el propio registro de riesgos de la Fase 1 ya proponía y que no se materializó en ningún pilar de diseño).

**Veredicto: modificar.** Usar el argumento de venta a la Asamblea (alineación con Apollo) no es incorrecto como táctica, pero debe acompañarse de la salvaguarda que el proyecto mismo ya se había prometido a sí mismo desde la Fase 1 y que se dejó de lado en el diseño.

---

### Crítica 14 — Proliferación de comités y mesas técnicas como respuesta por defecto: el proyecto declara 0% de "construir nuevo" pero en la práctica añade al menos seis cuerpos coordinadores

**Problema:** Cada pilar que enfrenta un vacío de gobernanza responde con una variante del mismo instrumento: Comité de Ética y Transparencia de la FMF (Pilar 1), reforma del Comité de Ética y Buen Gobierno de Liga MX (Pilar 1), Comité Técnico de Continuidad de Selecciones (Agente 11), Mesa Técnica de Seguimiento de Implementación (Agente 15), Mesa de Estándares de Cobertura dentro del Comité de Ética de la CIRT (Agente 12), extensión del Comité de Inversión y Certificación (Pilar 1/6). Cada uno, individualmente, pasa la prueba de las 14 preguntas y se justifica como extensión de un órgano existente, no como institución nueva — y eso es formalmente correcto. Pero el efecto agregado no se evaluó nunca como conjunto: son al menos seis cuerpos de coordinación nuevos o reformados operando en paralelo, cada uno con su propio calendario de reporte, su propia composición y su propio riesgo de vaciarse de contenido (ya señalado individualmente para el Comité Técnico de Continuidad y el Comité de Ética de la FMF).

**Evidencia:** Recuento propio a partir de `fase5-agente11-selecciones.md` sección 15, `fase7-agente15-implementacion.md` sección 15, `fase5-agente12-cultura-medios.md` sección 15.1, `fase5b-pilar1-gobernanza.md` secciones 16.3-16.4. Ningún documento de integración (`09`, `10`) evalúa la carga administrativa agregada de coordinar seis cuerpos distintos, cada uno con su propio ciclo de reporte (trimestral, anual), sobre la misma FMF cuya capacidad administrativa ya es objeto de la Crítica 6.

**Gravedad:** Leve-moderada. Cada instrumento individual está bien justificado; el riesgo es acumulativo, no de ningún componente aislado.

**Consecuencia si no se corrige:** Fragmentación de la gobernanza del propio proyecto de implementación —seis reportes distintos, sin un solo punto de consolidación real más allá de que la Mesa Técnica "reciba" los indicadores de los demás—, contradiciendo el espíritu (aunque no la letra) de la regla de "aprovechar antes de crear."

**Corrección propuesta:** El Agente 17 (integración final) debe mapear los seis cuerpos en un solo diagrama de gobernanza del propio proyecto, verificar que sus mandatos no se traslapen y, si es posible, consolidar el reporte de al menos dos de ellos (por ejemplo, la Mesa de Estándares de la CIRT y el boletín trimestral ya comparten insumos) en un solo ciclo de publicación.

**Veredicto: mantener con nota.** Ningún comité individual debe eliminarse —cada uno resolvió correctamente su propia prueba de las 14 preguntas— pero el proyecto debe reconocer y gestionar explícitamente la carga acumulada, hoy invisible porque cada pilar la evaluó de forma aislada.

---

### Crítica 15 — El rubro presupuestal más grande depende de actores (CONADE/SEP/municipios) cuyo poder de palanca sobre el fútbol la propia línea base calificó como estructuralmente bajo, sin reconciliar esa tensión

**Problema:** El supuesto S-08 (`04`) afirma que "el fútbol profesional mexicano depende poco de fondos públicos... por lo que el poder de condicionamiento de CONADE... es estructuralmente bajo" — un hallazgo usado, correctamente, para explicar por qué el gobierno no tiene mucha palanca sobre la Asamblea de Dueños. Pero el rubro de mayor magnitud absoluta de todo el presupuesto (infraestructura escolar, ejecutado vía CONADE/SEP/municipios, no vía el fútbol profesional) depende exactamente de esos mismos actores de "poder estructuralmente bajo" — solo que aquí el poder relevante no es sobre el fútbol profesional sino sobre la ejecución de obra pública municipal, donde la línea base y el propio Agente 14 ya documentaron un problema distinto y no resuelto: capacidad fiscal desigual entre municipios. Ningún documento reconcilia que el rubro más grande del proyecto depende de la capacidad de ejecución de actores públicos que el propio proyecto nunca evaluó con el mismo rigor que evaluó a la Asamblea de Dueños.

**Evidencia:** `04-registro-supuestos-riesgos.md`, S-08, y `fase7-agente14-finanzas.md`, sección 21, riesgo: "Los municipios con menor capacidad fiscal no pueden aportar la contraparte esperada para uso compartido/mantenimiento, generando implementación desigual por región" (Alta probabilidad, Medio-Alto impacto). A diferencia del mapa de poder detallado que el Agente 2 construyó para la Asamblea de Dueños (con nombres, casos, patrones de incumplimiento), no existe un mapa equivalente de capacidad real de ejecución de CONADE, SEP y los municipios prioritarios — el rubro más grande del presupuesto se apoya en el actor menos investigado del proyecto.

**Gravedad:** Leve-moderada. El riesgo está declarado, pero con menos profundidad de evidencia que el resto del proyecto, precisamente porque el mandato original de los Agentes 1-4 se concentró en el fútbol profesional (FMF/Liga MX/clubes), no en la capacidad de ejecución de infraestructura pública municipal.

**Consecuencia si no se corrige:** El rubro presupuestal más grande del proyecto podría ejecutarse de forma desigual entre estados/municipios sin que exista, hoy, ningún diagnóstico comparable en calidad al que el proyecto sí hizo para el sector futbolístico privado.

**Corrección propuesta:** Encargar, como parte de la recalibración presupuestal ya prevista para el año 2 (`fase7-agente14`, recomendación 6), un diagnóstico específico de capacidad fiscal/administrativa municipal para el rubro de infraestructura escolar, con el mismo nivel de detalle que el Agente 2 aplicó al mapa de poder del fútbol profesional.

**Veredicto: modificar.** No cambia el diseño del rubro (rehabilitar antes que construir sigue siendo correcto), pero exige el mismo estándar de diagnóstico de capacidad institucional que el proyecto aplicó rigurosamente al sector privado y no aplicó, con el mismo rigor, al sector público del que depende su partida más grande.

---

## 4. Hallazgo positivo, por transparencia metodológica

No todo lo revisado es crítica. Vale registrar, porque el Red Team debe ser honesto en ambos sentidos, que el proyecto **evita consistentemente** los lugares comunes prohibidos por la sección 4 del manual metodológico: no propone limitar más a los extranjeros como solución aislada (el Pilar 6 explícitamente se abstiene de tocar la cuota), no restaura el ascenso/descenso, no propone una gran academia nacional (rechaza explícitamente el modelo marroquí de "academia insignia" para la captación binacional), no copia un solo modelo extranjero (cita 20 países con clasificación de transferibilidad específica), y no trata "invertir más dinero" ni "construir más canchas" como la solución por defecto (89-95% de las recomendaciones de cada pilar están en las primeras seis categorías de la jerarquía de intervención). Este nivel de disciplina no es automático — es el resultado de que el propio manual metodológico (Fase 1) fijó la regla y los agentes de diseño la citaron y la respetaron activamente, no solo de palabra.

---

## 5. Veredicto general — ¿pasa el proyecto el Control 7?

**No, tal como está hoy.** El manual metodológico define el Control 7 como superado cuando "todas las críticas [están] respondidas (mantener, modificar o eliminar cada recomendación)" — esta es precisamente la función que cumple este documento, y su resultado es que **ninguna crítica exige eliminar** una recomendación completa (el diseño de fondo es sólido, disciplinado en el uso de evidencia y consistente con su propio manual), pero **doce de las quince críticas exigen modificación concreta antes de avanzar a la Fase 9/10**, y al menos tres de ellas (críticas 1, 2 y 3) son de gravedad suficiente para considerarse bloqueadoras del control, no simples mejoras:

- La Crítica 3 (presupuesto y cronograma desactualizados frente a los cinco pilares más recientes) es, en sentido estricto, un incumplimiento del propio Control 6 tal como el manual lo define ("inversión, operación, fuente permanente, sensibilidad" para *todo* el proyecto, no para ocho de trece pilares) y debe resolverse con un adendum de Agente 14/15 antes de que el Agente 17 integre el documento final.
- Las Críticas 1 y 2 (la premisa de gobernanza no verificada y el mecanismo de transparencia financiera sin dientes reales para Liga MX) tocan directamente la advertencia que el propio proyecto se hizo a sí mismo como la más importante de todo el benchmark (`08`, sección 4) — el Red Team no puede dar por buena la respuesta del proyecto a su propia advertencia central mientras ambas sigan abiertas.

**Recomendación de proceso:** proceder a la Fase 9 (Corrección del borrador) como ya estaba previsto en el calendario original del Agente 0, con instrucción explícita de que el adendum de reconciliación presupuesto/cronograma (Crítica 3) y la verificación de PQ-I05 (Crítica 1) son condición previa —no tareas paralelas— antes de que el Agente 17 inicie la integración final de la Fase 10. Las doce críticas restantes pueden incorporarse como correcciones dentro del propio proceso de integración final, sin requerir una ronda adicional de diseño.
