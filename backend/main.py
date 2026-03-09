import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

sessions = {}

class ChatRequest(BaseModel):
    message: str


@app.get("/")
def health():
    return {"status": "AI French Coach backend running"}


@app.get("/hello")
def hello():
    return {"message": "Bonjour from backend"}


@app.post("/chat")
def chat(req: ChatRequest):

    session_id = "default"

    if session_id not in sessions:
        sessions[session_id] = []

    sessions[session_id].append({
        "role": "user",
        "content": req.message
    })

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a friendly French tutor helping someone practice speaking French."
            }
        ] + sessions[session_id]
    )

    reply = completion.choices[0].message.content

    sessions[session_id].append({
        "role": "assistant",
        "content": reply
    })

    if len(sessions[session_id]) > 20:
        sessions[session_id].pop(0)

    return {"reply": reply}