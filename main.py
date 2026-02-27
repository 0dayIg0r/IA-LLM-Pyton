import os
from dotenv import load_dotenv

load_dotenv()

import openai
import anthropic
import xai_sdk
# import google.generativeai as gai
import groq
import ollama 


openai_client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
anthropic_client = anthropic.Anthropic(api_key=os.getenv('ANTROPHIC_API_KEY'))
# xai_ia = xai_sdk.client(api_key=os.getenv('XAI_API_KEY'))
# gai.configure(api_key='GOOGLE_API_KEY')
groq_client = groq.Groq(api_key=os.getenv('GROQ_API_KEY'))


response = openai_client.responses.create(
    model="gpt-4o-mini",
    reasoning={'effort': 'low'},
    input=[
        {"role": "system", "content": "Seja direto e conciso. Responda apenas o necessário."},
        {"role": "user", "content": "Qual é a capital da França?"}
    ],
)


print("Resposta do OpenAI:", response.output_text)