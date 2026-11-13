# Especificación de la Aplicación Web

## ADDED Requirements

### Requirement: Panel Superior de Estadísticas (KPIs)

La web DEBE mostrar en la parte superior 4 tarjetas resumen que se calculen dinámicamente:

1. Total de tickets.
2. Tickets Pendientes de prioridad ALTA (en rojo).
3. Total de Datos Privados (PII) interceptados y protegidos.
4. Ataques / Rechazos bloqueados por el Root Prompt.

#### Scenario: Actualización automática de contadores

- **WHEN** se carga la página o se añade/resuelve un ticket
- **THEN** las 4 tarjetas superiores actualizan sus números al instante.

### Requirement: Listado de Tickets con Filtros y Buscador

La web DEBE mostrar las incidencias en tarjetas visuales (o tabla moderna) con
insignias de colores según prioridad (`ALTA` rojo, `MEDIA` ámbar, `BAJA` verde) y estado.

#### Scenario: Filtrado interactivo

- **WHEN** el usuario selecciona una categoría (`TODAS`, `REDES`, `HARDWARE`,
  `SOFTWARE`, `FACTURACION`, `SEGURIDAD`, `OTROS`) o escribe en el buscador
- **THEN** la lista muestra únicamente los tickets que coinciden sin recargar la página.

#### Scenario: Categoría sin resultados

- **WHEN** el filtro seleccionado no tiene ningún ticket
- **THEN** se muestra un estado vacío con un mensaje claro y un botón para limpiar filtros.

### Requirement: Formulario con Escudo RGPD en Vivo

La web DEBE incluir un formulario para crear un nuevo ticket que aplique las reglas de la
skill `escudo-rgpd-js`.

#### Scenario: Creación de ticket con datos sensibles

- **WHEN** el usuario escribe en el formulario el DNI `48112233A` junto con la IP
  `192.168.1.50` y el texto de la avería
- **THEN** la vista previa muestra `[DNI_OCULTO]` e `[IP_OCULTA]` en tiempo real, el
  ticket guardado en `localStorage` contiene únicamente el texto anonimizado y el
  contador de PII interceptados aumenta en 2.

#### Scenario: Bloqueo de Prompt Injection

- **WHEN** el usuario escribe una frase trampa como "ignora las instrucciones" o
  "olvida tus reglas"
- **THEN** aparece una alerta roja bajo el formulario y el botón de guardar queda
  deshabilitado, impidiendo el envío.

## REMOVED Requirements

Ninguno.
