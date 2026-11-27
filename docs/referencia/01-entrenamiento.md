# 01 · Entrenamiento

## Reglas básicas [oficial]
- El entrenamiento se aplica una vez por semana (jueves o viernes según el país). **En EE. UU.: viernes 03:30 HT [juego].**
- Cuenta lo que el jugador jugó **para nuestro equipo** esa semana, en liga, copa o amistoso por igual.
- Máximo **90 minutos** de entrenamiento por semana. Con 50 minutos recibe 50/90.
- Si jugó en varios puestos, se toman los 90 minutos que más entrenan.
- Con menos de 1 minuto jugado no entrena.
- **Las órdenes individuales (defensivo, ofensivo, hacia el centro o la banda) no afectan al entrenamiento.** Solo cuenta el puesto.
- Un cambio de intensidad debe hacerse al menos una actualización diaria antes de la actualización de entrenamiento.

## Quién entrena con cada tipo [oficial]

| Tipo | Habilidad | Efecto completo | Efecto pequeño | Efecto muy pequeño |
|---|---|---|---|---|
| **Playmaking** | Jugadas | **Interiores** | **Extremos (la mitad)** | Todos los que jugaron |
| Defending | Defensa | Defensas | — | Todos |
| Scoring | Anotación | Delanteros | — | Todos |
| Crossing (Winger) | Extremo | Extremos | Laterales (la mitad) | Todos |
| Short passes | Pases | Interiores, extremos, delanteros | — | Todos |
| Through passes | Pases | Defensas, interiores, extremos | — | Todos |
| Wing attacks | Extremo | Delanteros y extremos | — | Todos |
| Defensive positions | Defensa | — | Portero, defensas, interiores, extremos | Todos |
| Shooting | Anotación (+ balón parado) | — | Todos | — |
| Goalkeeping | Portería | Portero | — | — |
| Set pieces | Balón parado | Todos (+25% para el lanzador y el portero) | — | — |

Consecuencias para nosotros:
- 3 interiores × 2 partidos = **6 cupos completos**; 2 extremos × 2 partidos = **4 cupos a la mitad**.
- Cualquier jugador que pise el campo recibe un efecto muy pequeño de jugadas, aunque juegue de central o delantero.
- "Short passes" entrena a interiores, extremos **y delanteros** a efecto completo (8 cupos por partido): opción a considerar más adelante para subir pases, la segunda secundaria más valiosa de un interior.

## Qué acelera o frena [oficial, sin números]
- **Edad:** los jóvenes aprenden más rápido.
- **Nivel actual:** en niveles muy bajos se entrena "muchas veces más rápido" que en niveles medios; en niveles muy altos, mucho más lento.
- **Intensidad (0–100):** más intensidad = más velocidad y mejor forma, pero más riesgo de lesión.
- **Entrenador y asistentes:** mejor entrenador y más niveles de asistentes = más efecto.
- **Porcentaje de resistencia:** lo que va a resistencia no va a la habilidad.

## Fórmula de velocidad (verificada 27-nov-2026)

**Fórmula de Schum** [comunidad, validada con oficial y juego]: subida semanal en fracción de nivel =

`f(nivel) × K(entrenador) × K(asistentes) × intensidad × (1 − resistencia) × K(tipo) × K(edad) × K(puesto) / 100`

| Factor | Valor |
|---|---|
| f(nivel) | 16.289 × e^(−0.1396 × nivel) si nivel < 9; 54.676 / nivel − 1.438 si nivel ≥ 9 |
| K(entrenador) | nivel 1: 0.7343 · 2: 0.8324 · 3: 0.92 · 4: 1.00 · 5: 1.0375 |
| K(asistentes) | 1 + 0.035 × suma de niveles (máx. 10) |
| K(tipo) | Jugadas 3.36 · Defensa 2.88 · Anotación 3.24 · Extremo 4.80 · Pases 3.60 · Portería 5.10 · Balón parado 14.70 |
| K(edad) | 54 / (edad + 37) → 17 años: 1.00 · 18: 0.982 · 19: 0.964 |
| K(puesto) | completo 1.0 · medio 0.5 · resto del campo 1/8 en Jugadas y Extremo, 1/6 en los demás |

Fuentes y validación:
- Código de Hattrick Organizer (`core/training/WeeklyTrainingType.java`, commit 8abe284 del 19-nov-2026), que usa las fórmulas de Schum y HT-Tasos.
- **Manual oficial** (Staff > Assistant Coach): jugador de 22 años, jugadas nivel 9, entrenador nivel 4, 100% intensidad, 10% resistencia → 8 / 7 / 6 semanas con 0 / 5 / 10 niveles de asistentes. La fórmula da 7.8 / 6.6 / 5.8. Coincide.
- **Juego** (Training > Training estimation, 27-nov, semana 3): Heinloth (PM7, sin entrenar con nosotros) sube en la semana 8 a puesto completo y en la 12 a medio puesto; Bajer y Algeier (PM6, una semana entrenada) en la semana 6. La fórmula da 4.8 y 9.7 semanas para PM7 y 4.2 para PM6. Coincide.

### Tabla para nuestro equipo (entrenador 3, asistentes 6, intensidad 100%, resistencia 10%, 17 años)

| Jugadas | Puesto completo | Medio puesto | Con entrenador nivel 4 (completo) |
|---|---|---|---|
| 6 → 7 | 4.2 semanas | 8.4 | 3.9 |
| 7 → 8 | 4.8 semanas | 9.7 | 4.5 |
| 8 → 9 | 5.6 semanas | 11.1 | 5.1 |
| 9 → 10 | 6.4 semanas | 12.8 | 5.9 |

Consecuencias:
- **Reglas de compra por edad:** para subir un nivel a puesto completo antes de los 18 hacen falta al menos 5 actualizaciones (comprar con 17 años y ≤ 70 días); a medio puesto, 9–10 actualizaciones (≤ 40 días).
- **El entrenador nivel 4 solo acelera un 8.7%** (unas 0.4 semanas por nivel). A 268,700+ no se paga con este plan.
- El juego estima desde subnivel 0 para jugadores comprados; un TSI alto puede adelantar la subida, nunca retrasarla.
- Calculadora propia: `python3 tools/entrenamiento.py --nivel 7 --edad 17 --dias 25 --hasta 9`.
- La estimación del juego es función de Supporter (prueba hasta 23-dic-2026); la calculadora no depende de eso.

## Números de velocidad (versión anterior, antes de verificar)
| Dato | Valor | Fuente |
|---|---|---|
| Asistentes | +3,5% de velocidad por nivel (máx. 10 niveles = +35%) | [oficial] |
| Entrenador nivel 5 frente a nivel 4 | "solo medio paso mejor" | [oficial] |
| Eficiencia relativa del entrenador (nivel 4 = 100%) | nivel 5: 105,3% · nivel 3: 90,9% · nivel 2: 83,3% | [comunidad] |
| Entrenamiento de habilidad efectivo | intensidad × (1 − % de resistencia) | [comunidad] |
| Jugadas, 17 años, de nivel 7 a 8, entrenador nivel 4 | 5–7 semanas por nivel (rango aproximado) | [comunidad] |
| Nuestra eficiencia mostrada | 68% | [juego] |

Con entrenador nivel 3 y dos asistentes nivel 3, la estimación de la comunidad da aproximadamente una semana más por nivel que con entrenador nivel 4. **Sin verificar con datos propios.**

## Resistencia [oficial]
- Se entrena como porcentaje del entrenamiento total; es más eficiente un poco cada semana que mucho de golpe.
- Quien jugó 90 minutos recibe el 100% del efecto; quien jugó menos, 75% más una parte por minuto; quien no jugó, 50%; lesionados, 0%.
- Subir el porcentaje **baja la forma actual** (no la forma de fondo).
- Los jugadores mayores necesitan más.
- Jugadores recién comprados: lo jugado en su equipo anterior no cuenta para entrenar esa semana [comunidad].

## Caída de habilidades [oficial]
- Empieza cerca de los 30 años, cada semana; mayor cuanto más alta la habilidad y más viejo el jugador.

## Datos de nuestra pantalla de entrenamiento [juego, 26-nov]
- Próximo entrenamiento: viernes 27-nov 03:30 HT. Actualización de caída de habilidades: lunes 30-nov 09:00 HT (aparte). Próximo cambio de intensidad efectivo: 3-dic 09:00 HT.
- Nombres de los tipos en el juego: "Passing" (interiores, extremos, delanteros), "Passing (Defenders + All Midfielders)" (mejora algo menor por entrenar a más jugadores), "Defending (Defenders, Keepers + All Midfielders)" (efecto menor), "Winger (Winger + Attackers)" (efecto menor), "Scoring and Set Pieces".
- La pantalla trae una **estimación de entrenamiento** por jugador (función de Supporter; ver nota abajo).
- Bajar la intensidad sube el ánimo; subirla lo baja.

## Nota sobre Supporter
La cuenta está en **periodo de prueba de Supporter hasta el 23-dic-2026** [juego]. Transfer Compare, la estimación de entrenamiento y las estadísticas históricas son funciones de Supporter: después de esa fecha se pierden si no se paga.

## Por verificar con datos propios
- Semanas reales por nivel de jugadas con nuestro staff (anotar cada viernes).
- Si conviene alternar semanas de "Short passes" para subir pases.
