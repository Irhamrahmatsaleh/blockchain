from fastapi import WebSocket

# Sementara simpan semua koneksi aktif
connected_clients = []

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            # Untuk debug/demo: broadcast ulang
            for client in connected_clients:
                if client != websocket:
                    await client.send_text(f"Received: {data}")
    except Exception:
        connected_clients.remove(websocket)
        await websocket.close()
