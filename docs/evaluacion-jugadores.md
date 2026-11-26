# Cómo evaluar jugadores y alineaciones

## Herramientas del propio juego (fuente principal)
1. **"Recommended Positions"** en la ficha de cada jugador: muestra una calificación en estrellas por puesto. Sirve para decidir dónde rinde más cada uno.
2. **"Predict ratings"** en la pantalla de órdenes de partido (versión simple: `/Club/Matches/MatchOrder/Simple.aspx?MatchID=…`): predice las calificaciones de línea de la alineación cargada antes de enviarla. Es la forma más fiable de comparar dos alineaciones.
3. **Calificaciones del partido** ("Rating details" en el reporte): mediocampo, tres defensas, tres ataques. Se registran en `log/decisiones.md` para medir el efecto real de cada alineación.

Regla de trabajo: antes de cada partido, Claude carga la alineación, lee "Predict ratings" y la compara con la alternativa; después del partido compara predicción y resultado.

## Qué aporta cada puesto (tabla relativa) [pack, Unwritten Manual #15; no oficial]
Porcentaje de la habilidad del jugador que cuenta para cada línea, relativo al puesto que más aporta.

| Puesto | Mediocampo (PM) | Defensa central | Defensa lateral | Ataque central | Ataque lateral |
|---|---|---|---|---|---|
| Portero | — | 87% portería + 35% defensa | 61% portería + 25% defensa | — | — |
| Central | 25% | 100% defensa | 52% defensa | — | — |
| Lateral (normal) | 15% | 38% defensa | 92% defensa | — | 59% extremo |
| Interior (normal) | 100% | 40% defensa | 19% defensa | 22% scoring + 33% pases | 26% pases |
| Extremo (normal) | 45% | 20% defensa | 35% defensa | 11% pases | 86% extremo + 26% pases |
| Delantero (normal) | 25% | — | — | 100% scoring + 33% pases | 24% extremo + 14% pases + 27% scoring |

Penalización por aglomeración en el centro [pack]: 2 centrales −3,6% cada uno, 3 centrales −10%; 2 interiores −6,5%, 3 interiores −17,5%; 2 delanteros −5,5%, 3 delanteros −13,5%.

Lecturas útiles:
- El **mediocampo** lo hacen casi solo los interiores; un extremo aporta 45% de su playmaking y un central 25%.
- Con 3 interiores cada uno rinde 17,5% menos: el tercer interior suma entrenamiento, pero poca calificación.
- La **defensa** de un interior cuenta 40% para la defensa central: por eso un interior con defensa alta vale mucho más.
- Los valores son relativos; para calificaciones exactas se usa la predicción del juego.

## Fórmulas de partido [pack, datos de la comunidad]
- Reparto de ocasiones: `P = M_a³ / (M_a³ + M_b³)` con las calificaciones de mediocampo.
- Conversión de una ocasión: `P = 0,92 · a^3,5 / (a^3,5 + d^3,5)`, restando 0,75 a las calificaciones mostradas de ataque `a` y defensa `d`.

## Qué da valor de mercado a un aprendiz de playmaking [juego, mercado del 26-nov-2026]
Comparando subastas de 17 y 18 años:

| Perfil | Precio con pujas reales |
|---|---|
| 17 años, PM 6, sin especialidad ni secundarias | 0 – 3 000 |
| 17 años, PM 7, defensa 5–6, con o sin especialidad | 2 500 – 12 600 (con pocas pujas) |
| 17 años, PM 7, defensa 6, especialidad, 3–7 días de edad | 50 000 – 115 000 y más (50–200 pujas) |
| 18 años, PM 10, sin especialidad, una sola habilidad | ~15 000 (subasta en curso) |
| 18 años, PM 9–10, con especialidad | 150 000 – 245 000 |
| 18 años, PM 10, defensa 7, especialidad | 677 000 – 873 000 |

- La **especialidad** y la **defensa secundaria** multiplican el precio mucho más que un nivel extra de playmaking.
- Advertencia: algunos precios de la extracción salieron contaminados con dígitos del nombre del club pujador; solo se listan aquí los inequívocos.

## Herramientas externas
- Hattrick Organizer (HO) y similares son aplicaciones CHPP: requieren que Joan autorice su cuenta en Hattrick. Claude no ingresa credenciales. No son necesarias por ahora: el juego ya trae predicción de calificaciones y posiciones recomendadas.
