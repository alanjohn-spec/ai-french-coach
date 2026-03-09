Project: AI French Fluency Coach

Goal
Build an AI-powered French tutor that helps users reach conversational fluency.

Architecture
Frontend: Next.js (localhost:3000)
Backend: FastAPI (localhost:8000)

Core Stack
Next.js
FastAPI
OpenAI GPT
Railway deployment (planned)

Current Working Features
Backend running
Frontend running
Frontend ↔ Backend connection working
OpenAI GPT integration working

Working Endpoints

GET /
Health check

GET /hello
Test endpoint

POST /chat
GPT-powered French tutor response

Next Development Steps
1. Build chat interface in frontend
2. Connect frontend chat to /chat endpoint
3. Add conversation memory
4. Add voice input (Whisper)
5. Add voice output (TTS)
6. Deploy system to Railway
Current Status (Milestone 1)

Frontend
Next.js chat interface working

Backend
FastAPI running

AI
GPT integration working

Memory
Conversation history implemented
History limited to last 20 messages to control token usage

Architecture
Browser → NextJS → FastAPI → OpenAI
Milestone 2

Chat system fully functional
Session-based memory implemented
Token control implemented
Architecture stable

Next Goals
1. Move API URL to environment variables
2. Prepare backend for Railway deployment
3. Deploy backend
4. Deploy frontend
5. Add voice tutor