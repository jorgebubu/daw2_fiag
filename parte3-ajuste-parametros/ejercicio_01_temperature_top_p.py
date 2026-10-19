"""Ejercicio Práctico 1 - Controlar la Creatividad (temperature y top_p).

Objetivo:
  Entender cómo `temperature` y `top_p` afectan la creatividad y aleatoriedad
  de las respuestas del modelo.

Parámetros:
  - temperature (0.0 - 2.0): controla la aleatoriedad.
      * Valores bajos (~0.2): respuestas deterministas, predecibles y conservadoras.
      * Valores altos (~0.9): respuestas más creativas, variadas y arriesgadas.
  - top_p (0.0 - 1.0): muestreo de núcleo (nucleus sampling).
      * Limita el conjunto de tokens considerados a los que acumulan una
        probabilidad `top_p`. Valores bajos reducen la diversidad.

En este ejercicio se genera el mismo cuento corto con 3 configuraciones distintas
para comparar el resultado.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# --- Configuración del cliente (igual que main.py del proyecto) ---
load_dotenv()
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

MODELO = "qwen/qwen3.8-27b"

PROMPT = (
    "Escribe un cuento muy corto de ciencia ficción, exactamente en 3 oraciones, "
    "sobre un robot que descubre la pintura por primera vez."
)


def generar(temperature: float, top_p: float, etiqueta: str) -> str:
    """Genera una respuesta con los parámetros indicados y devuelve el texto."""
    response = client.chat.completions.create(
        model=MODELO,
        messages=[
            {"role": "system", "content": "Eres un escritor creativo."},
            {"role": "user", "content": PROMPT},
        ],
        temperature=temperature,
        top_p=top_p,
    )
    return response.choices[0].message.content


def main():
    configuraciones = [
        ("Conservadora / determinista", 0.2, 0.9),
        ("Equilibrada", 0.7, 0.9),
        ("Creativa / arriesgada", 0.9, 0.9),
    ]

    print("=" * 70)
    print("EJERCICIO 1 - temperature y top_p")
    print("=" * 70)
    print(f"Prompt: {PROMPT}\n")

    for etiqueta, temperature, top_p in configuraciones:
        print("-" * 70)
        print(f"[{etiqueta}] temperature={temperature}, top_p={top_p}")
        print("-" * 70)
        try:
            texto = generar(temperature, top_p, etiqueta)
            print(texto)
        except Exception as e:
            print(f"[ERROR] {e}")
        print()  # línea en blanco entre resultados

    print("Fin del ejercicio 1. Observa cómo varía el estilo con cada configuración.")


if __name__ == "__main__":
    main()
