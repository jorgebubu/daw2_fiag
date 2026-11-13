# Propuesta: Exportador de Informes Ejecutivos en Markdown

## Por qué (Objetivo)

El responsable del taller necesita entregar cada viernes un resumen del estado de las
incidencias a dirección, sin copiar y pegar capturas. Hoy hay que revisar el panel a
mano. Queremos que la propia web genere un informe listo para adjuntar en un correo.

## Qué se construye (Alcance)

Un botón **"Exportar informe"** en la cabecera que genere y descargue automáticamente
`informe_incidencias.md` con:

- Fecha y hora de generación.
- Tabla de KPIs (total, pendientes ALTA, PII protegidos, bloqueos).
- Tabla de incidencias agrupadas por categoría y prioridad.
- Lista de tickets urgentes pendientes con su solución sugerida y tiempo estimado.
- Resumen de datos PII protegidos por tipo.
- Pie con el aviso de que el informe se ha generado en el navegador y no contiene PII.

## Por qué en Markdown

- Se genera en el cliente con un `Blob` (sin backend ni dependencias).
- Se puede pegar en el correo, en Notion o convertir a PDF.
- Es texto plano: no arrastra estilos ni datos ocultos.
