"""Ejercicio Práctico 3 - Secuencia de Parada Personalizada (stop).

Objetivo:
  Entender cómo `stop` detiene la generación tan pronto como el modelo produce
  una secuencia de texto específica.

Parámetro:
  - stop (str | list[str]): una o más secuencias que, al aparecer en la
    generación, detienen la respuesta inmediatamente. Cuando se activa, el
    `finish_reason` vale "stop".

En este ejercicio se pide al modelo que cuente del 1 al 20 y se le indica que
se detenga al llegar al número 10, usando stop=["10"].
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
    "Cuenta del 1 al 20, escribiendo un número en cada línea. "
    "Cuando llegues al número 10, detente y escribe 'FIN'."
)


def generar(stop_secuencias) -> str:
    response = client.chat.completions.create(
        model=MODELO,
        messages=[
            {"role": "system", "content": "Eres un asistente que sigue instrucciones al pie de la letra."},
            {"role": "user", "content": PROMPT},
        ],
        stop=stop_secuencias,
    )
    choice = response.choices[0]
    return choice.message.content, choice.finish_reason


def main():
    print("=" * 70)
    print("EJERCICIO 3 - stop (secuencia de parada personalizada)")
    print("=" * 70)
    print(f"Prompt: {PROMPT}\n")

    print("-" * 70)
    print("[CASO] stop=['10'] -> se detiene al generar el número 10")
    print("-" * 70)
    try:
        texto, razon = generar(["10"])
        print(texto)
        print(f"\n[finish_reason: {razon}]  <- 'stop' porque se encontró la secuencia '10'.")
    except Exception as e:
        print(f"[ERROR] {e}")

    print()
    print("Fin del ejercicio 3. Usa stop para cortar respuestas en palabras clave, "
          "etiquetas (por ejemplo '<|end|>') o cuando se cumpla una condición de corte.")


if __name__ == "__main__":
    main()
