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
        sio = socketio.Client()

        @sio.event
        def connect():
            print('connection established')

        @sio.event
        def disconnect():
            print('disconnected from server')

        @sio.on('mcxratesupdate:App\\Events\\MCXRateUpdates')
        def my_message(data):
            tick = {
                "type": "tick",
                "gold_tick":
                    {
                        "bid": json.loads(data['updatedata'])[0]['gold1_bid'],
                        "ask": json.loads(data['updatedata'])[0]['gold1_ask']
                    }
            }
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                settings.SOCKET_GROUP,
                tick
            )
            # rates=json.loads(data)
            # rates=rates['updatedata']
            # print(rates)
            # print('message received with ', data)
            # sio.emit('my response', {'response': 'my response'})


        sio.connect('http://209.59.158.15:3001/',headers={ "secure": "true", "rejectUnauthorized": "false", "reconnect" : "true" },transports=["websocket"])
        # sio.wait()
        # while True:

            # update_high_low.delay(tick)
        #     time.sleep(1)
