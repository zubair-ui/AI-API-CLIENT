from datetime import datetime


def create_conversation():
    return {
        "created_at": datetime.now().isoformat(),
        "messages": [],
    }


def add_message(conversation, role, content):
    conversation["messages"].append({
        "role": role,
        "content": content,
    })


def get_messages(conversation):
    return conversation["messages"]


def is_empty(conversation):
    return len(conversation["messages"]) == 0