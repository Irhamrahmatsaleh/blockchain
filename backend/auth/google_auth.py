from fastapi import HTTPException
from backend.auth.firebase_config import firebase_auth

def verify_google_token(id_token: str):
    try:
        # Verifikasi token dari frontend
        decoded_token = firebase_auth.verify_id_token(id_token)
        uid = decoded_token.get("uid")
        email = decoded_token.get("email")

        if not uid or not email:
            raise ValueError("Missing uid or email in token.")

        return {
            "uid": uid,
            "email": email
        }

    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {str(e)}")
