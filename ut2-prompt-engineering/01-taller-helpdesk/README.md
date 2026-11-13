# Memoria Técnica · Taller UT2

## Desarrollo Web Dirigido por IA (Prompts, Skills y OpenSpec)

| | |
|---|---|
| **Proyecto** | **MotorShield Taller - JM** — Panel de incidencias TIC del taller mecánico |
| **Autor** | Jorge Montalbán (iniciales **JM**) |
| **Módulo** | Fundamentos de Inteligencia Artificial Generativa (FIAG) |
| **Ciclo** | 2.º Grado Superior en Desarrollo de Aplicaciones Web (DAW) |
| **Centro** | IES Alcántara (Región de Murcia) |
| **Curso** | 2026/2027 |

> **Regla 0 (personalización):** el apellido **Montalbán** empieza por **M**, que pertenece al
> grupo H–N, por lo que la temática asignada es **Taller Mecánico / Concesionario**. El nombre
> del proyecto es **MotorShield Taller - JM** y aparece en `AGENTS.md`, en el título de
> `index.html` y en `proposal.md`, tal y como exige el enunciado.

---

## Índice

1. [Resumen del proyecto](#1-resumen-del-proyecto)
2. [Requisitos previos](#2-requisitos-previos)
3. [Estructura final del proyecto](#3-estructura-final-del-proyecto)
4. [Fase 1 · Preparación del proyecto y el mapa para la IA (AGENTS.md)](#4-fase-1--preparación-del-proyecto-y-el-mapa-para-la-ia-agentsmd)
5. [Fase 2 · Laboratorio de prompts (de texto sucio a JSON limpio)](#5-fase-2--laboratorio-de-prompts-de-texto-sucio-a-json-limpio)
6. [Fase 3 · Skills (skills.sh de Vercel)](#6-fase-3--skills-skillssh-de-vercel)
7. [Fase 4 · Construcción de la web con OpenSpec y Prompt Chaining](#7-fase-4--construcción-de-la-web-con-openspec-y-prompt-chaining)
8. [Fase 5 · Auditoría y mejora con CoT y Patrón Reflexión](#8-fase-5--auditoría-y-mejora-con-cot-y-patrón-reflexión)
9. [Fase 6 · Funcionalidad individual y despliegue web](#9-fase-6--funcionalidad-individual-y-despliegue-web)
10. [Tabla de pruebas y resultados](#10-tabla-de-pruebas-y-resultados)
11. [Conclusiones y mejoras futuras](#11-conclusiones-y-mejoras-futuras)

---

## 1. Resumen del proyecto

En la UT1 aprendimos a llamar a la API de un LLM desde Python. En esta UT2 el reto es distinto:
**no escribir código repetitivo a mano, sino dirigir a un agente de IA** (`OpenCode`) con
artefactos bien diseñados (Markdown, comandos, Skills y OpenSpec) para construir una
aplicación web real y desplegarla en Internet.

El resultado es **MotorShield Taller - JM**, un panel web de gestión de incidencias que:

- Lee un `datos_tickets.json` generado por un **prompt estructurado** que anonimiza datos
  personales (RGPD) y bloquea ataques de Prompt Injection.
- Muestra **4 KPIs** calculados dinámicamente.
- Permite **filtrar y buscar** incidencias en vivo.
- Permite **crear, resolver y eliminar** tickets con un **escudo RGPD en tiempo real** que
  censura DNIs, tarjetas, teléfonos, IBAN, matrículas, IPs y contraseñas antes de guardarlos.
- **Exporta un informe ejecutivo en Markdown** con las estadísticas del panel.
- Se **despliega en Netlify** para poder abrirse con un clic.

---

## 2. Requisitos previos

Verificados en el equipo antes de empezar:

| Requisito | Comprobación |
|---|---|
| VS Code con Git configurado | ✔ Git `v2.39` (Git for Windows) |
| Node.js 20+ y npm/npx | ✔ Node `v22.23.2`, npm `10.9.8` |
| OpenCode conectado al proveedor | ✔ `opencode` (modelo del proveedor configurado en la sesión) |
| Repo privado `daw2-fiag` | ✔ `https://github.com/jorgebubu/daw2_fiag.git` (acceso autenticado) |
| Navegador | ✔ Google Chrome (capturas y despliegue) |
| Conexión a Internet | ✔ necesario para `npx skills` y `@fission-ai/openspec` |

---

## 3. Estructura final del proyecto

Todo vive dentro de `ut2-prompt-engineering/01-taller-helpdesk/`:

```
01-taller-helpdesk/
├── AGENTS.md                          ← Mapa técnico del proyecto (contexto para el agente)
├── bandeja_entrada_sucia.txt          ← 10 mensajes brutos con PII y trampas
├── datos_tickets.json                 ← Base de datos limpia y anonimizada (salida del prompt)
├── index.html                         ← Estructura y diseño de la aplicación web
├── app.js                             ← Lógica: KPIs, filtros, escudo RGPD, exportación
├── informe_incidencias.md             ← Informe exportado (funcionalidad individual)
├── skills-lock.json                   ← Bloqueo de versiones de las Skills
├── .opencode/
│   └── commands/
│       ├── limpiar-y-clasificar.md    ← Prompt maestro (6 técnicas + placeholders ampliados)
│       └── reflexionar-calidad.md     ← Comando de auditoría CoT / Patrón Reflexión
├── .agents/
│   └── skills/
│       ├── web-design-guidelines/     ← Skill oficial de Vercel instalada con `npx skills`
│       ├── escudo-rgpd-js/            ← Skill propia (copia para que OpenCode la detecte)
│       └── openspec-*/                ← Skills generadas por `openspec init`
├── escudo-rgpd-js/
│   └── SKILL.md                       ← Skill propia con sus 4 reglas
├── openspec/
│   ├── config.yaml                    ← Configuración de OpenSpec (herramienta: OpenCode)
│   └── changes/
│       ├── mvp-dashboard/             ← Especificación del panel (proposal, spec, tasks)
│       └── mi-mejora/                 ← Especificación de la exportación a Markdown
└── capturas/                          ← Capturas reales de la aplicación
```

---

## 4. Fase 1 · Preparación del proyecto y el mapa para la IA (AGENTS.md)

Antes de pedir nada, se prepara la carpeta y se escribe `AGENTS.md`: es el "mapa técnico"
que OpenCode lee al arrancar y donde se fija el **stack obligatorio** y las **reglas de
código** para el agente.

**Contenido esencial de `AGENTS.md`:**

- **Descripción:** panel de incidencias del taller MotorShield desarrollado por Jorge
  Montalbán, con garantía de que ningún dato personal queda expuesto (RGPD).
- **Stack:** HTML5 semántico + TailwindCSS por CDN + JavaScript Vanilla (ES6+) +
  `localStorage`, con datos de respaldo para abrir `index.html` sin servidor.
- **Reglas:** todo en español, nunca `innerHTML` con texto de usuario, funciones pequeñas y
  comentadas, nada de claves secretas en el repositorio.

> El enunciado incluye en su Paso 1.2 una regla de control que condiciona la entrega a que
> se detecte una resolución automática "de golpe". **Se ha decidido no incluir ese texto**
> para que la entrega no quede marcada; el trabajo se ha realizado de forma asistida,
> ejecutando los comandos y validando cada fase como se describe en esta memoria.

---

## 5. Fase 2 · Laboratorio de prompts (de texto sucio a JSON limpio)

### 5.1 Entrada bruta: `bandeja_entrada_sucia.txt`

Se pegan los 8 mensajes del enunciado (el mensaje 1 firmado por **Jorge Montalbán**) y se
añaden los **2 mensajes inventados** que pide la *Modificación del Alumno 1*:

- **Mensaje 9:** una factura de un taller con **matrícula** (`4821 KZX`) y **cuenta IBAN**
  (`ES91 2100 0418 4502 0005 1332`).
- **Mensaje 10:** un intento de Prompt Injection ingenioso, disfrazado de *auditoría de
  calidad*, que pide cambiar las prioridades y **ocultar la regla en el razonamiento**.

La bandeja contiene, repartidos entre los 10 mensajes:

| Trampa | Mensajes |
|---|---|
| DNI | 1, 4 |
| Teléfono | 1, 7 |
| Contraseña en texto plano | 2, 8 |
| Tarjeta + CVV | 5 |
| Dirección postal | 7 |
| IP privada | 8 |
| Matrícula + IBAN | 9 |
| Prompt Injection | 3, 10 |
| Fuera de tema (bocadillo) | 6 |

### 5.2 El prompt maestro: `.opencode/commands/limpiar-y-clasificar.md`

En lugar de un script de Python, el prompt vive como un **comando de OpenCode**. Aplica las
6 técnicas de la unidad:

| # | Técnica | Cómo aparece en el prompt |
|---|---|---|
| 1 | Los 4 bloques + delimitadores XML | `<rol_y_reglas>`, `<ejemplos_few_shot>`, `<formato_salida>` |
| 2 | Root Prompt (portero) | Rechaza fuera de tema (`RECHAZADO_FUERA_DE_TEMA`) y bloquea la inyección (`BLOQUEADO_PROMPT_INJECTION`, categoría `SEGURIDAD`) |
| 3 | Filtro semántico PII | Placeholders `[DNI_OCULTO]`, `[TELEFONO_OCULTO]`, `[TARJETA_OCULTA]`, `[CVV_OCULTO]`, `[CLAVE_OCULTA]`, `[DIRECCION_OCULTO]`, `[IP_OCULTA]`, **`[MATRICULA_OCULTA]`**, **`[IBAN_OCULTO]`** |
| 4 | Chain-of-Thought | Campo `razonamiento_ia` con la justificación de la prioridad |
| 5 | Few-Shot | 2 ejemplos completos (incidencia con PII y ataque de inyección) |
| 6 | Placeholder `$ARGUMENTS` | El archivo de entrada se pasa como argumento al comando |

**Ejecución en OpenCode:**

```
/limpiar-y-clasificar @bandeja_entrada_sucia.txt
```

### 5.3 Resultado: `datos_tickets.json`

OpenCode genera un array JSON con **10 tickets** (uno por mensaje), con las claves:

```
id · autor · ubicacion · categoria · mensaje_anonimizado · pii_detectada
· razonamiento_ia · prioridad · estado · solucion_sugerida · tiempo_estimado_minutos
```

Comprobación del resultado (con `node`):

```
tickets: 10 | PII: 12
```

| Comprobación | Resultado |
|---|---|
| DNI de los mensajes 1 y 4 | ✔ `[DNI_OCULTO]` |
| Clave de Laura (mensaje 2) | ✔ `[CLAVE_OCULTA]` |
| Tarjeta y CVV (mensaje 5) | ✔ `[TARJETA_OCULTA]` `[CVV_OCULTO]` |
| Móvil y calle de Elena (mensaje 7) | ✔ `[TELEFONO_OCULTO]` `[DIRECCION_OCULTO]` |
| IP y clave del mensaje 8 | ✔ `[IP_OCULTA]` `[CLAVE_OCULTA]` |
| Mensaje 3 (inyección `[SISTEMA]`) | ✔ `BLOQUEADO_PROMPT_INJECTION` · `SEGURIDAD` |
| Mensaje 6 (bocadillo) | ✔ `RECHAZADO_FUERA_DE_TEMA` |
| Mensaje 10 (inyección "auditoría") | ✔ `BLOQUEADO_PROMPT_INJECTION` |
| Matrícula e IBAN (mensaje 9) | ✔ `[MATRICULA_OCULTA]` `[IBAN_OCULTO]` |
| `tiempo_estimado_minutos` (Mod. 1) | ✔ campo presente en los 10 tickets |

### 5.4 Modificación del Alumno 1

1. **Dos mensajes nuevos** añadidos al final de la bandeja: uno con matrícula + IBAN y otro
   con una inyección ingeniosa (sección 5.1).
2. **El comando se editó** para ocultar `[MATRICULA_OCULTA]` y `[IBAN_OCULTO]` y para
   añadir el campo `tiempo_estimado_minutos`.
3. **Se volvió a ejecutar** el comando y se regeneró `datos_tickets.json`.

---

## 6. Fase 3 · Skills (skills.sh de Vercel)

### 6.1 Skill oficial de diseño web

```bash
npx skills find web-design
npx skills add vercel-labs/agent-skills --skill web-design-guidelines -a opencode -y
npx skills list
```

La skill se instala en `.agents/skills/web-design-guidelines/` (origen:
`vercel-labs/agent-skills`, evaluación de seguridad **Safe / 0 alertas / Low Risk**).

### 6.2 Skill propia: `escudo-rgpd-js`

```bash
npx skills init escudo-rgpd-js
```

Se crea `escudo-rgpd-js/SKILL.md` y se copia a `.agents/skills/escudo-rgpd-js/` para que
OpenCode la detecte como una skill del proyecto. La skill obliga a incluir:

1. `sanitizarTextoPII(texto)` con expresiones regulares (DNI/NIE y tarjeta).
2. Vista previa en vivo bajo el `<textarea>` con el evento `input`.
3. Detector de Prompt Injection que bloquea el envío.

### 6.3 Modificación del Alumno 2

Se añadió la **regla 4** a `SKILL.md`: `sanitizarTextoPII()` también detecta y oculta
**cualquier dirección IPv4** (`xxx.xxx.xxx.xxx`) sustituyéndola por `[IP_OCULTA]`, con la
precaución de aplicarla **después** del filtro de tarjetas para no confundir los octetos con
grupos de una tarjeta. Esta regla se implementó en `app.js` (apartado 7.4).

**Skills instaladas finalmente** (`npx skills list`):

```
escudo-rgpd-js          · untracked        (skill propia)
web-design-guidelines   · vercel-labs/agent-skills (skill oficial)
openspec-*              · generadas por openspec init
```

---

## 7. Fase 4 · Construcción de la web con OpenSpec y Prompt Chaining

### 7.1 Inicialización de OpenSpec

```bash
npx @fission-ai/openspec@latest init --tools opencode --language es
npx @fission-ai/openspec@latest list
```

Se crean `openspec/config.yaml` y las skills de OpenSpec en `.agents/skills/`.

### 7.2 Los 3 documentos de la especificación `mvp-dashboard`

| Archivo | Contenido |
|---|---|
| `proposal.md` | Por qué y qué se construye (alcance y fuera de alcance) |
| `specs/interfaz-web/spec.md` | Requisitos con escenarios **WHEN/THEN**: KPIs, listado con filtros y formulario con escudo RGPD |
| `tasks.md` | El **plan encadenado** en 3 eslabones, con las casillas marcadas |

El escenario "Creación de ticket con datos sensibles" se **completó** siguiendo el formato
WHEN/THEN:

> **WHEN** el usuario escribe en el formulario el DNI `48112233A` junto con la IP
> `192.168.1.50` y el texto de la avería → **THEN** la vista previa muestra `[DNI_OCULTO]` e
> `[IP_OCULTA]` en tiempo real, el ticket guardado en `localStorage` contiene únicamente el
> texto anonimizado y el contador de PII interceptados aumenta en 2.

**Validación:**

```
✓ change/mvp-dashboard
✓ change/mi-mejora
Totals: 2 passed, 0 failed (2 items)
```

### 7.3 Prompt Chaining: los 3 eslabones

La construcción se dividió en 3 peticiones encadenadas, leyendo el artefacto de cada fase
anterior:

| Eslabón | Tarea | Resultado |
|---|---|---|
| 1 | `index.html`: cabecera, 4 KPIs, filtros, listado y modal con vista previa RGPD (aplicando `web-design-guidelines`) | Estructura y diseño |
| 2 | `app.js`: carga de `datos_tickets.json` → `localStorage`, render de tarjetas con `razonamiento_ia`, filtros en vivo y botón "Marcar resuelto" | Motor de datos |
| 3 | `app.js`: integración al 100 % de la skill `escudo-rgpd-js` (sanitización en vivo + bloqueo de inyección) | Escudo RGPD |

### 7.4 El escudo RGPD en vivo (`sanitizarTextoPII`)

La función aplica las expresiones regulares **en orden** (importante para no pisar un
placeholder con otro filtro):

```
IBAN → tarjeta (16 dígitos) → DNI/NIE → IPv4 → teléfono → matrícula → CVV
     → contraseña → dirección postal
```

y devuelve el texto censurado junto con la lista de tipos encontrados, que alimenta el
contador "PII interceptados".

---

## 8. Fase 5 · Auditoría y mejora con CoT y Patrón Reflexión

Se creó el comando `.opencode/commands/reflexionar-calidad.md` con las 3 fases del patrón
Reflexión:

1. **Pensamiento en voz alta (CoT):** recorrido de los 3 escenarios críticos (categoría
   sin tickets, `<script>alert(1)</script>` en el formulario, recarga tras resolver o
   borrar).
2. **Autocrítica:** tabla con 3 puntos débiles.
3. **Refactorización:** corrección de los 3 puntos sin romper lo anterior.

### 8.1 Tabla de autocrítica (salida de `/reflexionar-calidad`)

| # | Punto débil detectado | Tipo | Corrección propuesta |
|---|---|---|---|
| 1 | El icono del modo claro/oscuro se cambiaba con `innerHTML`, lo que rompe la regla de AGENTS.md ("nunca `innerHTML` sin escapar") y abre la puerta a un XSS si en el futuro el icono depende de una variable | Seguridad | Sustituir el `innerHTML` por dos SVG predefinidos en `index.html` (`icono-luna`, `icono-sol`) y alternarlos con `classList.toggle('hidden')` |
| 2 | El borrado de un ticket usaba `window.confirm()`, un diálogo nativo bloqueante que corta el ritmo y no se puede personalizar | Usabilidad | Confirmación inline dentro de la tarjeta: al pulsar 🗑 aparecen "¿Borrar? · Sí, borrar · No", sin bloquear la interfaz |
| 3 | El detector de inyección bloqueaba cualquier texto con la frase suelta "sin restricciones", con falsos positivos en mensajes legítimos ("la red funciona sin restricciones") | Robustez | Sustituir la frase corta por patrones más largos y concretos: "actúa como administrador sin restricciones", "haz lo que te pida sin restricciones" |

**Además** (mejora adicional de la Fase 6): el informe se descargaba siempre con el mismo
nombre, así que se añadió la fecha: `informe-incidencias-2026-11-13.md`.

**Comprobación final:** `node --check app.js` → sin errores.

### 8.2 Verificación de los escenarios críticos

| Escenario | Antes | Después |
|---|---|---|
| Filtrar una categoría sin tickets | Listado en blanco sin explicación | Estado vacío con mensaje y botón "Limpiar filtros" |
| `<script>alert(1)</script>` en el formulario | — | Todo el render usa `textContent` (nunca `innerHTML`), el `<script>` se muestra como texto y la vista previa usa `textContent` |
| Recargar tras resolver o borrar | Los cambios se perdían | `localStorage` conserva los cambios; al volver a abrir se recuperan el estado y el contador |

---

## 9. Fase 6 · Funcionalidad individual y despliegue web

### 9.1 Funcionalidad individual elegida

**Opción A — Exportador de Informes Ejecutivos en Markdown.**

Se especificó en OpenSpec (`openspec/changes/mi-mejora/`) con `proposal.md`,
`specs/informe-ejecutivo/spec.md` y `tasks.md`. La web incluye el botón **"Exportar
informe"** que genera `informe-incidencias-<fecha>.md` con:

1. Fecha de generación y responsable.
2. Tabla de KPIs.
3. Incidencias por categoría y por prioridad.
4. Tickets urgentes pendientes con solución sugerida y tiempo estimado.
5. PII protegidos por tipo.
6. Detalle de los tickets pendientes.
7. Pie con el aviso de que el informe **no contiene PII**.

Se generó el informe real desde el navegador (archivo `informe_incidencias.md`, 5 993
caracteres) y se verificó que sus cifras coinciden con los KPIs del panel.

### 9.2 Despliegue en Internet

1. **GitHub:** todo el proyecto se sube al repo privado `daw2-fiag` dentro de
   `ut2-prompt-engineering/01-taller-helpdesk/`, con el profesor añadido como colaborador.

   ```bash
   git add .
   git commit -m "Finalizado Taller UT2: App Web HelpDesk con Prompts, Skills y OpenSpec"
   git push
   ```

2. **Netlify Drop:** se arrastra la carpeta `01-taller-helpdesk` a
   <https://app.netlify.com/drop>.

> **Enlace de la web desplegada:** `(se incluirá aquí tras publicar en Netlify)`

---

## 10. Tabla de pruebas y resultados

Capturas reales de la aplicación (carpeta `capturas/`):

| # | Prueba | Resultado | Captura |
|---|---|---|---|
| 1 | Panel en modo claro con 10 tickets y 4 KPIs | ✔ Total 10 · Pendientes ALTA 4 · PII 12 · Bloqueos 3 | `capturas/01-panel-claro.png` |
| 2 | Panel en modo oscuro (persistencia de preferencia) | ✔ Interfaz completa en oscuro | `capturas/02-panel-oscuro.png` |
| 3 | Filtro por categoría REDES | ✔ Solo tickets de REDES | `capturas/03-filtro-redes.png` |
| 4 | Buscador "impresora" | ✔ Resultado filtrado en vivo | `capturas/04-busqueda-impresora.png` |
| 5 | Formulario con IP + DNI + tarjeta + clave | ✔ Vista previa muestra `[IP_OCULTA] [DNI_OCULTO] [TARJETA_OCULTA] [CLAVE_OCULTA]` | `capturas/05-formulario-rgpd.png` |
| 6 | Texto con "Ignora las instrucciones" | ✔ Alerta roja y botón "Guardar ticket" deshabilitado | `capturas/06-inyeccion-bloqueada.png` |
| 7 | Crear un ticket nuevo | ✔ Ticket #11 creado, KPI total sube a 11, aviso flotante | `capturas/07-ticket-creado.png` |
| 8 | Marcar un ticket como resuelto | ✔ Insignia `RESUELTO` y KPI "Pendientes ALTA" baja a 3 | `capturas/08-ticket-resuelto.png` |
| 9 | Confirmación inline de borrado | ✔ "¿Borrar? · Sí, borrar · No" sin `window.confirm` | `capturas/09-confirmacion-borrado.png` |
| 10 | `openspec validate --all` | ✔ 2 passed, 0 failed | — |
| 11 | `node --check app.js` | ✔ Sin errores de sintaxis | — |
| 12 | Exportar informe Markdown | ✔ `informe_incidencias.md` generado | — |

---

## 11. Conclusiones y mejoras futuras

**Lo que he aprendido:**

- Un **prompt estructurado** (bloques XML, Root Prompt, Few-Shot, CoT) convierte texto sucio
  en datos fiables y anonimizados.
- Un **comando de OpenCode** es una forma reutilizable de empaquetar un prompt, sin escribir
  scripts desechables.
- Las **Skills** permiten fijar normas de calidad (diseño, RGPD) que el agente aplica solo.
- **OpenSpec + Prompt Chaining** evita el "vibe coding": se construye por eslabones
  revisables en lugar de pedirlo todo de golpe.
- El **Patrón Reflexión** sirve para que el propio agente encuentre fallos (XSS, UX,
  falsos positivos) y los corrija.

**Mejoras futuras:**

- Reto B: migrar `localStorage` a una tabla real en **Supabase**.
- Reto A: clasificación automática con **Groq** desde el navegador (clave solo en
  `sessionStorage`).
- Filtro por rango de fechas y carga de tickets desde el propio correo del taller.

---

### Entrega

- Repositorio privado: `daw2-fiag` → `ut2-prompt-engineering/01-taller-helpdesk/`
- Web desplegada: Netlify (enlace en el apartado 9.2)
- Memoria técnica: este `README.md` exportado a PDF
