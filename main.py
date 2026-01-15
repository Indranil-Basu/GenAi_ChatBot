from fastapi import FastAPI
from src.routes.chat_route import router as chat_router

app = FastAPI(title="Groq Chat API")

app.include_router(chat_router)

@app.get("/")
def root():
    return {"status": "API is running"}
