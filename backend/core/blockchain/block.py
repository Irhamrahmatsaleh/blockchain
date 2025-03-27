from typing import List
from datetime import datetime
from .transaction import Transaction
from .merkle_tree import MerkleTree
import time
from backend.wallet.wallet import Wallet
from backend.core.blockchain.transaction import Transaction

class Block:
    def __init__(self, index: int, transactions: List[Transaction], previous_hash: str, nonce: int = 0):
        self.index = index
        self.timestamp = datetime.utcnow()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.merkle_root = MerkleTree(transactions).root_hash
        self.hash = None  # Akan diisi saat mining selesai

    def to_dict(self):
        """Convert block to dictionary."""
        return {
            "index": self.index,
            "timestamp": self.timestamp.isoformat(),
            "transactions": [tx.to_dict() for tx in self.transactions],  # Convert transactions to dict
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
            "merkle_root": self.merkle_root,
            "hash": self.hash
        }

    def mine(self, difficulty: int, reward: float):
        """Function to mine the block and reward the miner."""
        from backend.core.mining.pow import proof_of_work

        # Menghitung Proof-of-Work
        nonce, block_hash, duration = proof_of_work(self, difficulty)

        # Simpan nonce dan hash setelah penambangan selesai
        self.nonce = nonce
        self.hash = block_hash

        # Tambahkan transaksi reward untuk miner
        miner_reward_transaction = Transaction(
            sender="network",  # Sistem blockchain memberikan reward
            recipient=self.transactions[0].sender,  # Penerima reward adalah miner yang berhasil
            amount=reward,  # Jumlah reward
            fee=0.0,  # Tidak ada fee untuk reward
            timestamp=time.time()
        )

        # Masukkan transaksi reward ke dalam list transaksi
        self.transactions.append(miner_reward_transaction)

            # Update saldo miner
        wallet = Wallet()
        wallet_balance = wallet.calculate_balance(self.transactions[0].sender, [self])  # Simulasi saldo
        print(f"Miner balance updated: {wallet_balance}")

        return block_hash, duration
