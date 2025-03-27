from cryptography.fernet import Fernet
import base64
import hashlib

def _derive_key(password: str) -> bytes:
    """Generate a Fernet key from password."""
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def encrypt_data(data: str, password: str) -> str:
    key = _derive_key(password)
    fernet = Fernet(key)
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data: str, password: str) -> str:
    key = _derive_key(password)
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data.encode()).decode()
