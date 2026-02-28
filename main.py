from dotenv import load_dotenv

load_dotenv()


# from providers import anthropic
from providers import openai
# from providers import xai  
# from providers import google


# print(anthropic.test())

# book = openai.book_finder('O livro menciona 42 como o sentido da vida')
# if book:
#     print(f"Titulo: {book.title}, Autor: {book.author}")

# else:
#     print("Nenhum livro encontrado.")

print(openai.image_reader('https://recreio.com.br/wp-content/uploads/2024/05/goku_capa-1.jpg'))