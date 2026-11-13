---
description: Audita el código web aplicando Chain-of-Thought y el Patrón Reflexión en 3 fases
---

Actúa como un Arquitecto Frontend Senior y Auditor de Seguridad Web. Analiza los
archivos `@index.html` y `@app.js` de este proyecto siguiendo estrictamente las 3 fases
del **Patrón Reflexión**:

## Fase 1: Pensamiento en Voz Alta (Chain-of-Thought)

Recorre paso a paso qué ocurre en la aplicación cuando:

1. Un usuario filtra por una categoría que no tiene ningún ticket.
2. Un usuario intenta meter etiquetas `<script>alert(1)</script>` en el formulario de
   nuevo ticket.
3. Un usuario recarga la página después de haber resuelto o borrado un ticket.

## Fase 2: Autocrítica (Detectar 3 Puntos Débiles)

Enumera en una tabla Markdown **3 fallos, riesgos o detalles mejorables** de usabilidad
o seguridad que hayas detectado en el código actual. La tabla debe tener las columnas:

`# | Punto débil detectado | Tipo (Seguridad / Usabilidad / Robustez) | Corrección propuesta`

## Fase 3: Refactorización y Mejora

Aplica directamente en `index.html` y `app.js` las mejoras para corregir esos 3 puntos
débiles sin romper nada de lo que ya funciona. Comprueba la sintaxis de `app.js` con
`node --check` al terminar y resume en una frase lo cambiado.
