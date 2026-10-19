# Parte 3: Ajuste de Parámetros (Experimentos Prácticos)

Esta carpeta contiene los ejercicios prácticos de la Parte 3 del curso, enfocados en
controlar el comportamiento de un modelo de lenguaje mediante los parámetros de
muestreo y generación de la API (Groq / OpenAI).

## Estructura

| Archivo | Ejercicio | Parámetro principal |
|---------|-----------|---------------------|
| `ejercicio_01_temperature_top_p.py` | Ejercicio Práctico 1 | `temperature` y `top_p` (creatividad) |
| `ejercicio_02_max_completion_tokens.py` | Ejercicio Práctico 2 | `max_completion_tokens` (longitud) |
| `ejercicio_03_stop.py` | Ejercicio Práctico 3 | `stop` (secuencia de parada) |
| `ejercicio_04_stream.py` | Ejercicio Práctico 4 | `stream=True` (tiempo real) |
| `ejercicio_05_reasoning_effort.py` | Ejercicio Práctico 5 (opcional) | `reasoning_effort` (razonamiento) |
| `reto_integrador.py` | Reto Integrador Final (opcional, subir nota) | Combinación de varios parámetros |

## Requisitos

- Python 3.10+
- Variables de entorno en `D:\Users\daw2-13\Desktop\daw2-fiag\.env`:
  ```
  GROQ_API_KEY=tu_clave_aqui
  ```
- Dependencias instaladas (ya están en el entorno `.venv`):
  ```
  openai
  python-dotenv
  ```

## Cómo ejecutar

Desde la raíz del proyecto (`daw2-fiag`), activando el entorno virtual:

```powershell
.\.venv\Scripts\Activate.ps1
cd parte3-ajuste-parametros
python ejercicio_01_temperature_top_p.py
```

Repite el comando con el nombre de cada archivo para ejecutar los demás ejercicios.

## Notas sobre el modelo usado

Todos los scripts usan el modelo `qwen/qwen3.8-27b` a través de Groq, el mismo que el
`main.py` del proyecto. Algunos parámetros (como `reasoning_effort`) solo tienen efecto
en modelos de razonamiento (Qwen3) y no se combinan con `temperature` en ciertas
configuraciones del proveedor; cada ejercicio lo indica cuando aplica.
