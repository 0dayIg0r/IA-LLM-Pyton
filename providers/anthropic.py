
import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

anthropic_client = anthropic.Anthropic(api_key=os.getenv('ANTROPHIC_API_KEY'))

def test():
    response = anthropic_client.messages.create(
        model="claude-2",
        max_tokens=1024,
        system="Seja direto e conciso. Responda apenas o necessário.",
        messages=[
            {"role": "user", "content": "Qual é a capital da França?"}
        ]
    )
    return response.output_text