from fastapi import APIRouter

router = APIRouter(prefix="/network", tags=["Network"])

@router.get("/peers")
def get_peers():
    # Dummy list of peers
    return {
        "peers": [
            "127.0.0.1:8000",
            "192.168.1.10:8000"
        ]
    }

@router.get("/sync-status")
def get_sync_status():
    return {
        "status": "synced",
        "current_block": 128,
        "known_block": 128
    }
