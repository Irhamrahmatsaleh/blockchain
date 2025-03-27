from __future__ import annotations
import time
from typing import List

from backend.core.crypto.keys import (
    generate_key_pair,
    private_key_to_pem,
    public_key_to_pem,
    load_private_key
)
from backend.core.crypto.signatures import sign_message, verify_signature
from backend.core.crypto.hashing import hash_data
from backend.core.blockchain.transaction import Transaction
from backend.utils.helpers import encrypt_data, decrypt_data  # Harus tersedia


class Wallet:
    def __init__(self):
        self.private_key, self.public_key = generate_key_pair()
        self.address = self.generate_address()
        self.transactions = []

    def generate_address(self) -> str:
        """Generate address dari public key."""
        public_pem = public_key_to_pem(self.public_key)
        return hash_data(public_pem)[:40]  # Bisa upgrade ke Base58

    def get_public_key_pem(self) -> str:
        """Ambil public key dalam format PEM."""
        return public_key_to_pem(self.public_key)

    def get_private_key_pem(self) -> str:
        """Ambil private key dalam format PEM."""
        return private_key_to_pem(self.private_key)

    def sign_transaction(self, message_hash: str) -> str:
        """Tanda tangani transaksi."""
        return sign_message(self.private_key, message_hash)

    @staticmethod
    def calculate_balance(address: str, blockchain: List[dict]) -> float:
        """Hitung saldo berdasarkan seluruh transaksi dalam blockchain."""
        balance = 0.0
        for block in blockchain:
            for tx in block.transactions:
                if isinstance(tx, dict):
                    tx = Transaction(**tx)
                if tx.recipient == address:
                    balance += tx.amount
                if tx.sender == address:
                    balance -= tx.amount
                    if hasattr(tx, 'fee'):
                        balance -= tx.fee
        return round(balance, 8)

    def create_transaction(
        self,
        recipient: str,
        amount: float,
        blockchain: List[dict],
        fee: float = 0.0001
    ) -> Transaction:
        """Buat transaksi baru."""
        if amount <= 0:
            raise ValueError("Amount must be positive")

        current_balance = self.calculate_balance(self.address, blockchain)
        total_cost = amount + fee

        if total_cost > current_balance:
            raise ValueError(f"Insufficient funds. Balance: {current_balance}, Required: {total_cost}")

        transaction = Transaction(
            sender=self.address,
            recipient=recipient,
            amount=amount,
            fee=fee,
            timestamp=time.time()
        )

        transaction_hash = transaction.calculate_hash()
        transaction.signature = self.sign_transaction(transaction_hash)
        return transaction

    @staticmethod
    def verify_signature(public_key_pem: str, signature: str, message_hash: str) -> bool:
        """Verifikasi signature transaksi."""
        try:
            return verify_signature(public_key_pem, signature, message_hash)
        except Exception as e:
            print(f"Signature verification failed: {e}")
            return False

    def export_wallet(self, password: str) -> dict:
        """Ekspor wallet sebagai data terenkripsi."""
        encrypted_private_key = encrypt_data(self.get_private_key_pem(), password)
        return {
            'address': self.address,
            'encrypted_private_key': encrypted_private_key,
            'public_key': self.get_public_key_pem()
        }

    @classmethod
    def import_wallet(cls, wallet_data: dict, password: str) -> Wallet:
        """Impor wallet dari data terenkripsi."""
        try:
            decrypted_private_key = decrypt_data(wallet_data['encrypted_private_key'], password)
            wallet = cls()
            wallet.private_key = load_private_key(decrypted_private_key)
            wallet.public_key = wallet_data['public_key']
            wallet.address = wallet_data['address']
            return wallet
        except Exception as e:
            raise ValueError(f"Failed to import wallet: {e}")
