import os
import google.generativeai as gai
from dotenv import load_dotenv



client = gai.Client(api_key=os.getenv('GOOGLE_API_KEY'))

def test():
 res = client.generate_content(
     model ='gemini-2.0-flash',
     config =gai.types.GenerateContentConfig(
         system_instruction = "You are a helpful assistant that translates English to Brazilian Portuguese."),
     contents='Translate the following sentence to Brazilian Portuguese: "Hello, how are you?"'
 )
 
 return res.text