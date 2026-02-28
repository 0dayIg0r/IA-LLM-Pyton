import os
from openai import OpenAI

from pydantic import BaseModel

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



def image_reader(url):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "Você é um assistente de análise de imagens. Dada uma imagem, identifique os objetos presentes e extraia qualquer texto visível. Não forneça nenhuma informação adicional, apenas a descrição dos objetos e o texto extraído."},
                  {"role": "user", "content": [{"type": "image_url", "image_url": {"url": url}}, {"type": "text", "text": f"Analise esta imagem e identifique os objetos presentes e extraia qualquer texto visível."}]}]
    )
    return response.choices[0].message.content




class BookResponse(BaseModel):
    title: str
    author: str

def book_finder(search):
    res = client.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente de busca de livros. Dado um termo de pesquisa, retorne o título e o autor do livro mais relevante. Não retorne nenhuma mensagem adicional, apenas o título e o autor.   "},
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