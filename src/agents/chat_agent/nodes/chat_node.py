import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from src.agents.chat_agent.states.chat_agent_state import ChatAgentState

load_dotenv()

def chat_node(state: ChatAgentState) -> ChatAgentState:
    model = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY")
    )

    ai_response = model.invoke(state["message"])

    state["response"] = ai_response.content
    return state
