import requests

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": "Bearer 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",  # Replace directly here
    "Content-Type": "application/json"
}
data = {
    "model": "mistralai/mistral-7b-instruct:free",
    "messages": [
        {"role": "user", "content": "Hello"}
    ]
}

response = requests.post(url, headers=headers, json=data)
print(response.status_code)
print(response.text)
