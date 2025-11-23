import os
from fastapi import FastAPI, APIRouter, Body, HTTPException
from pydantic import BaseModel

from utils.model import get_chat_completion

app = FastAPI()

router = APIRouter(prefix="/api")

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(payload: ChatRequest = Body(...)):
    """Accept a user message and return model completion via utils.model."""
    user_message = payload.message.strip()
    if not user_message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    try:
        content = await get_chat_completion(user_message)
        return ChatResponse(response=content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model error: {e}")

@router.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(router)