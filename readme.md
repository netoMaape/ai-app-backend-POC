# 🚀 Generic AI POC Backend

A lightning-fast, production-ready FastAPI skeleton designed to spin up AI Proof-of-Concepts (POCs) in minutes, not days.

Stop wasting time writing login routes and database models. Clone this repository, paste your app idea into an AI, and start building the core logic of your application immediately.

## ✨ Features

- **FastAPI:** Lightning-fast API with auto-generated Swagger documentation.
- **SQLite:** Zero-configuration database that just works.
- **JWT Auth:** Secure login and registration using Bcrypt and JWT out of the box.
- **Auto-Seeding:** Drops, recreates, and seeds dummy users on startup. Toggleable via `.env`.
- **Provider-Agnostic AI:** A built-in factory pattern to switch seamlessly between Mock AI, OpenAI, or Gemini.
- **Protected Routes:** Pre-built `/me` and `/ai/summarize` endpoints demonstrating how to protect data.
- **AI Architect Context:** Includes a `context.md` file designed to turn DeepSeek (or any LLM) into a Principal Engineer that plans and builds your app step by step.

## 🛠️ Quick Start

### 1. Clone the Repository

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/netoMaape/generic-ai-poc-backend.git
cd generic-ai-poc-backend
```

### 2. Create and Activate a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add the following:

```env
SECRET_KEY=super_secret_key_change_me
RESET_DB_ON_STARTUP=True
AI_PROVIDER=mock
AI_MODEL_API_KEY=your_openai_key_here
```

### 5. Run the Server

```bash
uvicorn main:app --reload
```

### 6. Open the API Documentation

Navigate to the following URL in your browser:

[http://127.0.0.1:8000/] or (http://127.0.0.1:8000/docs)

**Note:** The database automatically seeds two test users when the server starts:

- **User:** `test@example.com` / **Password:** `password123`
- **User:** `admin@example.com` / **Password:** `admin123`

---

## 🧠 How to Build Your App (The AI Workflow)

This repository includes a `context.md` file that helps turn an AI assistant like DeepSeek, Claude, or ChatGPT into a **Principal Engineering Consultant**.

Instead of simply asking the AI to "build an app" (which can result in messy, broken code), this workflow requires the AI to plan first.

### The Workflow

1. **Open Your AI Chat:** Start a new conversation with DeepSeek or your preferred AI assistant.
2. **Paste the Context:** Drag the `context.md` file from this repository into the chat.
3. **Describe Your Idea:** In the chat where you drpoped the file, type a brief description of the application you want to build.
4. **Get Interviewed:** The AI will ask clarifying questions about your application's data and business logic. Answer these questions.
5. **Review the Plan:** The AI will generate a complete backend architecture plan.
6. **Copy and Paste the Code:** The AI will guide you through creating database models, Pydantic schemas, AI services, and API routes. Copy the code blocks it provides into the corresponding files in this repository.

---

**Happy building! 🚀**