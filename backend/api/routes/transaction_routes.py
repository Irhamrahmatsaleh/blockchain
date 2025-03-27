from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/transaction", tags=["Transaction"])

class TransactionRequest(BaseModel):
    sender: str
    recipient: str
    amount: float

@router.post("/send")
def send_transaction(tx: TransactionRequest):
    # sementara dummy response
    return {
        "status": "success",
        "from": tx.sender,
        "to": tx.recipient,
        "amount": tx.amount
    }
