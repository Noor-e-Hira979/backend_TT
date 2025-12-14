from fastapi import APIRouter
from pydantic import BaseModel
from app.utils.gemini_client import ask_gemini

router = APIRouter()

class ChatMessage(BaseModel):
    message: str

@router.post("/chatbot")
async def chatbot_api(data: ChatMessage):
    reply = ask_gemini(data.message)
    return {"reply": reply}
