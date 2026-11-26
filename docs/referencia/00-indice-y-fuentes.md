# Referencia del juego — índice y fuentes

Esta carpeta es la **base de conocimiento** de Satoshian FC. Toda decisión de estrategia se justifica con un dato de aquí. Investigación hecha el 26-nov-2026.

| Archivo | Área |
|---|---|
| [01-entrenamiento.md](01-entrenamiento.md) | Quién entrena, cuánto, velocidad, resistencia |
| [02-jugadores.md](02-jugadores.md) | Habilidades, forma, experiencia, lealtad, especialidades, sueldos, lesiones |
| [03-partido-y-tacticas.md](03-partido-y-tacticas.md) | Motor de partido, tácticas, formación, ánimo y confianza |
| [04-contribucion-por-puesto.md](04-contribucion-por-puesto.md) | Qué aporta cada habilidad en cada puesto y orden |
| [05-economia-estadio-aficion.md](05-economia-estadio-aficion.md) | Ingresos, gastos, estadio, afición, patrocinadores, premios |
| [06-staff-y-entrenador.md](06-staff-y-entrenador.md) | Asistentes, médico, psicólogo, entrenador |
| [07-transferencias.md](07-transferencias.md) | Pujas, comisiones, reglas de venta |
| [08-cantera.md](08-cantera.md) | Academia juvenil |
| [09-liga-copa-amistosos.md](09-liga-copa-amistosos.md) | Ascensos, premios, copa, amistosos |

## Niveles de confianza

Cada dato lleva una etiqueta. **Si dos fuentes chocan, gana la de más arriba.**

| Etiqueta | Fuente | Confianza |
|---|---|---|
| **[juego]** | Leído en pantalla en nuestro club | Máxima: es lo que el juego hace hoy |
| **[oficial]** | Reglamento de Hattrick (hattrick.org/Help/Rules), leído el 26-nov-2026 | Alta. Da reglas y algunos números; a menudo no da fórmulas |
| **[wiki]** | Wiki de Hattrick (mantenida por usuarios) | Media. La página de contribuciones es de dic-2019 |
| **[comunidad]** | hattrick-context-pack (cita el "Unwritten Manual" y publicaciones de empleados de Hattrick en foros) y foros | Media-baja. Números útiles, sin verificación propia |
| **[inferencia]** | Cálculo o deducción nuestra | A confirmar en el juego |

## Fuentes consultadas
- Reglamento oficial completo: https://en-us.hattrick.org/Help/Rules/Complete.aspx y capítulos Training, Transfers, LineupBasics, LineupExpConf, Psychology, SeriesSystem, MatchBasics.
- Wiki "Skill contribution": https://wiki.hattrick.org/wiki/Skill_contribution (PDF aportado por Joan).
- hattrick-context-pack: https://github.com/rmagasi/hattrick-context-pack (archivos de referencia de entrenamiento, economía, tácticas y motor).
- Lecturas en el juego registradas en `log/decisiones.md` y `snapshots/`.

## Límites de esta investigación
- **Verificado directamente en el juego el 26-nov (segunda pasada):** regla de ascenso de VI.78, tabla de premios y bonos de ascenso, Apéndice 4 (comisión del agente y del club anterior), tabla de precios de entrenador con sus etiquetas, escala de niveles, editorial del 10-nov-2026, ánimo, confianza, afición y datos del entrenador.
- **Siguen siendo solo [comunidad]:** semanas por nivel de entrenamiento, eficiencia relativa del entrenador por nivel, coeficientes de local y de actitud, porcentajes exactos de la penalización por varios jugadores en el centro, fórmulas de ocasiones.
- **[wiki] sin segunda fuente:** la tabla de contribución por puesto (dic-2019).
- No hay forma de confirmar los números de [comunidad] sin datos propios: se irán validando con "Predict ratings" y con las actualizaciones semanales.
