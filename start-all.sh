#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "$0")" && pwd)
echo "[START] Backend on http://0.0.0.0:8000 (reload on change)"
uvicorn server.main:app --host 0.0.0.0 --port 8000 --reload &
BACKEND_PID=$!

if [ -d "$ROOT_DIR/app" ]; then
  echo "[START] Frontend (Expo)"
  (cd "$ROOT_DIR/app" && npm install >/dev/null 2>&1 || true; npm run start >/dev/null 2>&1) &
  FRONTEND_PID=$!
else
  FRONTEND_PID=0
fi

echo "[INFO] Backend PID: $BACKEND_PID; Frontend PID: $FRONTEND_PID (if started)"
wait $BACKEND_PID
if [ "$FRONTEND_PID" -ne 0 ]; then
  wait $FRONTEND_PID
fi
