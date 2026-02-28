import os
from openai import OpenAI

from pydantic import BaseModel

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class BookResponse(BaseModel):
    title: str
    author: str

def book_finder(search):
    res = client.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente de busca de livros. Dado um termo de pesquisa, retorne o título e o autor do livro mais relevante."},
            {"role": "user", "content": f"Encontre um livro sobre '{search}'."}
        ],
        response_format=BookResponse
    )
    
    message = res.choices[0].message
    
    if message.parsed:
        return message.parsed
    else:
        return False
  
    


# def test():
#     response = client.responses.create(
#         model="gpt-4o-mini",
#         input=[
#             {"role": "system", "content": "Seja direto e conciso. Responda apenas o necessário."},
#             {"role": "user", "content": "Qual é a capital da França?"}
#         ],
#     )
#     return response.output_text 

# print(test())