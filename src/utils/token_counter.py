import tiktoken

class TokenCounter:
    def __init__(self, encoding_name="cl100k_base"):
        self.enc = tiktoken.get_encoding(encoding_name)

    def count(self, text: str) -> int:
        if not isinstance(text, str):
            text = str(text)
        tokens = self.enc.encode(text)
        return len(tokens)
