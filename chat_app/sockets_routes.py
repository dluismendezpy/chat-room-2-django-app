# Django
from django.urls import path

# Owns
from . import views

websocket_urlpatterns = [
    path('ws/<str:room_chat_name>/', views.ChatConsumer.as_asgi()),
]