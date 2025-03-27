import json
from backend.core.crypto.keys import (
    private_key_to_pem,
    public_key_to_pem,
    load_private_key,
    load_public_key
)

def save_keystore(private_key, filepath: str):
    data = {
        "private_key": private_key_to_pem(private_key)
    }
    with open(filepath, "w") as f:
        json.dump(data, f)
    print(f"🔐 Keystore saved to {filepath}")

def load_keystore(filepath: str):
    with open(filepath, "r") as f:
        data = json.load(f)
        private_key = load_private_key(data["private_key"])
        public_key = private_key.public_key()
        return private_key, public_key
