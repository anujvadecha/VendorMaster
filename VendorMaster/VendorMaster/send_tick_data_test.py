import time
from random import randint

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from VendorMaster import settings


def send_tick_data():
    while True:
        tick = {
            "type": "tick",
            "gold_tick":
                {
                    "bid": randint(40000, 60000),
                    "ask": randint(40000, 60000)
                }
        }
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            settings.SOCKET_GROUP,
            tick
        )
        # update_high_low.delay(tick)
        time.sleep(1)
