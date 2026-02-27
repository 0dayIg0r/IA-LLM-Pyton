import os
import ollama
from dotenv import load_dotenv

def test():
    res = ollama.generate(
        model='llama3',
        system='You are a helpful assistant that translates English to Brazilian Portuguese.',
        prompt='Translate the following sentence to Brazilian Portuguese: "Hello, how are you?"'
    )
    
    return res['response']['content']
    
    


def ollamaChat():
    res = ollama.chat(
        model='llama3',
        system='You are a helpful assistant that translates English to Brazilian Portuguese.',
        messages=[
            {'role': 'user', 'content': 'Translate the following sentence to Brazilian Portuguese: "Hello, how are you?"'}
        ]
    )
    
    return res['response']