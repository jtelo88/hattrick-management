# Reglas de operación

## Aprobaciones
- Claude propone el plan y **ejecuta solo con aprobación de Joan**.
- En subastas, Joan aprueba criterios y topes por adelantado; Claude puja dentro del tope y se detiene al alcanzarlo. Subir un tope requiere nueva aprobación.
- Solo hay **un autobid ("Max bid") gratis a la vez**; los adicionales cuestan 2 Credits (dinero real) y no se compran. El resto son pujas manuales.
- Pelear contra el autobid de un rival solo revela su techo subiendo el precio: decidir el tope antes y no perseguir (caso Stas, 26-nov).
- Mensajes a otros mánagers: nunca se envían sin texto aprobado por Joan. Al ojeador de Bután Sub-21 se decidió no responder.
- Acciones irreversibles (despedir, vender, romper contratos) siempre se confirman antes.

## Acceso
- Navegador integrado de la app de escritorio de Claude, con la sesión iniciada por Joan. Claude no escribe contraseñas.
- La sesión caduca sola tras unas horas y al volver a entrar puede cambiar de servidor (www87 el 25-nov; www84 el 26-nov). Antes de navegar, leer el host de la pestaña activa.
- La sesión vive en un servidor concreto (`www87.hattrick.org` el 25-nov). Navegar a otro `wwwNN` la cierra: usar siempre el host de la sesión activa.
- Para alineaciones, la versión simple (`/Club/Matches/MatchOrder/Simple.aspx?MatchID=…`) usa menús desplegables y es la más fiable.
- Ritmo humano: pocas páginas, sin scraping masivo.

## Seguimiento programado
- Las revisiones se programan como mensajes diferidos a esta sesión. **Solo funcionan con la app de escritorio abierta y la sesión de Hattrick activa** (el 25-nov se perdió a Conor Ross por sesión cerrada).
- Un clasificador de seguridad bloqueó el clic de "Add your team to pool"; no se rodea: Joan hace ese clic.
- No se ingresan credenciales de Hattrick en sitios externos (p. ej. trackers).

## Riesgos
- El editorial del 10-nov-2026 anuncia una revisión de los acuerdos CHPP "adding better privacy and AI use protection for end users". Se refiere a desarrolladores de aplicaciones; qué implica para un asistente de IA por navegador sigue sin verificar.
- La prueba de Supporter vence el 23-dic-2026; varias herramientas que usamos dependen de ella.
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
