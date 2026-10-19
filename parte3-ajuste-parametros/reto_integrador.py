"""Reto Integrador Final (opcional, subir nota).

Objetivo:
  Aplicar en conjunto varios parámetros de ajuste para resolver una tarea
  real de forma controlada y justificar cada elección.

Tarea:
  Generar un RESUMEN EJECUTIVO corto y conciso de un texto largo sobre
  inteligencia artificial. El resumen debe ser profesional, directo y no
  exceder cierta longitud.

Parámetros combinados y justificación:
  - temperature=0.3: bajo, porque un resumen ejecutivo debe ser preciso y no creativo.
  - top_p=0.9: mantiene suficiente variedad sin alejarse del contenido fuente.
  - max_completion_tokens=180: obliga al resumen a ser breve y al punto.
  - stop=["\n\n"]: opcional, detiene al generar un párrafo vacío para evitar extensión extra.
  - stream=True: para mostrar el resumen en tiempo real (mejora UX).

Cada parámetro se comenta dentro del código para justificar su uso.
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

TEXTO_FUENTE = """
La inteligencia artificial (IA) ha dejado de ser una promesa futura para convertirse
en una herramienta presente en prácticamente todos los sectores productivos. Desde
la automatización de procesos administrativos hasta el diagnóstico asistido por
imagen en medicina, los modelos de lenguaje y los sistemas de visión por computadora
están transformando la forma en que las organizaciones operan.

No obstante, la adopción masiva de la IA conlleva retos importantes: sesgos en los
datos de entrenamiento, falta de transparencia en los modelos ("cajas negras"),
preocupaciones por la privacidad de los datos y el impacto en el empleo. Ante este
escenario, las empresas deben implementar marcos de gobernanza de IA que garanticen
uso ético, auditoría de resultados y supervisión humana continua.

En resumen, la IA ofrece oportunidades de eficiencia e innovación sin precedentes,
pero su éxito depende de una implementación responsable, ética y alineada con los
valores de cada organización.
""".strip()

PROMPT = (
    "A continuación tienes un texto sobre inteligencia artificial. Redacta un "
    "RESUMEN EJECUTIVO en español, de máximo 3 oraciones, tono profesional y "
    "directo. No incluyas introducciones como 'Aquí tienes el resumen':\n\n"
    f"{TEXTO_FUENTE}"
)


def main():
    print("=" * 70)
    print("RETO INTEGRADOR FINAL (opcional, subir nota)")
    print("=" * 70)
    print("Tarea: generar un resumen ejecutivo breve y profesional de un texto sobre IA.")
    print("-" * 70)
    print("Parámetros elegidos y por qué:")
    print("  - temperature=0.3   -> precisión, poca creatividad (resumen ejecutivo).")
    print("  - top_p=0.9         -> diversidad controlada, sin alejarse de la fuente.")
    print("  - max_completion_tokens=180 -> obliga a ser breve y al punto.")
    print("  - stop=['\\n\\n']         -> evita generar párrafos extra/vacíos.")
    print("  - stream=True       -> muestra el resumen en tiempo real.")
    print("-" * 70)
    print("Resumen ejecutivo (streaming):")
    print("-" * 70)

    response = client.chat.completions.create(
        model=MODELO,
        messages=[
            {"role": "system", "content": "Eres un redactor ejecutivo experto en síntesis de información."},
            {"role": "user", "content": PROMPT},
        ],
        temperature=0.3,
        top_p=0.9,
        max_completion_tokens=180,
        stop=["\n\n"],
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
    print("Fin del reto integrador. Cada parámetro fue usado con un propósito concreto.")

    print()
    print("Fin del reto integrador.")


if __name__ == "__main__":
    main()
