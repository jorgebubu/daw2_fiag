"""Ejercicio Práctico 5 (opcional) - Controlar el Nivel de Razonamiento (reasoning_effort).

Objetivo:
  Entender cómo `reasoning_effort` ajusta cuánto "piensa" el modelo antes de
  responder. Solo tiene efecto en modelos de razonamiento (como Qwen3).

Parámetro:
  - reasoning_effort ("low" | "medium" | "high"):
      * "low": razonamiento rápido, menos tokens internos, respuestas directas.
      * "medium": equilibrio entre velocidad y profundidad.
      * "high": razonamiento más profundo, útil para problemas complejos.

Nota: en muchos proveedores, `reasoning_effort` no se combina con `temperature`.
En este ejercicio se omite `temperature` y se prueba con los tres niveles en una
pregunta que requiere un pequeño cálculo razonado.
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
    "Tengo 3 manzanas. Como 1 manzana y luego compro el doble de manzanas de "
    "las que me quedan. ¿Cuántas manzanas tengo al final? Explica el cálculo paso a paso."
)


def generar(effort: str) -> str:
    response = client.chat.completions.create(
        model=MODELO,
        messages=[
            {"role": "system", "content": "Eres un asistente lógico y preciso."},
            {"role": "user", "content": PROMPT},
        ],
        reasoning_effort=effort,
    )
    return response.choices[0].message.content


def main():
    print("=" * 70)
    print("EJERCICIO 5 (opcional) - reasoning_effort (nivel de razonamiento)")
    print("=" * 70)
    print(f"Prompt: {PROMPT}\n")

    niveles = ["low", "medium", "high"]

    for esfuerzo in niveles:
        print("-" * 70)
        print(f"[reasoning_effort = {esfuerzo}]")
        print("-" * 70)
        try:
            texto = generar(esfuerzo)
            print(texto)
        except Exception as e:
            print(f"[ERROR] {e}")
            print("(Nota: si el proveedor no soporta reasoning_effort con este modelo, el error es esperado.)")
        print()

    print("Fin del ejercicio 5. Usa un esfuerzo bajo para tareas sencillas y alto "
          "para problemas que requieran varios pasos de razonamiento.")


if __name__ == "__main__":
    main()
