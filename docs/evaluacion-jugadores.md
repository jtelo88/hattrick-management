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

## Qué da valor de mercado a un aprendiz de playmaking [juego, Transfer Compare, ventas cerradas 4–25 nov 2026]

| Perfil | n | Percentil 25 | Mediana | Percentil 75 |
|---|---|---|---|---|
| 17 años, PM7 + defensa 6 | 17 | 20 500 | 96 900 | 325 000 |
| 18 años, PM9 sola | 10 | 36 750 | 94 625 | 211 750 |
| 18 años, PM9 + defensa 6 | 10 | 38 250 | 125 500 | 180 500 |
| 18 años, PM9 + pases 5 | 10 | 83 750 | 120 500 | 238 000 |
| 18 años, PM9 + defensa 7 | 10 | 191 250 | 232 000 | 301 044 |
| 18 años, PM10 sola | 10 | 107 355 | 162 210 | 254 625 |
| 18 años, PM10 + pases 6 | 10 | 394 095 | 494 800 | 527 825 |

- Factores que mueven el precio dentro de un mismo perfil: **TSI** (subnivel oculto), **días de edad**, especialidad, forma. Con las mismas habilidades visibles el precio varió hasta 300×.
- Hipótesis sin verificar: nacionalidad (demanda de selecciones Sub-21) explica los casos de más de 1 000 000.
- El precio a horas del cierre no es el precio final; por eso se registran ambos en `data/subastas-seguidas.csv`.
- Esta tabla sustituye a la del 26-nov temprano, que mezclaba subastas en curso con ventas reales.
- Datos y método: `data/ventas.csv`, `docs/base-de-precios.md`.

## Herramientas externas
- Hattrick Organizer (HO) y similares son aplicaciones CHPP: requieren que Joan autorice su cuenta en Hattrick. Claude no ingresa credenciales. No son necesarias por ahora: el juego ya trae predicción de calificaciones y posiciones recomendadas.
