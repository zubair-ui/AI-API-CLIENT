import json
import os


CONVERSATION_FILE = "data/conversations.json"


def load_conversation():
    if not os.path.exists(CONVERSATION_FILE):
        return []

    try:
        with open(CONVERSATION_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_conversation(conversation):
    os.makedirs("data", exist_ok=True)

    with open(CONVERSATION_FILE, "w", encoding="utf-8") as file:
        json.dump(
            conversation,
            file,
            indent=4,
            ensure_ascii=False,
        )