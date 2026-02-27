import os
from dotenv import load_dotenv

from xai_sdk import Client
from xai_sdk.chat import system, user

load_dotenv()

xai_client = Client(api_key=os.getenv("XAI_API_KEY"))

def test():
    chat = xai_client.chat.create(model="grok-3")  # ou outro grok-*
    chat.append(system("Seja direto e conciso. Responda apenas o necessário."))
    chat.append(user("Qual é a capital da França?"))

    response = chat.sample()
    return response.content