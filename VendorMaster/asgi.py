"""
ASGI config for VendorMaster project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VendorMaster.settings")
django.setup()
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import VendorMaster.routing
from VendorMaster.TokenAuthMiddleware import QueryAuthMiddleware
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VendorMaster.settings")

#application = get_default_application()
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VendorMaster.settings')

application = ProtocolTypeRouter({
  "http": AsgiHandler(),
  "websocket": QueryAuthMiddleware(
        URLRouter(
            VendorMaster.routing.websocket_urlpatterns
        )
    ),
})
