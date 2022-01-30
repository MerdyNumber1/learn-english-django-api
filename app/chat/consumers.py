from channels.generic.websocket import JsonWebsocketConsumer

from . import services as chat_services
from .serializers import MessageSerializer


class ChatConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive_json(self, content):
        serializer = MessageSerializer(data=content)

        if serializer.is_valid():
            message = chat_services.create_message(content, self.scope['user'])
            self.send_json(content=MessageSerializer(message).data)


