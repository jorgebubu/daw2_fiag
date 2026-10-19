import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Instanciar cliente especificando la URL de Groq
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

response = client.chat.completions.create(
    model="qwen/qwen3.8-27b",
    messages=[
        {"role": "system", "content": "Eres un asistente técnico conciso."},
        {"role": "user", "content": "Hola, ¿funciona la API?"}
    ]
)

print(response.choices[0].message.content)