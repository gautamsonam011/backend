from fastapi import APIRouter
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

from app.core.websocket_manager import manager


router = APIRouter(
    prefix="/ws",
    tags=["WebSocket"]
)


@router.websocket("/events")
async def websocket_events(
    websocket: WebSocket
):

    await manager.connect(websocket)

    try:

        while True:

            data = await websocket.receive_text()

            await manager.broadcast(
                f"Message: {data}"
            )

    except WebSocketDisconnect:

        manager.disconnect(websocket)