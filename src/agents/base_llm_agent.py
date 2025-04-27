import os
import requests
import time

class BaseLLMAgent:
    def __init__(self, model: str, api_url: str, api_key_env: str):
        self.model = model
        self.url = api_url
        self.headers = {
            'Authorization': f"Bearer {os.getenv(api_key_env)}",
            'Content-Type': 'application/json'
        }

    def _call_llm(self, prompt: str, temperature=0.7, max_tokens=1024):
        messages = [
            {'role': 'system', 'content': 'Eres un asistente útil.'},
            {'role': 'user',   'content': prompt}
        ]
        payload = {
            'model': self.model,
            'messages': messages,
            'temperature': temperature,
            'max_tokens': max_tokens
        }
        start = time.time()
        print("DEBUG → Llamando a:", self.url)
        resp = requests.post(self.url, json=payload, headers=self.headers)
        resp.raise_for_status()
        data = resp.json()
        latency = time.time() - start
        choice = data['choices'][0]['message']
        return {
            'content': choice.get('content', ''),
            'usage': data.get('usage', {}),
            'latency': latency
        }