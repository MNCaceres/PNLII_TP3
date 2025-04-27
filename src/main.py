import os
import time
import requests
from dotenv import load_dotenv
from utils.token_counter import TokenCounter

load_dotenv()

# Parámetros
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-70b-8192"  # 🔥 CAMBIADO

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def main():
    tc = TokenCounter()

    question = input('Ingresa tu pregunta: ')
    tokens_entrada = tc.count(question)
    print(f"Tokens entrada: {tokens_entrada}")

    system_msg = "Eres un asistente que descompone problemas complejos en subpreguntas detalladas para facilitar su resolución."
    user_msg = f"Descompón en sub-preguntas detalladas esta pregunta:\n{question}"
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ],
        "temperature": 0.0,
        "max_tokens": 1500   # 🔥 reducido
    }

    print("DEBUG → Llamando a:", URL)
    start = time.time()
    response = requests.post(URL, headers=HEADERS, json=payload)
    elapsed = time.time() - start

    response.raise_for_status()
    out = response.json()

    subquestions = out['choices'][0]['message']['content']
    tokens_razonamiento = tc.count(subquestions)

    print("\nSub-preguntas:\n", subquestions)

    # Paso 2: Resolver razonamiento
    reasoning_prompt = f"""Ahora resuelve paso por paso las siguientes subpreguntas:

{subquestions}

Utiliza los datos de la pregunta original para calcular todo. Luego entrega el resultado final.

Proporciona un razonamiento detallado y el resultado numérico final."""

    payload2 = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Eres un asistente experto en razonamiento lógico y matemático."},
            {"role": "user", "content": reasoning_prompt}
        ],
        "temperature": 0.0,
        "max_tokens": 2048  # 🔥 seguro
    }

    print("DEBUG → Llamando a:", URL)
    start2 = time.time()
    response2 = requests.post(URL, headers=HEADERS, json=payload2)
    elapsed2 = time.time() - start2

    response2.raise_for_status()
    out2 = response2.json()

    final_response = out2['choices'][0]['message']['content']
    tokens_salida = tc.count(final_response)

    print("\n--- Respuesta del LLM ---\n")
    print(final_response)

    print("\n--- Uso de tokens ---")
    print(f"Tokens razonamiento: {tokens_razonamiento}")
    print(f"Tokens salida      : {tokens_salida}")

if __name__ == "__main__":
    main()
