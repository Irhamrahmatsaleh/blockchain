from fastapi import APIRouter

router = APIRouter(prefix="/mining", tags=["Mining"])

@router.get("/status")
def get_mining_status():
    return {
        "status": "idle",
        "hash_rate": "0 H/s",
        "last_block_mined": None
    }
