# Plan de Construcción Encadenado (Prompt Chaining)

- [x] **Eslabón 1 (Estructura HTML y Diseño):** Crear `index.html` con TailwindCSS
      incluyendo la cabecera, las 4 tarjetas KPI, la barra de filtros/búsqueda, el
      contenedor de tickets y el modal/formulario de nuevo ticket con vista previa RGPD.
- [x] **Eslabón 2 (Motor de Datos y Filtros JS):** Crear `app.js` cargando los datos
      iniciales de `datos_tickets.json` en `localStorage`, renderizando las tarjetas con
      el razonamiento de la IA, los filtros en vivo y el botón para marcar tickets como
      "RESUELTO".
- [x] **Eslabón 3 (Integración de la Skill Escudo RGPD):** Implementar en `app.js` las
      funciones de la skill `escudo-rgpd-js` (sanitización PII en vivo con regex y
      bloqueo de Prompt Injection en el formulario).

## Notas de ejecución

- Cada eslabón se ha ejecutado en una sesión distinta de OpenCode, leyendo el anterior.
- El resultado de cada paso se ha validado abriendo `index.html` en el navegador.
- La auditoría de la Fase 5 (`/reflexionar-calidad`) se aplicó después del Eslabón 3.
