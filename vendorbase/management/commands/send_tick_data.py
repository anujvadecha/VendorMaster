import json
from random import randint
import time
import socketio
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.cache import cache
from django.core.management import BaseCommand
from VendorMaster import settings
from VendorMaster.consumers import TickConsumer
from vendorbase.models import Symbol
from vendorbase.tasks import update_high_low

class Command(BaseCommand):
    help = 'Process to send gold ticker data'
    def handle(self, *args, **options):
        # sio = socketio.Client(reconnection=True)

        # @sio.on(event='connect')
        def connect():
            print('connection established')

        # @sio.on(event='disconnect')
        def disconnect():
            print('disconnected from server')

        # @sio.on(event='mcxratesupdate:App\\Events\\MCXRateUpdates')
        while True:
        # def my_message(data):
            tick = {
                "type": "tick",
                "gold_tick":
                    {
                        "bid": randint(50000,50800),
                        "ask": randint(50000,50800),
                        "low": randint(50000,50800),
                        "high": randint(50000,50800)
                    },
                "silver_tick":
                    {
                        "bid": randint(23, 25),
                        "ask": randint(23, 25),
                        "low": randint(23, 25),
                        "high": randint(23, 25)
                    },
                "gold_comex":
                    {
                        "bid": randint(1840,1840),
                        "ask": randint(1840,1840),
                        "low": randint(1840,1840),
                        "high": randint(1840,1840)
                    },
                "silver_comex":
                    {
                        "bid": randint(23, 25),
                        "ask": randint(23, 25),
                        "low": randint(23, 25),
                        "high": randint(23, 25)
                    },
                "dollar":
                    {
                        "bid": randint(74, 75),
                        "ask": randint(74, 75),
                        "low": randint(74, 75),
                        "high": randint(74, 75)
                    }
            }
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                settings.SOCKET_GROUP,
                tick
            )
            update_high_low.delay(tick)
            time.sleep(0.5)
        # sio.connect('http://209.59.158.15:3001/',headers={ "secure": "true", "rejectUnauthorized": "false" },transports=["websocket"])
        # sio.wait()
        # while True:
        # time.sleep(1)

