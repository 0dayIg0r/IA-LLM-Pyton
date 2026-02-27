
import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

anthropic_client = anthropic.Anthropic(api_key=os.getenv('ANTROPHIC_API_KEY'))