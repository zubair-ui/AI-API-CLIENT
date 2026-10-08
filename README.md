# AI API Client

A Python-based command-line AI client that communicates with an LLM through the OpenRouter API.

The project was built as part of a **GenAI / AI Engineer learning roadmap**, with a focus on understanding practical software engineering concepts such as HTTP APIs, JSON, environment variables, error handling, modular code, persistence, and Git/GitHub.

## Features

* 🤖 Interact with an AI model through OpenRouter
* 💬 Multi-message conversations
* 🧠 Conversation context is sent with each request
* 💾 Local conversation persistence using JSON
* 🆕 Start a new conversation with `/new`
* 📜 View conversation history with `/history`
* 🚪 Exit the application with `/exit`
* 🔐 API key stored securely in `.env`
* ⚠️ Basic API and response error handling
* 🧩 Modular Python project structure

## Project Structure

```text
ai-api-client/
│
├── app/
│   ├── main.py
│   ├── api_client.py
│   ├── conversation.py
│   ├── config.py
│   └── storage.py
│
├── data/
│   └── conversations.json
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* Requests
* python-dotenv
* OpenRouter API
* JSON
* Git & GitHub

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/zubair-ui/AI-API-CLIENT.git
cd ai-api-client
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create your `.env` file

Create a file named:

```text
.env
```

Add:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Get your own OpenRouter API key from the OpenRouter website.

The repository includes `.env.example` as a template.

### 5. Run the application

From the project root:

```bash
python app/main.py
```

## Usage

Once the application starts:

```text
AI API Client
Commands: /new | /history | /exit

You:
```

Enter a message and the AI will respond.

### Available Commands

| Command    | Description                      |
| ---------- | -------------------------------- |
| `/new`     | Start a new conversation         |
| `/history` | Display the current conversation |
| `/exit`    | Exit the application             |

## How It Works

The application follows this basic flow:

```text
User Input
    ↓
main.py
    ↓
conversation.py
    ↓
api_client.py
    ↓
OpenRouter API
    ↓
AI Response
    ↓
conversation.py
    ↓
storage.py
    ↓
conversations.json
```

Previous messages are included in subsequent API requests, allowing the model to maintain context within the conversation.

## Conversation Storage

Conversations are stored locally in:

```text
data/conversations.json
```

Example:

```json
{
    "created_at": "2026-10-08T14:30:00",
    "messages": [
        {
            "role": "user",
            "content": "What is Python?"
        },
        {
            "role": "assistant",
            "content": "Python is a high-level programming language..."
        }
    ]
}
```

## Security

The API key is loaded from the `.env` file using `python-dotenv`.

The `.env` file is excluded from Git using `.gitignore`.

```text
.env
```

Users should create their own API key rather than sharing or committing one.

## Learning Objectives

This project was built to practice:

* Python project structure
* Functions and modules
* HTTP requests
* REST APIs
* Authentication headers
* JSON serialization/deserialization
* Environment variables
* Exception handling
* File handling
* Data persistence
* Virtual environments
* Dependency management
* Git and GitHub

## Future Improvements

Possible future improvements include:

* Multiple saved conversations
* Conversation IDs
* Conversation titles
* Timestamps for individual messages
* Streaming responses
* Retry logic
* Logging
* Token/usage information
* Export conversations
* Better CLI interface
* Command-line arguments

## License

This project is intended for educational purposes.
