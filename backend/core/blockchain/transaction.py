import json
import hashlib
from datetime import datetime

class Transaction:
    def __init__(self, sender: str, recipient: str, amount: float, signature: str = ""):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = datetime.utcnow().isoformat()
        self.signature = signature

    def to_dict(self):
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "timestamp": self.timestamp,
            "signature": self.signature
        }

    def to_json(self):
        return json.dumps(self.to_dict(), sort_keys=True)

    def calculate_hash(self):
        tx_data = self.to_json()
        return hashlib.sha256(tx_data.encode()).hexdigest()
