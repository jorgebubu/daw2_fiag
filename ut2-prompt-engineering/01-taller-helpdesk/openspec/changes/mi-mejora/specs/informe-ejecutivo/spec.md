# Especificación: Exportador de Informes Ejecutivos

## ADDED Requirements

### Requirement: Botón de exportación

La aplicación DEBE mostrar un botón "Exportar informe" en la cabecera, visible en
escritorio y móvil.

#### Scenario: Descarga del informe

- **WHEN** el usuario pulsa "Exportar informe"
- **THEN** el navegador descarga un archivo llamado `informe_incidencias.md` sin recargar
  la página ni pedir confirmación.

### Requirement: Contenido mínimo del informe

El informe DEBE incluir la fecha de generación, una tabla de KPIs, una tabla de
incidencias por categoría y prioridad, la lista de tickets urgentes pendientes y un
resumen de los tipos de PII protegidos.

#### Scenario: Informe coherente con el panel

- **WHEN** existen 10 tickets, 4 pendientes de prioridad ALTA y 12 datos PII protegidos
- **THEN** las cifras del informe coinciden exactamente con las tarjetas KPI del panel.

#### Scenario: Informe sin datos personales

- **WHEN** se genera el informe
- **THEN** ningún ticket incluye DNI, teléfonos, tarjetas, IBAN, matrículas, IPs ni
  contraseñas reales: solo aparecen los placeholders `[DNI_OCULTO]`, etc.

## REMOVED Requirements

Ninguno.
