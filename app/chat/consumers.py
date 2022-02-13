from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync

from . import services as chat_services
from .serializers import MessageSerializer


class ChatConsumer(JsonWebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)("chat", self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("chat", self.channel_name)

    def receive_json(self, content):
        serializer = MessageSerializer(data=content)

        if serializer.is_valid():
            async_to_sync(self.channel_layer.group_send)(
                "chat",
                {
                    "type": "chat.message",
                    "text": content,
                    "user": self.scope['user']
                },
            )

    def chat_message(self, event):
        message = chat_services.create_message(event['text'], event["user"])
        self.send_json(content=MessageSerializer(message).data)
