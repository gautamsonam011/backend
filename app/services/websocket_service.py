from app.core.websocket_manager import manager


class WebSocketService:

    @staticmethod
    async def send_event_update(
        message: str
    ):

        await manager.broadcast(message)