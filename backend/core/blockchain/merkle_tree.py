import hashlib
from typing import List
from .transaction import Transaction

class MerkleTree:
    def __init__(self, transactions: List[Transaction]):
        self.transactions = transactions
        self.root_hash = self.build_merkle_root()

    def build_merkle_root(self) -> str:
        if not self.transactions:
            return ""

        # Hash setiap transaksi
        hashes = [tx.calculate_hash() for tx in self.transactions]

        # Buat Merkle Tree dari hash transaksi
        while len(hashes) > 1:
            if len(hashes) % 2 != 0:
                hashes.append(hashes[-1])  # Duplicate last if odd

            new_hashes = []
            for i in range(0, len(hashes), 2):
                combined = hashes[i] + hashes[i+1]
                new_hash = hashlib.sha256(combined.encode()).hexdigest()
                new_hashes.append(new_hash)

            hashes = new_hashes

        return hashes[0]
