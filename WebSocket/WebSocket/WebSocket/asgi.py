"""
ASGI config for WebSocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
import json
import os
from pprint import pprint

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import re_path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebSocket.settings')
chat_user_list=[]
{'id': 1, 'socket_obj' : None}

list_of_user=[]

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            "type": 'done'
        }))
        if len(list_of_user) >0:
            for i in list_of_user:
                i['object'].notify()
    def notify(self):
        self.send("hello")
    def receive(self, text_data=None, bytes_data=None):
        if str(text_data).isdigit():
            list_of_user.append({'id':text_data,'object':self})
            # print(list_of_user)

        else:
            try:
                soc_data = json.loads(str(text_data))
                print(soc_data)
                message=soc_data['message']
                self.send(text_data=json.dumps({
                    'type':'chat',
                    'message':message
                }))

            except Exception as e:
                pass


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter([
            re_path(r'^ws/socket-server/$', ChatConsumer.as_asgi()),
        ])
    ),
})
