import time
import hashlib
from backend.core.blockchain.block import Block
from typing import Tuple

def proof_of_work(block: Block, difficulty: int) -> Tuple[int, str, float]:
    prefix = "0" * difficulty  # Miner harus menemukan hash yang dimulai dengan prefix
    nonce = 0
    start = time.time()

    while True:
        block.nonce = nonce
        # Gunakan hashing SHA-256 untuk block
        block_hash = hashlib.sha256(f"{block.to_dict()}".encode()).hexdigest()
        if block_hash.startswith(prefix):  # Cek apakah hash memenuhi target
            block.hash = block_hash
            duration = round(time.time() - start, 4)
            return nonce, block_hash, duration
        nonce += 1
