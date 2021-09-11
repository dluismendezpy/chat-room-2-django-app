# Django
from django.urls import path

# Owns
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room_chat_name>/', views.room_view, name='chat_room')
]
