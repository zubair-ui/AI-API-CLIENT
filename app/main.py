import requests

from api_client import get_ai_response
from conversation import add_message, create_conversation, get_messages
from storage import load_conversation, save_conversation


def display_history(conversation):
    messages = get_messages(conversation)

    if not messages:
        print("\nNo conversation history.\n")
        return

    print("\n--- Conversation History ---")

    for message in messages:
        role = message["role"].capitalize()
        content = message["content"]

        print(f"\n{role}:")
        print(content)

    print("\n-----------------------------\n")


def main():
    conversation = load_conversation()

    print("AI API Client")
    print("Commands: /new | /history | /exit\n")

    while True:
        message = input("You: ").strip()

        if message.lower() == "/exit":
            print("Goodbye!")
            break

        if message.lower() == "/new":
            conversation = create_conversation()
            save_conversation(conversation)
            print("\nStarted a new conversation.\n")
            continue

        if message.lower() == "/history":
            display_history(conversation)
            continue

        if not message:
            print("Error: Message cannot be empty.\n")
            continue

        add_message(conversation, "user", message)

        try:
            ai_response = get_ai_response(get_messages(conversation))

            print("\nAI:")
            print(ai_response)
            print()

            add_message(conversation, "assistant", ai_response)
            save_conversation(conversation)

        except ValueError as error:
            print(f"\nError: {error}\n")

        except requests.exceptions.RequestException as error:
            print(f"\nError: API request failed: {error}\n")


if __name__ == "__main__":
    main()