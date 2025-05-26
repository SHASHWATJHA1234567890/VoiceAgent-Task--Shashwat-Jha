import requests
import os
from dotenv import load_dotenv



def get_response(prompt: str, user_input: str, key: str, model="mistralai/mistral-7b-instruct:free"):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }
    messages = (
        [{"role": "system", "content": prompt}] if prompt else []
    ) + [{"role": "user", "content": user_input}]

    payload={
        "model": model,

        "messages": messages
    }

    response= requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']