from fastapi import APIRouter, Request, HTTPException, Header
from backend.auth.google_auth import verify_google_token
from backend.auth.session import create_session, destroy_session
from backend.wallet.wallet import Wallet

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
async def login_via_google(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=400, detail="Invalid Authorization header format")

    id_token = authorization.split(" ")[1]

    user_info = verify_google_token(id_token)
    uid = user_info["uid"]
    email = user_info["email"]

    # 🔐 Inisialisasi wallet user (bisa kita simpan nanti ke DB atau cache)
    wallet = Wallet()
    create_session(uid, id_token)  # Simpan session sementara

    return {
        "message": "Login successful",
        "uid": uid,
        "email": email,
        "wallet_address": wallet.address,
        "public_key": wallet.get_public_key_pem()
    }

@router.post("/logout")
async def logout(request: Request):
    uid = request.headers.get("X-UID")
    if not uid:
        raise HTTPException(status_code=400, detail="Missing X-UID header")

    destroy_session(uid)
    return {"message": f"Logout successful for UID {uid}"}
