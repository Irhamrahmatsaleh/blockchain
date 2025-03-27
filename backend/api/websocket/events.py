from fastapi import APIRouter, WebSocket
from .handlers import websocket_endpoint

router = APIRouter()

@router.websocket("/ws")
async def websocket_route(websocket: WebSocket):
    await websocket_endpoint(websocket)
