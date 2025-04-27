from .base_llm_agent import BaseLLMAgent

class DecompositionAgent(BaseLLMAgent):
    def __init__(self):
        super().__init__(
            model='llama3-70b-8192',
            api_url='https://api.groq.com/openai/v1/chat/completions',
            api_key_env='GROQ_API_KEY'
        )


    def run(self, question: str):
        prompt = (
            'Descompón la siguiente pregunta compleja en sub-preguntas más simples:\n'
            f"{question}\n\n"
            'Devuelve solo una lista numerada.'
        )
        out = self._call_llm(prompt, temperature=0.0, max_tokens=500)
        raw = out['content']
        subqs = []
        for line in raw.splitlines():
            line = line.strip()
            if line and (line[0].isdigit() or line.startswith('-')):
                clean = line.lstrip('-0123456789. ').strip()
                subqs.append(clean)
        usage = out['usage'].get('total_tokens', 0)
        return subqs, usage