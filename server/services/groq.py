import os
import httpx


class GroqClient:
    def __init__(self, endpoint: str | None = None, api_key: str | None = None):
        self.endpoint = endpoint or os.environ.get("GROQ_API_ENDPOINT", "")
        self.api_key = api_key or os.environ.get("GROQ_API_KEY", "")

    async def generate(self, prompt: str, memory: str | None = None) -> str:
        # If no endpoint is configured, return a simple echo for MVP
        if not self.endpoint:
            return f"AI: (offline) {prompt[:100]}..."

        payload = {"prompt": prompt}
        if memory:
            payload["memory"] = memory

        headers = {}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                resp = await client.post(self.endpoint, json=payload, headers=headers)
            if resp.status_code == 200:
                data = resp.json()
                # Expect a common shape; adjust as real API evolves
                return data.get("response") or data.get("text") or ""
            else:
                return f"Error {resp.status_code}: {resp.text}"
        except Exception as e:
            return f"Groq error: {str(e)}"


# Singleton-like instance for reuse across routes
groq_client = GroqClient()
