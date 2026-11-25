# Reglas de operación

## Aprobaciones
- Claude propone el plan y **ejecuta solo con aprobación de Joan**.
- En subastas, Joan aprueba criterios y topes por adelantado; Claude hace una sola puja manual por subasta y no usa autopuja ("Max bid").
- Acciones irreversibles (despedir, vender, romper contratos) siempre se confirman antes.

## Acceso
- Navegador integrado de la app de escritorio de Claude, con la sesión iniciada por Joan. Claude no escribe contraseñas.
- La sesión vive en un servidor concreto (`www87.hattrick.org` el 25-nov). Navegar a otro `wwwNN` la cierra: usar siempre el host de la sesión activa.
- Para alineaciones, la versión simple (`/Club/Matches/MatchOrder/Simple.aspx?MatchID=…`) usa menús desplegables y es la más fiable.
- Ritmo humano: pocas páginas, sin scraping masivo.

## Riesgos
- Hattrick negó a Joan el acceso a la API CHPP.
- El manual de CHPP prohíbe la puja automática para apps aprobadas. La política sobre un asistente de IA operando por navegador **no está verificada**; hay riesgo para la cuenta.
- Recomendación pendiente: pedir confirmación escrita a soporte o a un GameMaster.

## Horarios clave (HT)
- Órdenes de partido: hasta 20 minutos antes del inicio.
- Partidos del equipo: 23:20.
- Actualización de entrenamiento: viernes 03:30.

## Fuentes de conocimiento
- Reglamento y guía oficial de Hattrick.
- hattrick-context-pack (https://github.com/rmagasi/hattrick-context-pack): útil pero no oficial; su tabla numérica de habilidades está desfasada en 1 respecto al juego y sus cifras están en €.
