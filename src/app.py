from flask import Flask, render_template, request
import os
import requests
from utils.token_counter import TokenCounter
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Configurar API de Groq
API_URL = "https://api.groq.com/openai/v1/chat/completions"
API_KEY = os.getenv("GROQ_API_KEY")
MODEL = "llama3-70b-8192"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Inicializar contador de tokens
tc = TokenCounter()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')

    # Armar prompt
    prompt = f"{user_text}\nRazona paso por paso, genera resultados parciales y luego suma para llegar al resultado total."

    # Contar tokens entrada
    tokens_entrada = tc.count(prompt)
    print(f"Tokens entrada: {tokens_entrada}")

    # Armar payload
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Eres un asistente útil."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 2048
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=data)
        response.raise_for_status()

        result = response.json()
        content = result['choices'][0]['message']['content']

        return content

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True, port=5050)
