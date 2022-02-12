import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

asgi_app = get_asgi_application()

from core.middlewares import QueryAuthMiddleware
import chat.routing


django.setup()

application = ProtocolTypeRouter({
    "http": asgi_app,
    "websocket": QueryAuthMiddleware(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
