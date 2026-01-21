# 📚 GenAI ChatBot

A **full-stack AI chatbot** built with **FastAPI**, **Streamlit**, and **Groq LLM**, featuring:

✅ Real-time token streaming (ChatGPT-like typing)  
✅ Session-based memory persistence  
✅ PDF upload & chat  
✅ Modular tool-ready backend  
✅ Designed for production workflows

---

## 🚀 Features

### 🧠 Core Chat
- Interactive chat UI with Streamlit
- Backend streaming responses
- Support for conversational memory
- Session persistence across refreshes

### 📄 PDF Chat
- Upload a PDF document
- Backend processes text from PDF
- Ask questions about the PDF content

### 🔧 Backend Architecture
- FastAPI server with streaming (SSE)
- LangChain + Groq LLM integration
- JSON-based persistent memory
- Endpoint design suitable for adding tools (web search, weather, calculator)

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| LLM | Groq (via LangChain) |
| Memory | JSON persistence (chat_memory.json) |
| Dev / Env | Python 3.14, venv |
| Deployment Ready | Uvicorn, SSE support |

---

## 📦 Prerequisites

- Python 3.14+
- Git
- A Groq API key
- (Optional) LangSmith key for tracing

---

## 🛠️ Setup Locally

### 1️⃣ Clone Repo
```bash
git clone https://github.com/Indranil-Basu/GenAi_ChatBot.git
cd GenAi_ChatBot
