from config import GROQ_API_KEY, GROQ_MODEL, GROQ_ENDPOINT
import requests

def send_AI_prompt(prompt):

    #request body
    data = {
        "model": GROQ_MODEL,
        "messages": [
            
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    headers = {'Authorization': f'Bearer {GROQ_API_KEY}'}
    response = requests.post(GROQ_ENDPOINT, headers=headers, json=data)

    response_json = response.json()

    aiResponse = response_json['choices'][0]['message']['content']

    return aiResponse