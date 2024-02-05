from django.urls import path
from .consumers import MyConsumer

websocket_urlpatterns = [
    path('ws/some_path/', MyConsumer.as_asgi()),
]

