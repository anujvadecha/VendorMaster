from django.urls import re_path

from . import consumers

websocket_urlpatterns= [
    re_path(r'ws/ticker/$', consumers.TickConsumer.as_asgi()),
    re_path(r'ws/orderEngine/$', consumers.OrderEngineConsumer.as_asgi()),
    re_path(r'ws/vendor/$', consumers.VendorConsumer.as_asgi()),
]