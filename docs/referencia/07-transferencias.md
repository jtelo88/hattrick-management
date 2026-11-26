# 07 · Transferencias

## Vender [oficial]
- Publicar cuesta **1 000 US$**, no reembolsable.
- El jugador debe haber jugado **al menos un partido** con nosotros antes de poder publicarlo (no aplica a juveniles promovidos ni a la plantilla inicial).
- Se puede cancelar en los 10 minutos siguientes si no hay pujas.
- Dura **tres días**; se va con el mejor postor.
- Máximo 50 jugadores en plantilla.

## Pujar [oficial]
- Subida mínima manual: **1 000 US$ o 2%, lo que sea mayor**.
- Una puja a menos de 3 minutos del cierre **extiende el cierre 3 minutos** (comprobado con Heinloth [juego]).
- Las pujas no se retiran.
- Pujas más primer sueldo no pueden dejarnos con más de 200 000 de deuda.
- **Autopuja ("Max bid"):** sube lo mínimo necesario; solo **una activa a la vez**; se puede cambiar el tope pero no retirar la puja actual; cuando alcanza su tope deja de contar y se puede poner otra. Solo nosotros vemos nuestro tope.

## Comisiones al vender
| Concepto | Valor | Fuente |
|---|---|---|
| Club de origen | 2% del precio (no al vender por primera vez a un canterano propio) | [oficial] |
| Club anterior | 3% del precio va a un fondo; lo que recibe el club anterior depende de los partidos que jugó con él | [oficial] |
| Agente | Depende del tiempo en el club | [oficial]; tabla abajo |
| Lo que cobra el club anterior | 0% con 0 partidos; 0,25% con 1; 0,5% con 2; 1% con 3; 1,5% con 4; 2% con 5; 2,5% con 7; 3% con 10; 3,5% con 20; 4% con 40 | [oficial, Apéndice 4] |

Comisión del agente según tiempo en nuestro club [oficial, Apéndice 4 del reglamento, leído en el juego el 26-nov]:

| Tiempo | Comisión | Tiempo | Comisión |
|---|---|---|---|
| 0 días | 12,00% | 6 semanas | 5,09% |
| 1 día | 10,45% | 8 semanas | 4,24% |
| 3 días | 9,59% | 10 semanas | 3,52% |
| 1 semana | 8,62% | 12 semanas | 2,88% |
| 2 semanas | 7,55% | 14 semanas | 2,30% |
| 4 semanas | 6,12% | 16 semanas o más | 2,00% (mínimo) |

La ficha de cada jugador muestra cuánto nos quedaría al venderlo [oficial]: **esa cifra del juego manda**.

## Efectos secundarios [oficial]
- Comprar o vender puede **bajar el ánimo del equipo** (ver 03).
- Vender puede restar un poco de experiencia de formación.
- Las reservas de la directiva solo se quedan con parte de la venta en casos raros (porteros con portería solid o más, o candidatos a entrenador, que no sean titulares). No nos aplica.
- Está prohibido comprar a precios inflados; el valor de mercado depende de habilidades, edad, rareza y potencial de selección.

## Lo que dice nuestro mercado [juego, 26-nov]
- El precio a horas del cierre no indica el precio final: Ibañez pasó de 12 000 a 186 000 en siete horas; Stas de 7 000 a 382 500.
- Dentro del mismo nivel visible, el TSI alto y pocos días de edad multiplican el precio.
- "Potencial de selección" es un factor oficial del valor: explica los precios de más de 1 000 000 en juveniles de ciertos países [inferencia].
- Datos: `data/ventas.csv`, `data/subastas-seguidas.csv`, `docs/base-de-precios.md`.

## Edad y precio [juego, Transfer Compare, 26-nov]
- Jugadas 10 sin secundarias: mediana de 162 210 a los 18 años y de **48 000 a los 19**. El mismo jugador pierde unos dos tercios de su precio al cumplir 19.
- Por eso se compra con 17 años y pocos días y se vende antes de los 19.
- La especialidad separa los precios dentro de un mismo perfil: en jugadas 7 + pases 5 de 17 años, sin especialidad se vendieron entre 5 000 y 157 000; con especialidad, entre 157 000 y 1 010 000.
- La ficha de cada jugador en venta muestra un "Estimated Value" (promedio de Transfer Compare). Es un promedio inflado por los casos extremos: usar la mediana y los comparables de TSI parecido.

## Reglas operativas que salen de aquí
- Antes de pujar: Transfer Compare, TSI, especialidad y **personalidad** (no comprar "nasty fellow" ni "controversial person": riesgo de ánimo).
- Un aprendiz comprado y revendido antes de 16 semanas paga más comisión: vender a las 16 semanas o más deja ~6–7% de costos totales; revender en la primera semana, ~14% o más.
- Cada compra que no vaya a jugar es un riesgo de ánimo sin beneficio: comprar solo lo que entra en un cupo.
