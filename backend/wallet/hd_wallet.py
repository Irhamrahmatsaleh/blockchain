import hashlib
import hmac
import os

class HDWallet:
    def __init__(self, seed: bytes = None):
        self.seed = seed or os.urandom(32)
        self.master_key = self._derive_master_key(self.seed)

    def _derive_master_key(self, seed: bytes) -> str:
        return hmac.new(b"Neutron seed", seed, hashlib.sha512).hexdigest()

    def generate_child_key(self, index: int) -> str:
        data = f"{self.master_key}:{index}"
        return hashlib.sha256(data.encode()).hexdigest()
