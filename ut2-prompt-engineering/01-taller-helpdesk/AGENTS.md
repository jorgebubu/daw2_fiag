# Contexto del Proyecto: MotorShield Taller - JM

## Descripción General

Aplicación web interactiva (Dashboard) para gestionar las incidencias informáticas
del taller mecánico **MotorShield Taller**, desarrollada por **Jorge Montalbán**,
garantizando que ningún dato personal sensible (PII) quede expuesto según normativa RGPD.

El panel centraliza los avisos que llegan al buzón TIC del taller (recepción, TPV,
elevadores conectados, red WiFi de la nave y facturación), los anonimiza, los clasifica
por prioridad y permite hacer seguimiento hasta su resolución.

## Stack Tecnológico Obligatorio

- **Frontend:** HTML5 semántico en un archivo `index.html`.
- **Estilos:** TailwindCSS cargado mediante CDN oficial (no usar compiladores
  complejos para facilitar el despliegue directo). Diseño moderno, limpio y
  responsive con soporte para modo claro/oscuro.
- **Lógica:** JavaScript Vanilla moderno (ES6+) en un archivo `app.js`.
- **Persistencia de Datos:** Carga inicial desde `datos_tickets.json` y
  guardado de cambios en `localStorage` del navegador.

## Reglas de Código para el Agente

1. Todo el código y los comentarios deben estar en **español**.
2. NUNCA uses `innerHTML` directamente con textos de usuario sin escapar para
   evitar vulnerabilidades XSS.
3. Mantén las funciones pequeñas, claras y fáciles de entender por un
   estudiante de 2º de DAW.
4. La aplicación debe funcionar también abriendo `index.html` directamente en el
   navegador (sin servidor local): incluye los datos de respaldo dentro de `app.js`.
5. No incluyas claves de API ni secretos en el repositorio. El despliegue es
   estático (Netlify Drop / Vercel).

## Identidad Visual

- Nombre comercial: **MotorShield Taller - JM**
- Paleta: azul acero (`#0f172a`), ámbar de taller (`#f59e0b`) y verde de
  "resuelto" (`#10b981`).
- Tono de los textos: cercano pero profesional, en español de España.
