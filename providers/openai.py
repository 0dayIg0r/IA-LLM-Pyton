import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def test():
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "system", "content": "Seja direto e conciso. Responda apenas o necessário."},
            {"role": "user", "content": "Qual é a capital da França?"}
        ],
    )
    return response.output_text 

print(test())