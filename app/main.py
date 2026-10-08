from api_client import get_ai_response
from storage import load_conversation, save_conversation

message = input("You: ").strip()

if not message:
    print("Error: Message cannot be empty.")
    exit()

conversation = load_conversation()

conversation.append({
    "role": "user",
    "content": message,
})

try:
    ai_response = get_ai_response(conversation)

    print("\nAI:")
    print(ai_response)

    conversation.append({
        "role": "assistant",
        "content": ai_response,
    })

    save_conversation(conversation)

except ValueError as error:
    print(f"\nError: {error}")

except Exception as error:
    print(f"\nError: API request failed: {error}")