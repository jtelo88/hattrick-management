# Base de datos de precios de transferencias

Objetivo: saber cuándo un jugador está caro o barato antes de pujar, y a cuánto se revende ya entrenado.

## Archivos
- `data/ventas.csv` — ventas **cerradas** (precio final real). Fuente: herramienta Transfer Compare del juego (10 últimas ventas por perfil). Una fila por venta.
- `data/subastas-seguidas.csv` — subastas que vimos abiertas (nuestras y de referencia). Se completa `precio_final` y `ganador` cuando cierran; así medimos cuánto sube el precio entre "X horas antes" y el cierre.

## Cómo se alimenta
1. En cada revisión: abrir las subastas seguidas ya cerradas (pestaña Transfers del jugador) y anotar precio final.
2. Por cada perfil que nos interese comprar o vender: leer Transfer Compare y añadir las ventas nuevas (clave: player_id + fecha).
3. Perfiles a cubrir: 17a PM7 (D5/D6/D7, con y sin pases), 17a W7; 18a y 19a PM9/PM10/PM11 (mono, +D, +P); extremos equivalentes.

## Reglas de lectura (provisionales, 26-nov, n=10 por perfil)
- Precio depende de: nivel visible, TSI (subnivel oculto), días de edad, especialidad, secundarias. Posible factor no visible: nacionalidad (selecciones Sub-21) — sin verificar.
- "Barato" = por debajo del percentil 25 de su perfil con TSI igual o mayor a la mediana. "Caro" = por encima de la mediana con TSI menor.
- El precio a varias horas del cierre NO es el precio final: registrar ambos para calcular el multiplicador.

## Aporte en el campo
Antes de pujar, calcular el aporte del candidato con `tools/aporte.py` (ver `docs/referencia/04-contribucion-por-puesto.md`) y compararlo con el de los aprendices actuales: un jugador se compra si mejora una línea o si su perfil se revende mejor, no solo por precio.

## Limitaciones
- Transfer Compare solo da 10 ventas y agrupa con criterios propios; la muestra es chica y los rangos anchos.
- Sin acceso CHPP, la carga es manual por navegador.

## Escalera con pases como secundaria (28-nov-2026) [juego, Transfer Compare]

17 años con ≥ 25 días, 10 ventas por perfil:

| Perfil | Mediana | Rango | Sin especialidad |
|---|---|---|---|
| PM6 + P6 | 13,000 | 1,000–96,900 | 1,000 · 25,000 |
| PM7 + P6 | 63,503 | 4,000–419,000 | 4,000 · 5,000 · 23,000 · 102,005 |
| PM8 + P6 | 246,000 | 99,000–650,000 | 128,000 · 180,000 |

Comparación con defensa: PM7+D6 mediana 4,000; PM8+D6 mediana 102,990. **Pases 6 vale mucho más que defensa 6 en un jugador de jugadas.** Los de más de 100 días y sin especialidad caen a 4,000–5,000.
