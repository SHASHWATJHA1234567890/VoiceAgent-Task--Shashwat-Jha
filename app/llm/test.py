import requests
import os
from dotenv import dotenv_values
from pathlib import Path

env_path = Path(__file__).resolve().parents[2] / ".env"
print("ENV PATH:", env_path)

# Directly load and print contents
env_vars = dotenv_values(env_path)

key = env_vars["OPENROUTER_API_KEY"]
print("key loaded:", key)

headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}
data = {
    "model": "mistralai/mistral-7b-instruct:free",
    "messages": [
        {"role": "user", "content": "Hello"}
    ]
}

response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
print(response.status_code)
print(response.text)
