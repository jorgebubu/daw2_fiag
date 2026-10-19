"""Ejercicio Práctico 4 - Respuestas en Tiempo Real (stream=True).

Objetivo:
  Entender cómo `stream=True` permite recibir el contenido del modelo a medida
  que se genera (token por token), en lugar de esperar la respuesta completa.

Parámetro:
  - stream (bool): si es True, la API devuelve un flujo de fragmentos (chunks)
    que se pueden ir procesando y mostrando en tiempo real.

En este ejercicio se pide un cuento corto y se imprime cada fragmento a medida
que llega, sin saltos de línea innecesarios, simulando un efecto de escritura.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

MODELO = "qwen/qwen3.8-27b"

PROMPT = (
    "Escribe un cuento corto de fantasía (máximo 80 palabras) sobre un dragón "
    "que prefiere leer libros a quemar aldeas."
)


def main():
    print("=" * 70)
    print("EJERCICIO 4 - stream=True (respuesta en tiempo real)")
    print("=" * 70)
    print(f"Prompt: {PROMPT}\n")
    print("Respuesta del modelo (streaming):")
    print("-" * 70)

    response = client.chat.completions.create(
        model=MODELO,
        messages=[
            {"role": "system", "content": "Eres un narrador de cuentos."},
            {"role": "user", "content": PROMPT},
        ],
        stream=True,
    )

    try:
        for chunk in response:
            delta = chunk.choices[0].delta
            contenido = delta.content
            if contenido:
                print(contenido, end="", flush=True)
    except Exception as e:
        print(f"\n[ERROR durante el streaming] {e}")

    print()  # salto de línea final
    print("-" * 70)
    print("Fin del streaming. Con stream=True el usuario ve el texto aparecer "
          "progresivamente, lo cual mejora la percepción de velocidad.")

    print()
    print("Fin del ejercicio 4.")


if __name__ == "__main__":
    main()
