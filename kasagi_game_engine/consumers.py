import json
from channels.generic.websocket import AsyncWebsocketConsumer

class StateSyncConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'global_state'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.send(text_data=json.dumps({"message": "Connected to Kasagi Game Engine!"}))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'state_update',
                'text': text_data
            }
        )

    async def state_update(self, event):
        await self.send(text_data=event['text'])
