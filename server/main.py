from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.db import init_db
from server.routes.chat import router as chat_router
from server.routes.history import router as history_router

app = FastAPI(title="Jarvis Backend MVP")

origins = ["*"]  # Allow all origins for MVP; tighten in production
app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"]
)


@app.on_event("startup")
async def on_startup():  # noqa: D401
    init_db()


app.include_router(chat_router, prefix="/api")
app.include_router(history_router, prefix="/api")
