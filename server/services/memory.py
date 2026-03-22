from typing import List, Dict
from server.db import get_connection


def add_memory(user_id: str, role: str, content: str) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO memories (user_id, role, content) VALUES (?, ?, ?)",
        (user_id, role, content),
    )
    conn.commit()
    conn.close()


def get_recent_memories(user_id: str, limit: int = 10) -> List[Dict]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, role, content, created_at FROM memories WHERE user_id = ? ORDER BY created_at ASC LIMIT ?",
        (user_id, limit),
    )
    rows = cur.fetchall()
    conn.close()
    memories = []
    for r in rows:
        memories.append(
            {
                "id": r[0],
                "role": r[1],
                "content": r[2],
                "created_at": r[3],
            }
        )
    return memories
