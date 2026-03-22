Jarvis Android APK MVP

Overview
- MVP backend in Python FastAPI with SQLite storage for memory and a Groq wrapper.
- Expo/React Native frontend scaffold for Android.
- End-to-end path: Voice → Text → AI → Text → Voice (offline-first by default).
- Render deployment: Added render.yaml and requirements.txt for hosting on render.com.
- MVP backend in Python FastAPI with SQLite storage for memory and a Groq wrapper.
- Expo/React Native frontend scaffold for Android.
- End-to-end path: Voice → Text → AI → Text → Voice (offline-first by default).

How to run locally
- Backend
 1) Ensure Python 3.8+ is installed.
 2) Create a virtualenv and install dependencies (fastapi, uvicorn).
 3) Run the server: uvicorn server.main:app --reload --port 8000
 4) The first startup will bootstrap the SQLite DB in server/jarvis.db.
- Frontend
 1) Install Node.js and npm/yarn.
 2) cd app && npm install
 3) Start Expo: npm run start
 4) Use an Android emulator; if needed, adjust API_BASE to your host IP

Notes
- Some endpoints are intentionally simple for MVP; wire in real authentication and security later.
- The Groq API is wired via env vars; if not configured, the backend will echo the prompt as a fallback.
