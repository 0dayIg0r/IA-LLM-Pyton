import os
import xai_sdk
from dotenv import load_dotenv

xai_ia = xai_sdk.client(api_key=os.getenv('XAI_API_KEY'))
