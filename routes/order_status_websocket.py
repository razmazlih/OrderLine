from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from typing import List

order_status_ws_router = APIRouter()


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@order_status_ws_router.websocket("/ws/order-status/{order_id}")
async def websocket_endpoint(websocket: WebSocket, order_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received message for order {order_id}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print(f"Connection closed for order {order_id}")


async def notify_order_status(order_id: int, status: str):
    await manager.broadcast(status)
