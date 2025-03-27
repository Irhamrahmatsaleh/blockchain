from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# 🔐 Generate key pair
def generate_key_pair():
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()
    return private_key, public_key

# 🔄 Convert private key to PEM string
def private_key_to_pem(private_key) -> str:
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    return pem.decode()

# 🔄 Convert public key to PEM string
def public_key_to_pem(public_key) -> str:
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return pem.decode()

# 🔁 Load private key from PEM string
def load_private_key(pem_str: str):
    return serialization.load_pem_private_key(pem_str.encode(), password=None)

# 🔁 Load public key from PEM string
def load_public_key(pem_str: str):
    return serialization.load_pem_public_key(pem_str.encode())
