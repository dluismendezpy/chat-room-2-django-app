# Django
from django.urls import path

# Owns
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room_name>/', views.room, name='room'),
]
