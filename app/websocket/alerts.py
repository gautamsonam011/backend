from fastapi import APIRouter
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

from app.websocket.manager import manager


router = APIRouter()


@router.websocket(
    "/ws/alerts/{organization_id}"
)
async def websocket_alerts(
    websocket: WebSocket,
    organization_id: str
):

    await manager.connect(
        organization_id,
        websocket
    )

    try:

        while True:

            data = await websocket.receive_text()

            await manager.broadcast(
                organization_id,
                f"Alert Triggered: {data}"
            )

    except WebSocketDisconnect:

        manager.disconnect(
            organization_id,
            websocket
        )