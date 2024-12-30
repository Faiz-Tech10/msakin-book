import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'msakin.settings')
django.setup()

from chat.routing import websocket_urlpatterns as chat_ws_urls
from notifications.routing import websocket_urlpatterns as notifications_ws_urls
from properties.routing import websocket_urlpatterns as properties_ws_urls

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                chat_ws_urls +
                notifications_ws_urls +
                properties_ws_urls
            )
        )
    ),
})
