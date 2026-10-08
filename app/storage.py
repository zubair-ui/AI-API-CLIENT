import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CONVERSATION_FILE = DATA_DIR / "conversations.json"


def load_conversation():
    if not CONVERSATION_FILE.exists():
        return []

    try:
        with open(CONVERSATION_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_conversation(conversation):
    DATA_DIR.mkdir(exist_ok=True)

    with open(CONVERSATION_FILE, "w", encoding="utf-8") as file:
        json.dump(
            conversation,
            file,
            indent=4,
            ensure_ascii=False,
        )