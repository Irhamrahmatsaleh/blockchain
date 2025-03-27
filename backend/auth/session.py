from typing import Dict
from fastapi import Request, HTTPException

# Sesi aktif (sementara disimpan dalam memori)
active_sessions: Dict[str, str] = {}

def create_session(uid: str, token: str):
    active_sessions[uid] = token

def destroy_session(uid: str):
    active_sessions.pop(uid, None)

def validate_session(request: Request) -> str:
    """Validasi token dan uid dari header."""
    auth_header = request.headers.get("Authorization")
    uid = request.headers.get("X-UID")

    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")
    if not uid or uid not in active_sessions:
        raise HTTPException(status_code=403, detail="Invalid or expired session")

    token = auth_header.split(" ")[1]
    if active_sessions[uid] != token:
        raise HTTPException(status_code=403, detail="Session token mismatch")

    return uid  # bisa digunakan untuk endpoint logic
