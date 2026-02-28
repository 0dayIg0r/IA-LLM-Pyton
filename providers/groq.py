import os

import groq


groq_client = groq.Groq(api_key=os.getenv('GROQ_API_KEY'))


def test():
    response = groq_client.chat.completions.create(
        model='groq-2',
        messages=[
            {
                'role': 'user',
                'content': 'What is the capital of France?'
            }
        ]
    )
    return response.choices[0].message.content