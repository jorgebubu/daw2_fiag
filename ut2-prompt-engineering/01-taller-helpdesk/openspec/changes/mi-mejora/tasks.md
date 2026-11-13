# Plan de Implementación: Exportador de Informes

- [x] **Paso 1:** Añadir el botón "Exportar informe" y su icono en la cabecera de
      `index.html`, con `id="btn-exportar"`.
- [x] **Paso 2:** Implementar en `app.js` las funciones `generarInformeMarkdown()`
      (construye el texto) y `descargarArchivo(nombre, contenido)` (Blob + enlace
      temporal).
- [x] **Paso 3:** Conectar el evento `click`, mostrar un aviso de éxito y comprobar que
      las cifras del informe coinciden con los KPIs del panel.
- [x] **Paso 4:** Probar el informe con tickets resueltos, filtros activos y un ticket
      nuevo creado desde el formulario.
