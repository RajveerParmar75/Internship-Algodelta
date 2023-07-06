import json
import os

from channels.generic.websocket import WebsocketConsumer
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import re_path

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dump({
            'type':'connection',
            'message':'you are done'
        }))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter([
            re_path(r'ws/data-server/$', ChatConsumer.as_asgi()),
        ])
    )
})
