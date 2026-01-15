from src.agents.chat_agent.graph import chat_graph
from src.agents.chat_agent.states.chat_agent_state import ChatAgentState

def handle_chat(message: str) -> str:
    state: ChatAgentState = {
        "message": message,
        "response": ""
    }

    result = chat_graph.invoke(state)
    return result["response"]
