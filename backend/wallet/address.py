import hashlib
import base64
from backend.core.crypto.keys import public_key_to_pem

def generate_address(public_key) -> str:
    # Dapatkan public key dalam format string PEM
    public_key_pem = public_key_to_pem(public_key)

    # Hash ganda (SHA256 → RIPEMD160) → mirip Bitcoin
    sha256_hash = hashlib.sha256(public_key_pem.encode()).digest()
    ripemd160 = hashlib.new("ripemd160")
    ripemd160.update(sha256_hash)
    address_bytes = ripemd160.digest()

    # Encode (versi simple, bisa upgrade ke Base58)
    address = base64.b32encode(address_bytes).decode()[:40]
    return address

def is_valid_address(address: str) -> bool:
    # Validasi panjang dan karakter dasar
    return isinstance(address, str) and len(address) >= 20
