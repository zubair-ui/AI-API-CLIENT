from api_client import get_ai_response
from storage import load_conversation, save_conversation


def main():
    conversation = load_conversation()

    print("AI API Client")
    print("Type 'exit' to quit.\n")

    while True:
        message = input("You: ").strip()

        if message.lower() == "exit":
            print("Goodbye!")
            break

        if not message:
            print("Error: Message cannot be empty.\n")
            continue

        conversation.append({
            "role": "user",
            "content": message,
        })

        try:
            ai_response = get_ai_response(conversation)

            print("\nAI:")
            print(ai_response)
            print()

            conversation.append({
                "role": "assistant",
                "content": ai_response,
            })

            save_conversation(conversation)

        except ValueError as error:
            print(f"\nError: {error}\n")

        except Exception as error:
            print(f"\nError: API request failed: {error}\n")


if __name__ == "__main__":
    main()