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
        sio = socketio.Client(reconnection=True)

        @sio.on(event='connect')
        def connect():
            print('connection established')

        @sio.on(event='disconnect')
        def disconnect():
            print('disconnected from server')

        @sio.on(event='mcxratesupdate:App\\Events\\MCXRateUpdates')
        def my_message(data):
            tick = {
                "type": "tick",
                "gold_tick":
                    {
                        "bid": float(json.loads(data['updatedata'])[0]['gold1_bid']),
                        "ask": float(json.loads(data['updatedata'])[0]['gold1_ask']),
                        "low": float(json.loads(data['updatedata'])[0]['gold1_low']),
                        "high": float(json.loads(data['updatedata'])[0]['gold1_high'])
                    },
                "silver_tick":
                    {
                        "bid": float(json.loads(data['updatedata'])[1]['gold1_bid']),
                        "ask": float(json.loads(data['updatedata'])[1]['gold1_ask']),
                        "low": float(json.loads(data['updatedata'])[1]['gold1_low']),
                        "high": float(json.loads(data['updatedata'])[1]['gold1_high'])
                    },
                "gold_comex":
                    {
                        "bid": float(json.loads(data['updatedata'])[2]['gold1_bid']),
                        "ask": float(json.loads(data['updatedata'])[2]['gold1_ask']),
                        "low": float(json.loads(data['updatedata'])[2]['gold1_low']),
                        "high": float(json.loads(data['updatedata'])[2]['gold1_high'])
                    },
                "silver_comex":
                    {
                        "bid": float(json.loads(data['updatedata'])[3]['gold1_bid']),
                        "ask": float(json.loads(data['updatedata'])[3]['gold1_ask']),
                        "low": float(json.loads(data['updatedata'])[3]['gold1_low']),
                        "high": float(json.loads(data['updatedata'])[3]['gold1_high'])
                    },
                "dollar":
                    {
                        "bid": float(json.loads(data['updatedata'])[4]['gold1_bid']),
                        "ask": float(json.loads(data['updatedata'])[4]['gold1_ask']),
                        "low": float(json.loads(data['updatedata'])[4]['gold1_low']),
                        "high": float(json.loads(data['updatedata'])[4]['gold1_high'])
                    }
            }
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                settings.SOCKET_GROUP,
                tick
            )
            update_high_low.delay(tick)
        sio.connect('http://209.59.158.15:3001/',headers={ "secure": "true", "rejectUnauthorized": "false" },transports=["websocket"])
        # sio.wait()
        # while True:
        #  time.sleep(1)
