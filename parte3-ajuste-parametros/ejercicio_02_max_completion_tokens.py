"""Ejercicio Práctico 2 - Limitar la Longitud de Salida (max_completion_tokens).

Objetivo:
  Entender cómo `max_completion_tokens` corta la respuesta cuando se alcanza el
  número máximo de tokens generados.

Parámetro:
  - max_completion_tokens (int > 0): número máximo de tokens que el modelo puede
    generar en la respuesta. Si el modelo se queda sin espacio, la respuesta se
    corta abruptamente y `finish_reason` vale "length".

En este ejercicio se pide un artículo largo y se genera dos veces:
  1. Sin límite efectivo (valor alto) -> respuesta completa.
  2. Con un límite bajo -> respuesta truncada.
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
    "Escribe un artículo breve (aproximadamente 200 palabras) sobre los "
    "beneficios de dormir bien para la salud. Usa un tono informativo y "
    "divide el texto en párrafos."
)


def generar(max_tokens: int | None) -> str:
    response = client.chat.completions.create(
        model=MODELO,
        messages=[
            {"role": "system", "content": "Eres un redactor saludable."},
            {"role": "user", "content": PROMPT},
        ],
        max_completion_tokens=max_tokens if max_tokens is not None else 2000,
    )
    choice = response.choices[0]
    return choice.message.content, choice.finish_reason


def main():
    print("=" * 70)
    print("EJERCICIO 2 - max_completion_tokens (longitud de salida)")
    print("=" * 70)
    print(f"Prompt: {PROMPT}\n")

    # 1. Sin límite restrictivo (valor alto)
    print("-" * 70)
    print("[CASO A] max_completion_tokens=2000 (sin límite efectivo)")
    print("-" * 70)
    texto_a, razon_a = generar(2000)
    print(texto_a)
    print(f"\n[finish_reason: {razon_a}]  <- 'stop' significa que terminó naturalmente.")
    print()

    # 2. Con límite bajo para forzar el corte
    print("-" * 70)
    print("[CASO B] max_completion_tokens=40 (límite bajo -> respuesta truncada)")
    print("-" * 70)
    texto_b, razon_b = generar(40)
    print(texto_b)
    print(f"\n[finish_reason: {razon_b}]  <- 'length' indica que se cortó por el límite.")

    print()
    print("Fin del ejercicio 2. Con max_completion_tokens controlas cuánto puede escribir el modelo.")


if __name__ == "__main__":
    main()
