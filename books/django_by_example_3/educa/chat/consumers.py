import json

from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data, bytes_data=None):
        text_data_as_json = json.loads(text_data)
        message = text_data_as_json["message"]
        self.send(
            text_data=json.dumps({"user": self.scope["user"].username, "message": message})
        )
