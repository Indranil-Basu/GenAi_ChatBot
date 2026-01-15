import streamlit as st
import requests

st.set_page_config(page_title="Groq Chatbot", layout="centered")

st.title("🤖 Indranil Chatbot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for role, msg in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(msg)

# Input box (ENTER key triggers send)
user_input = st.chat_input("Type your message and press Enter")

if user_input:
    # Show user message
    st.session_state.messages.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call FastAPI backend
    response = requests.post(
        "http://localhost:8000/chat/",
        json={"message": user_input}
    )

    if response.status_code == 200:
        ai_reply = response.json()["response"]
    else:
        ai_reply = "❌ Server error"

    # Show AI message
    st.session_state.messages.append(("assistant", ai_reply))
    with st.chat_message("assistant"):
        st.markdown(ai_reply)
