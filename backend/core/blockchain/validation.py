from .transaction import Transaction
from .block import Block
from backend.core.crypto.signatures import verify_signature

def validate_transaction(tx: Transaction) -> bool:
    # Verifikasi struktur + signature
    if not tx.sender or not tx.recipient or tx.amount <= 0:
        return False

    tx_hash = tx.calculate_hash()
    return verify_signature(tx.sender, tx.signature, tx_hash)

def validate_block(block: Block, previous_block: Block) -> bool:
    if block.previous_hash != previous_block.hash:
        return False

    if block.index != previous_block.index + 1:
        return False

    # Nanti bisa tambahkan validasi proof-of-work juga
    return True
