from fastapi import WebSocket

from collections import defaultdict


class ConnectionManager:

    def __init__(self):

        # organization_id -> websocket list

        self.active_connections = defaultdict(list)

    async def connect(
        self,
        organization_id: str,
        websocket: WebSocket
    ):

        await websocket.accept()

        self.active_connections[
            organization_id
        ].append(websocket)

    def disconnect(
        self,
        organization_id: str,
        websocket: WebSocket
    ):

        self.active_connections[
            organization_id
        ].remove(websocket)

    async def send_personal_message(
        self,
        message: str,
        websocket: WebSocket
    ):

        await websocket.send_text(message)

    async def broadcast(
        self,
        organization_id: str,
        message: str
    ):

        for connection in self.active_connections[
            organization_id
        ]:

            await connection.send_text(message)


manager = ConnectionManager()