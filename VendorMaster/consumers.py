import json
import threading
from random import random, randint
from uuid import UUID
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from VendorMaster import settings
from orderManagement.api.serializers import OrderSerializer
from orderManagement.models import Order, OrderStatus, OrderType
from vendorbase.api.serializers import SymbolSerializer, GlobalPremiumSerializer, VendorSerializer, FavouriteSerializer
from vendorbase.models import Symbol, GlobalPremium, Vendor, Favourite
import time

class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

class TickConsumer(WebsocketConsumer):

    room_group_name=settings.SOCKET_GROUP

    def connect(self):
        self.user = self.scope["user"]
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

    # #Not used anymore
    # def send_gold_ticks(self,ticks):
    #         async_to_sync(self.channel_layer.group_send)(
    #             self.room_group_name,
    #             {
    #                 'type':"tick",
    #                 "gold_tick":ticks
    #             }
    #         )
    #         time.sleep(0.5)
    # noinspection PyMethodOverriding

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        type=text_data_json['type']
        if (type == "ticker_request"):
            self.send(json.dumps({
                'instruments':json.dumps(SymbolSerializer(Symbol.objects.all(),many=True).data,cls=UUIDEncoder),
                'global_premium':GlobalPremiumSerializer(GlobalPremium.objects.all().first()).data,
                'favourites':json.dumps(FavouriteSerializer(Favourite.objects.filter(user_id=self.user),many=True).data,cls=UUIDEncoder)
            }))
        if(type=="vendor_request"):
            self.send(json.dumps({
                "vendors":VendorSerializer(Vendor.objects.all(),many=True).data
            }))

    def tick(self,data):
        message = data
        self.send(text_data=json.dumps(message))

    #For future use in frontend ui to update premums on the go
    #Backend admin page anyway reloads on update
    def instrument_update(self,data):
        self.send(text_data=json.dumps(data, cls=UUIDEncoder))

    def order_update(self,data):
        pass

    def premium_update(self,data):
        print(f" Premium has been updated for {data}")


class OrderEngineConsumer(WebsocketConsumer):

    room_group_name=settings.SOCKET_GROUP

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

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        type=text_data_json['type']
        if (type == "ticker_request"):
            self.send(json.dumps({
                'instruments':json.dumps(SymbolSerializer(Symbol.objects.all(),many=True).data,cls=UUIDEncoder),
                'global_premium':GlobalPremiumSerializer(GlobalPremium.objects.all().first()).data
            }))
        if(type=="all_orders_limit_pending"):
            self.send(json.dumps({
                'orders':
                    json.dumps(OrderSerializer(Order.objects.filter(status=OrderStatus.WAITING_FOR_LIMIT).filter(type=OrderType.LIMIT), many=True).data,cls=UUIDEncoder),
            }))
        if(type=="order_filled"):
            print(len(text_data_json["order_ids"]))
            Order.objects.filter(order_id__in=text_data_json["order_ids"]).update(status=OrderStatus.OPEN)

    def instrument_update(self,data):
        self.send(text_data=json.dumps(data,cls=UUIDEncoder))

    def order_update(self,data):
        self.send(text_data=json.dumps(data,cls=UUIDEncoder))

    def tick(self,data):
        message = data
        self.send(text_data=json.dumps(message))
    #For future use in frontend ui to update premums on the go
    #Backend admin page anyway reloads on update
    def premium_update(self,data):
        print(f" Premium has been updated for {data}")


class VendorConsumer(WebsocketConsumer):
    room_group_name = settings.SOCKET_GROUP

    def connect(self):
        self.user = self.scope["user"]
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

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        type = text_data_json['type']
        if (type == "ticker_request"):
            self.send(json.dumps({
                'instruments': json.dumps(SymbolSerializer(Symbol.objects.filter(vendor_id__user_id=self.user), many=True).data, cls=UUIDEncoder),
                'global_premium': GlobalPremiumSerializer(GlobalPremium.objects.all().first()).data,
                'favourites': json.dumps(
                    FavouriteSerializer(Favourite.objects.filter(user_id=self.user), many=True).data, cls=UUIDEncoder)
            }))
        if (type == "vendor_request"):
            self.send(json.dumps({
                "vendors": VendorSerializer(Vendor.objects.all(), many=True).data
            }))

    def tick(self, data):
        message = data
        self.send(text_data=json.dumps(message))

    # For future use in frontend ui to update premums on the go
    # Backend admin page anyway reloads on update
    def instrument_update(self, data):
        self.send(text_data=json.dumps(data, cls=UUIDEncoder))

    def order_update(self, data):
        pass

    def premium_update(self, data):
        print(f" Premium has been updated for {data}")
