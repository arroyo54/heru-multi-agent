# Matriz de agentes

18 agentes (0–17, con el Agente 5 dividido en cinco sub-agentes regionales). Cada fila resume su fase, insumos, entregables y de qué depende — el detalle de responsabilidades por agente está en el prompt maestro (Parte XX); esta matriz es la referencia operativa para la coordinación entre fases.

| Agente | Nombre | Fase | Insumos que recibe | Entregable principal | Depende de |
|---|---|---|---|---|---|
| 0 | Director de investigación | 1, 3, 6, 11 | Prompt maestro | Metodología, taxonomía, integración, control de calidad | — |
| 1 | Capacidades existentes | 2 | Manual metodológico, plantilla | Inventario nacional de instituciones, infraestructura, programas, capital humano, sistemas | Fase 1 |
| 2 | Gobernanza y poder | 2 | Manual metodológico, plantilla | Mapa de poder (FMF, Liga, dueños, clubes, TV, gobierno, FIFA, Concacaf, agentes, medios) | Fase 1 |
| 3 | Derecho y regulación | 2 | Manual metodológico, plantilla | Diagnóstico jurídico (leyes, reglamentos, menores, agentes, transferencias, datos, injerencia) | Fase 1 |
| 4 | Economía del fútbol | 2 | Manual metodológico, plantilla | Diagnóstico económico (ingresos, costos, incentivos, transferencias, exportación) | Fase 1 |
| 5A | Benchmark — Europa Occidental | 4 | Línea base consolidada (Fase 3) | España, Portugal, Francia, Alemania, Países Bajos, Bélgica | Fase 3 |
| 5B | Benchmark — Países pequeños/comunitarios | 4 | Línea base consolidada | Noruega, Islandia, Dinamarca, Suecia, Croacia, Uruguay | Fase 3 |
| 5C | Benchmark — África y diáspora | 4 | Línea base consolidada | Marruecos, Senegal, Ghana, Costa de Marfil | Fase 3 |
| 5D | Benchmark — América | 4 | Línea base consolidada | Estados Unidos, Canadá, Argentina, Brasil, Colombia | Fase 3 |
| 5E | Benchmark — Asia y Oceanía | 4 | Línea base consolidada | Japón, Corea del Sur, Australia | Fase 3 |
| 6 | Formación y fuerzas básicas | 5 | Línea base + benchmark + restricciones | Pilotos 3 y 5 — pirámide 5–23 años, estándares de academias | Fases 3–4 |
| 7 | Escuela, universidad y comunidad | 5 | Línea base + benchmark + restricciones | Pilar 4 — modelo híbrido escuela/universidad/club, sin copiar la NCAA | Fases 3–4 |
| 8 | Entrenadores y ciencia | 5 | Línea base + benchmark + restricciones | Pilar 8 — licencias progresivas, metas por cada mil jugadores | Fases 3–4 |
| 9 | Infraestructura | 5 | Línea base + benchmark + restricciones | Pilar 10 — mantenimiento antes que construcción nueva | Fases 3–4 |
| 10 | Datos y scouting | 5 | Línea base + benchmark + restricciones | Pilar 9 — arquitectura interoperable, identificador único | Fases 3–4 |
| 11 | Selecciones | 5 | Línea base + benchmark + restricciones | Pilar 13 — integración de categorías juveniles y mayor | Fases 3–4 |
| 12 | Cultura y medios | 5 | Línea base + benchmark + restricciones | Pilar 12 — narrativa e identidad, sin propaganda | Fases 3–4 |
| 13 | Fútbol femenil e inclusión | 5 | Línea base + benchmark + restricciones | Pilar 11 — auditoría transversal a todos los demás pilares | Fases 3–4 |
| 14 | Finanzas | 7 | Diseño integrado de los 14 pilares (post Fase 6) | Presupuesto por escenario (conservador/intermedio/transformador), costos unitarios, sensibilidad | Fase 6 |
| 15 | Implementación | 7 | Diseño integrado de los 14 pilares (post Fase 6) | Cronograma 20 años, dependencias, gobernanza del cambio, pilotos | Fase 6 |
| 16 | Red team | 8 | Borrador reconciliado (Fase 7) | Registro de críticas: problema, evidencia, gravedad, consecuencia, corrección, veredicto | Fase 7 |
| 17 | Integrador final | 10 | Borrador corregido (Fase 9) | Documento ejecutivo, técnico, presupuesto, hoja de ruta, RACI, dashboard, riesgos, propuesta regulatoria, anexos | Fase 9 |

## Notas de coordinación

- Los agentes 1–4 (Fase 2) corren **simultáneamente**, pero ninguno depende de los otros tres — sus hallazgos se concilian en la Fase 3, no durante la Fase 2.
- Los agentes 5A–5E (Fase 4) pueden empezar tan pronto la línea base esté consolidada (Fase 3), y su ventana se solapa con el cierre de esa fase (ver calendario en `00-agente0-metodologia-y-plan.md`, sección 7).
- Los agentes 6–13 (Fase 5) son los únicos que diseñan soluciones sustantivas por pilar; **todos** deben pasar el filtro de la sección 2.1 (14 preguntas de justificación) antes de proponer algo nuevo.
- El Agente 13 (fútbol femenil e inclusión) tiene un rol doble: diseña su propio pilar **y** audita transversalmente que los agentes 6–12 no traten al fútbol femenil como sistema aparte.
- Los agentes 14 y 15 no diseñan: cuestan y calendarizan lo que los agentes 6–13 ya diseñaron. Si el diseño no incluye costo/tiempo/responsable/indicador (Control 4), no puede pasar a esta fase.
- El Agente 16 (Red Team) es el único que puede recomendar eliminar una propuesta completa; su veredicto (mantener/modificar/eliminar) es vinculante para la Fase 9.
