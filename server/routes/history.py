from fastapi import APIRouter, HTTPException
from server.services.memory import get_recent_memories

router = APIRouter()


@router.get("/history")
async def history(user_id: str | None = None):  # pragma: no cover
    if not user_id:
        raise HTTPException(status_code=400, detail="Missing 'user_id'")
    mems = get_recent_memories(user_id, limit=10)
    return {"history": mems}
