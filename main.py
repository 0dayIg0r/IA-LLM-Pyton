from dotenv import load_dotenv

load_dotenv()


# from providers import anthropic
# from providers import openai
from providers import xai  
# from providers import google


# print(anthropic.test())
print(xai.test())

