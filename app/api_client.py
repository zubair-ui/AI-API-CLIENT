import requests

from config import API_KEY, API_URL, MODEL


def get_ai_response(messages):
    if not API_KEY:
        raise ValueError("OPENROUTER_API_KEY is not set in the .env file.")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": MODEL,
        "messages": messages,
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json=data,
        timeout=30,
    )

    response.raise_for_status()

    result = response.json()

    return result["choices"][0]["message"]["content"]