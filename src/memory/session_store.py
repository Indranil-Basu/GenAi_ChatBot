import json
import os

MEMORY_FILE = "chat_memory.json"
sessions = {}

def load_memory():
    global sessions
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            sessions = json.load(f)

def save_memory():
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(sessions, f, indent=2)

def get_session(session_id):
    return sessions.get(session_id, [])

def save_session(session_id, messages):
    sessions[session_id] = messages
    save_memory()
