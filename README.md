# hattrick-management

Control y documentación de **Satoshian FC** (Hattrick.org, TeamID 3524617, serie VI.78 USA), gestionado por Joan con apoyo de Claude.

## Cómo está organizado

| Ruta | Qué contiene |
|---|---|
| `snapshots/` | Levantamientos completos del club con fecha (finanzas, estadio, serie, staff, plantilla). Uno nuevo cada vez que cambie algo importante; no se editan los anteriores. |
| `docs/estrategia.md` | Estrategia deportiva y de entrenamiento vigente, con su justificación. |
| `docs/plantilla.md` | Plantilla completa, prioridad de entrenamiento y alineaciones propuestas. |
| `docs/presupuesto.md` | Presupuesto semanal recurrente y palancas financieras. |
| `docs/competencia.md` | Rivales de la serie: calificaciones por línea, reglas de ascenso y lectura. |
| `docs/referencia/` | **Base de conocimiento del juego**, por área, con fuente y nivel de confianza por dato. Empezar por `00-indice-y-fuentes.md`. Incluye `data/contribuciones.csv` y `tools/aporte.py`. |
| `docs/estrategia-inversion.md` | En qué invertir la caja disponible y por qué. |
| `docs/base-de-precios.md` + `data/` | Base de precios de transferencias: ventas cerradas (`data/ventas.csv`) y subastas seguidas (`data/subastas-seguidas.csv`). |
| `docs/historico/` | Documentos de trabajo del 25–26 nov; ya no son referencia. |
| `docs/cantera-plantilla.md` | Plantilla de la cantera. |
| `docs/operacion.md` | Reglas de operación: aprobaciones, acceso, límites y riesgos. |
| `log/decisiones.md` | Bitácora cronológica de decisiones y cambios ejecutados en el juego. |
| `pendientes.md` | Lo que falta verificar o decidir. |

## Estado actual (26-nov-2026, ~08:10 HT)

- Temporada 96, semana 3 de 16. Posición: 2.º en VI.78 (suben 1.º y 2.º).
- Caja: 273 600 US$ (antes de pagar las subastas en curso). Gasto recurrente ≈ 40 800 US$/sem; margen sin taquilla entre −3 800 y +2 700.
- Plantilla: 21 jugadores. Aprendices actuales: Yangki (PM7), Bajer, Algeier, Vohidov (PM6), Cabrera (extremo 7).
- Entrenamiento: Playmaking 100% / stamina 10%, eficiencia 68%. Se juega 3-5-2 en liga y amistoso para llenar los 6 cupos.
- Experiencia de formación: 3-5-2 excellent (8) tras "Learn a formation"; 4-4-2 solid (7).
- **Compras activas** (aprobadas por Joan): 10 subastas con puja nuestra; ver tabla en `pendientes.md`.
- Estrategia de inversión: aprendices con valor de reventa + un premium (tope 90 000). Ver `docs/estrategia-inversion.md`.
- Base de precios iniciada: 77 ventas cerradas en `data/ventas.csv`.
- Cantera: Satoshian Academy (YouthTeamID 3296580) activa desde el 25-nov, 1 scout, Playmaking + Passing.
- Próximos partidos: liga 29-nov vs Alabama Bears; amistoso 2-dic vs Paulvan.
- Levantamientos: [`base`](snapshots/2026-11-25-base.md) · [`actualización tarde`](snapshots/2026-11-25-actualizacion-tarde.md)

## Convenciones

- Etiquetas de fiabilidad: **[juego]** leído en pantalla · **[pack]** hattrick-context-pack (no oficial) · **[inferencia]** cálculo o juicio · **[sin verificar]**.
- Montos en US$ del juego. Horas en hora del servidor Hattrick (HT).
- Este repo no guarda contraseñas, cookies ni tokens.
