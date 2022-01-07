import json
from channels.generic.websocket import JsonWebsocketConsumer

import services as chat_services


class ChatConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive_json(self, content):
        message = chat_services.create_message(content)

        self.send_json(content=message)
