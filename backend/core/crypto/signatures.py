import base64
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature

# 🔐 Fungsi untuk menandatangani hash pesan
def sign_message(private_key: ec.EllipticCurvePrivateKey, message_hash: str) -> str:
    signature = private_key.sign(
        message_hash.encode(),
        ec.ECDSA(hashes.SHA256())
    )
    return base64.b64encode(signature).decode()

# ✅ Fungsi untuk verifikasi tanda tangan
def verify_signature(public_key_pem: str, signature_b64: str, message_hash: str) -> bool:
    try:
        public_key = serialization.load_pem_public_key(public_key_pem.encode())
        signature = base64.b64decode(signature_b64)
        public_key.verify(
            signature,
            message_hash.encode(),
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except InvalidSignature:
        return False
    except Exception as e:
        print(f"Signature verification error: {e}")
        return False
