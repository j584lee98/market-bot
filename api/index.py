import os
from fastapi import FastAPI, APIRouter, Body, HTTPException
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter(prefix="/api")

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest = Body(...)):
    """Accept a user message and return model completion."""
    user_message = payload.message.strip()
    if not user_message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    try:
        completion = openai.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": user_message}],
        )
        content = completion.choices[0].message.content if completion.choices else ""
        return ChatResponse(response=content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model error: {e}")

@router.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(router)