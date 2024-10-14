import os
from mistralai import Mistral

api_key = "tjyXiDGjeI1mw4ws5o0P2LSHcpXI75PZ"
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model = model,
    messages = [
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ]
)

print(chat_response.choices[0].message.content)