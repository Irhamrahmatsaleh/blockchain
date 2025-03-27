from fastapi import APIRouter, HTTPException
from backend.database import SessionLocal
from backend.database.models.block import Block
from backend.database.models.transaction import Transaction
from sqlalchemy.orm import Session

router = APIRouter(prefix="/explorer", tags=["Explorer"])

# Get block by ID
@router.get("/block/{block_id}")
def get_block(block_id: int, db: Session = SessionLocal()):
    block = db.query(Block).filter(Block.id == block_id).first()
    if not block:
        raise HTTPException(status_code=404, detail="Block not found")
    return block.to_dict()

# Get transaction by ID
@router.get("/transaction/{tx_id}")
def get_transaction(tx_id: int, db: Session = SessionLocal()):
    tx = db.query(Transaction).filter(Transaction.id == tx_id).first()
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return tx.to_dict()
