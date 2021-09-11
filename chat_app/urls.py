# Django
from django.urls import path

# Owns
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
