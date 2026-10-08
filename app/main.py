import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    print("Error: OPENROUTER_API_KEY is not set in the .env file.")
    exit()

message = input("You: ").strip()

if not message:
    print("Error: Message cannot be empty.")
    exit()

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

data = {
    "model": "openrouter/free",
    "messages": [
        {
            "role": "user",
            "content": message,
        }
    ],
}

try:
    response = requests.post(
        url,
        headers=headers,
        json=data,
        timeout=30,
    )

    response.raise_for_status()

    result = response.json()

    ai_response = result["choices"][0]["message"]["content"]

    print("\nAI:")
    print(ai_response)

except requests.exceptions.RequestException as error:
    print(f"\nError: API request failed: {error}")

except (KeyError, IndexError, TypeError, ValueError):
    print("\nError: Unexpected response received from the API.")