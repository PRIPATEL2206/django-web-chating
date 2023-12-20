from django.urls import path
from . import consumer


websocket_urlpath=[
    path("ws/test/",consumer.MyConsumer.as_asgi()),
]