# Django
import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

# Owns
from chat_app import sockets_routes

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'room_chat_project.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            sockets_routes.websocket_urlpatterns
        )
    )
})
