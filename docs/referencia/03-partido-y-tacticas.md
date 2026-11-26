# 03 · Partido y tácticas

## Cómo se decide un partido [oficial]
- **El mediocampo decide cuántas ocasiones tiene cada equipo.** Las demás líneas (ataque y defensa por centro y bandas) deciden si la ocasión termina en gol.
- Hay ataques abiertos (los gana el mediocampo más fuerte) y ataques exclusivos de cada equipo.
- Los eventos especiales ocurren con una probabilidad igual a la posesión.
- El equipo local suele tener más posesión. En un derbi (misma región), el visitante recibe la mitad de esa ventaja.

## Factores que multiplican el mediocampo [comunidad]
| Factor | Efecto |
|---|---|
| Local | ×1,199 |
| Derbi como visitante | ×1,115 |
| "Play it cool" | ×0,839 |
| "Match of the season" | ×1,115 |
| Contraataque | ×0,93 (oficial: "pierdes 7% de mediocampo") |

## Actitud del equipo [oficial]
- **Match of the season:** rinden más; el ánimo cae después.
- **Play it cool:** rinden menos; el ánimo sube después y rinden mejor en los siguientes.
- Solo en partidos oficiales. Los amistosos no cambian ánimo, confianza ni afición.

## Ánimo y confianza [oficial]
- El **ánimo** afecta al mediocampo. Lo mueven: liderazgo del entrenador, actitud elegida, **transferencias** y psicólogo. Tiende a normalizarse cada día.
- **Comprar o vender jugadores puede bajar el ánimo**; más riesgo al vender a uno "agradable" o comprar a uno "desagradable". Vender un juvenil en sus primeros 6 días en el primer equipo no tiene riesgo.
- La **confianza** afecta a las calificaciones de ataque. Depende de resultados y goles.
- **Subestimación:** con confianza alta y rival peor clasificado, el equipo puede relajarse (solo en liga, no en las tres primeras jornadas). "Play it cool" aumenta el riesgo [comunidad: lo triplica].
- Con dos goles de ventaja el equipo se relaja: cada gol extra resta 9% al ataque y suma 7,5% a la defensa.

## Experiencia de formación [oficial + juego]
- Se gana por minutos jugados con la formación (máx. 90 por partido; amistosos cuentan igual).
- **Con "excellent" o más no hay riesgo de confusión.** Por debajo, el riesgo crece.
- **Si no se usa, baja.** También puede bajar un poco al vender un jugador.
- Nuestro estado: 3-5-2 excellent (8), 4-4-2 solid (7) [juego, 26-nov].
- Detalle no oficial: cada partido completo sube la formación usada y todas pierden un poco [comunidad].

## Varios jugadores en el centro [oficial + comunidad]
- Oficial: con 2 o 3 centrales, interiores o delanteros, todos pierden aporte; los interiores pierden el doble que los defensas y los delanteros quedan en medio.
- Números [comunidad]: 2 centrales −3,6% c/u, 3 centrales −10%; 2 interiores −6,5%, 3 interiores −17,5%; 2 delanteros −5,5%, 3 delanteros −13,5%.

## Tácticas [oficial]
| Táctica | Efecto | De qué depende |
|---|---|---|
| Pressing | Menos ocasiones para ambos; gasta resistencia | Defensa + resistencia totales; Powerful cuenta doble |
| Contraataque | −7% de mediocampo; ataques extra solo si vas perdiendo el mediocampo y el rival falla | Pases (doble) y defensa de los defensas |
| Atacar por el centro | 15–30% de ataques laterales pasan al centro; peor defensa lateral | Pases de los jugadores de campo |
| Atacar por las bandas | 20–40% de ataques centrales pasan a las bandas; peor defensa central | Pases de los jugadores de campo |
| Jugar creativo | Más eventos especiales; peor defensa | Pases y experiencia; Unpredictable cuenta doble |
| Tiros lejanos | Hasta ~30% de ataques se vuelven tiros; bajan un poco las demás líneas | Anotación (×3) y balón parado |

## Alineación y órdenes [oficial]
- Órdenes hasta **20 minutos antes** del partido. Mínimo 9 titulares; con menos, el club alinea por nosotros con penalización.
- Hasta 5 órdenes por partido, máximo 3 sustituciones.
- Guardar una "alineación estándar" evita quedarse sin alineación.
- Marcaje individual: una orden por partido; el marcador pierde 50–65% de su aporte (10% si el objetivo no aparece).

## Balón parado [oficial]
- Un tercio son indirectos (cuentan anotación y balón parado medios del equipo). En córners pesan los especialistas Head.

## Clima [oficial]
Technical +5% con sol y −5% con lluvia; Powerful al revés; Quick −5% con ambos. El pronóstico del día siguiente es exacto [comunidad].

## Fórmulas aproximadas [comunidad]
- Reparto de ocasiones abiertas: `P = M_a³ / (M_a³ + M_b³)` con las calificaciones de mediocampo.
- Conversión de una ocasión: `P = 0,92 · a^3,5 / (a^3,5 + d^3,5)`, restando 0,75 a las calificaciones mostradas de ataque `a` y defensa `d`.
- Para la calificación real de una alineación se usa siempre "Predict ratings" en la pantalla de órdenes [juego].

## Por verificar con datos propios
- Coeficientes de local y de actitud, comparando "Predict ratings" con y sin cada opción.
- Cuánto baja 4-4-2 por semana sin usarse.
