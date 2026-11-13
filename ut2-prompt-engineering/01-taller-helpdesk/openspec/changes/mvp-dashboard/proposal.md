# Propuesta: Dashboard Web MotorShield Taller - JM

## Por qué (Objetivo)

Necesitamos una interfaz web rápida, visual y segura para que el equipo del taller
MotorShield consulte las incidencias procesadas en `datos_tickets.json`, filtre por
urgencia, cambie estados y registre nuevos tickets con protección automática de datos
personales (RGPD). Hoy los avisos llegan por correo y WhatsApp mezclados con datos
sensibles, y se pierden incidentes críticos entre consultas que no son del área TIC.

## Qué se construye (Alcance)

Un Dashboard SPA (Single Page Application) en `index.html` y `app.js` usando
TailwindCSS y `localStorage`.

Incluye:

- Cabecera con identidad del taller (**MotorShield Taller - JM**) y modo claro/oscuro.
- Cuatro tarjetas KPI calculadas dinámicamente (total, pendientes de prioridad ALTA,
  PII interceptados y ataques/rechazos bloqueados).
- Listado de tickets en tarjetas con insignias de prioridad y estado, buscador y
  filtros por categoría.
- Formulario de alta de ticket con vista previa RGPD en vivo y detector de Prompt
  Injection en el cliente.
- Persistencia de los cambios en `localStorage`, con datos de respaldo embebidos para
  que la web funcione también abriendo el archivo directamente.

## Fuera de alcance (en esta primera iteración)

- Backend, autenticación de usuarios y base de datos en la nube.
- Envío real de correos al cliente.
- Paginación: el volumen previsto (decenas de tickets) no la requiere.
