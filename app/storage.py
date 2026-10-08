import json
from pathlib import Path

from conversation import create_conversation

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CONVERSATION_FILE = DATA_DIR / "conversations.json"


def load_conversation():
    if not CONVERSATION_FILE.exists():
        return create_conversation()

    try:
        with open(CONVERSATION_FILE, "r", encoding="utf-8") as file:
            conversation = json.load(file)

        if not isinstance(conversation, dict):
            return create_conversation()

        if "messages" not in conversation:
            return create_conversation()

        return conversation

    except (json.JSONDecodeError, OSError):
        return create_conversation()


def save_conversation(conversation):
    DATA_DIR.mkdir(exist_ok=True)

    with open(CONVERSATION_FILE, "w", encoding="utf-8") as file:
        json.dump(
            conversation,
            file,
            indent=4,
            ensure_ascii=False,
        )