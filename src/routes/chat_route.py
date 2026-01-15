from fastapi import APIRouter
from pydantic import BaseModel
from src.handlers.chat_handler import handle_chat

router = APIRouter(prefix="/chat", tags=["Chat"])

class ChatRequest(BaseModel):
    message: str

@router.post("/")
def chat_endpoint(req: ChatRequest):
    response = handle_chat(req.message)
    return {"response": response}
