import os
from fastapi import FastAPI
from openai import OpenAI

app = FastAPI()
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/api/chat")
def chat_endpoint():
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": "Give me a short welcome message."},
        ]
    )
    return {"response": response.choices[0].message.content}

@app.get("/api/health")
def health_check():
    return {"status": "ok"}