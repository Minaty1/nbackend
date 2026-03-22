from fastapi import APIRouter, HTTPException
from server.services.memory import add_memory, get_recent_memories
from server.services.groq import groq_client

router = APIRouter()


@router.post("/chat")
async def chat(payload: dict):  # pragma: no cover - small integration path
    user_id = payload.get("user_id")
    text = payload.get("text")
    if not user_id or not text:
        raise HTTPException(status_code=400, detail="Missing 'user_id' or 'text'")

    # Build minimal memory context (oldest first)
    mems = get_recent_memories(user_id, limit=10)
    memory_context = "\n".join([f"{m['role']}: {m['content']}" for m in mems])

    prompt = f"{memory_context}\nUser: {text}\nAI:"
    ai_text = await groq_client.generate(prompt, memory=memory_context)

    # Persist memory for future context
    add_memory(user_id, "user", text)
    add_memory(user_id, "ai", ai_text)

    updated = get_recent_memories(user_id, limit=10)
    return {"response": ai_text, "history": updated}
