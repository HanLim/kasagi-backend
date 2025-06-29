"""
ASGI config for kasagi_game_engine project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/

"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from kasagi_game_engine.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kasagi_game_engine.settings')

application = ProtocolTypeRouter({
    "http": __import__('django.core.asgi').core.asgi.get_asgi_application(),
    "websocket": URLRouter(websocket_urlpatterns),
})