import json
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

conversation_file = "data/conversations.json"

# Load existing conversation
if os.path.exists(conversation_file):
    with open(conversation_file, "r", encoding="utf-8") as file:
        conversation = json.load(file)
else:
    conversation = []

# Add user's new message
conversation.append({
    "role": "user",
    "content": message,
})

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}

data = {
    "model": "openrouter/free",
    "messages": conversation,
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

    # Add AI response to conversation
    conversation.append({
        "role": "assistant",
        "content": ai_response,
    })

    # Save updated conversation
    os.makedirs("data", exist_ok=True)

    with open(conversation_file, "w", encoding="utf-8") as file:
        json.dump(conversation, file, indent=4, ensure_ascii=False)

except requests.exceptions.RequestException as error:
    print(f"\nError: API request failed: {error}")

except (KeyError, IndexError, TypeError, ValueError):
    print("\nError: Unexpected response received from the API.")