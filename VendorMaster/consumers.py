import json
import threading
from random import random, randint
from uuid import UUID
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from vendorbase.api.serializers import SymbolSerializer, GlobalPremiumSerializer
from vendorbase.models import Symbol, GlobalPremium
import time

class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return obj.hex
        return json.JSONEncoder.default(self, obj)

class TickConsumer(WebsocketConsumer):

    room_group_name="ticker_group"

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    #Not used anymore
    def send_gold_ticks(self,ticks):
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type':"tick",
                    "gold_tick":ticks
                }
            )
            time.sleep(0.5)

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        type=text_data_json['type']
        if (type == "ticker_request"):
            self.send(json.dumps({
                'instruments':SymbolSerializer(Symbol.objects.all(),many=True).data,
                'global_premium':GlobalPremiumSerializer(GlobalPremium.objects.all().first()).data
            }))

    def tick(self,data):
        message = data
        self.send(text_data=json.dumps(message))
        pass
    #For future use in frontend ui to update premums on the go
    #Backend admin page anyway reloads on update
    def premium_update(self,data):
        print(f"premium has been updated for {data}")
        pass

class OrderConsumer(WebsocketConsumer):
    room_group_name = "order_group"

    pass