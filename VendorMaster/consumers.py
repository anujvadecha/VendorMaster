import json
import threading
from random import random, randint
from uuid import UUID
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import AnonymousUser

from VendorMaster import settings
from orderManagement.api.serializers import OrderSerializer
from orderManagement.models import Order, OrderStatus, OrderType
from userBase.models import NormalUser
from vendorbase.api.serializers import SymbolSerializer, GlobalPremiumSerializer, VendorSerializer, FavouriteSerializer
from vendorbase.models import Symbol, GlobalPremium, Vendor, Favourite
import time
import logging
logger = logging.getLogger(__name__)


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


class TickConsumer(WebsocketConsumer):
    room_group_name = settings.SOCKET_GROUP
    def connect(self):
        logger.info(f"{self.scope['user']} connected")
        self.user = self.scope["user"]
        print(self.user)
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
            if(self.user == AnonymousUser()):
                logger.info('Anonymous user ticker request')
                print('requested for ticker from anon')
                self.send(json.dumps({
                    'instruments': json.dumps(SymbolSerializer(Symbol.objects.all(), many=True).data, cls=UUIDEncoder),
                    'global_premium': GlobalPremiumSerializer(GlobalPremium.objects.all().first()).data,
                }))
            else:
                logger.info(f'{self.user} requested for ticker request')
                print('requested for ticker from user')
                self.send(json.dumps({
                    'instruments': json.dumps(SymbolSerializer(Symbol.objects.all(), many=True).data, cls=UUIDEncoder),
                    'global_premium': GlobalPremiumSerializer(GlobalPremium.objects.all().first()).data,
                    'favourites': json.dumps(
                        FavouriteSerializer(Favourite.objects.filter(
                            user_id=self.user), many=True).data,
                        cls=UUIDEncoder)
                }))
        if(type == "vendor_request"):
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
        print("helllooooo")
        print(data)
        if(self.user != AnonymousUser):
            if(data["user"] == self.user.id):
                self.send(text_data=json.dumps({
                    "type": "order_update",
                    "order_update": data["order_update"]
                }, cls=UUIDEncoder))
            else:
                print("hii")
                print("not this user")

    def cancel(self, data):
        pass

    def premium_update(self, data):
        print(f" Premium has been updated for {data}")


class OrderEngineConsumer(WebsocketConsumer):

    room_group_name = settings.SOCKET_GROUP

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
        print("receive from consumer")
        text_data_json = json.loads(text_data)
        type = text_data_json['type']
        if (type == "ticker_request"):
            self.send(json.dumps({
                'instruments': json.dumps(SymbolSerializer(Symbol.objects.all(), many=True).data, cls=UUIDEncoder),
                'global_premium': GlobalPremiumSerializer(GlobalPremium.objects.all().first()).data
            }))
        if(type == "all_orders_limit_pending"):
            print("i am here on best limit !!!")
            print(Order.objects.filter(status=OrderStatus.WAITING_FOR_LIMIT, type__in=[
                OrderType.LIMIT, OrderType.BEST_LIMIT]).filter())
            print("done")
            self.send(json.dumps({
                'orders':
                    json.dumps(OrderSerializer(Order.objects.filter(status=OrderStatus.WAITING_FOR_LIMIT, type__in=[
                               OrderType.LIMIT, OrderType.BEST_LIMIT]), many=True).data, cls=UUIDEncoder),
            }))
        if(type == "order_filled"):
            print(f"order fill called on order")
            orders = Order.objects.filter(
                order_id__in=text_data_json["order_ids"])
            print(f"order fill called on order: {orders}")
            for order in orders:
                if(order.status != OrderStatus.CANCELLED):
                    if (order.type == OrderType.BEST_LIMIT):
                        order.status = OrderStatus.OPEN
                        order.save()
                        best_limit_orders_to_be_cancelled = Order.objects.filter(
                            best_limit_id=order.best_limit_id, status=OrderStatus.WAITING_FOR_LIMIT)
                        print(
                            f"best_limit_orders_to_be_cancelled:{best_limit_orders_to_be_cancelled} ")
                        for bloc in best_limit_orders_to_be_cancelled:
                            bloc.status = OrderStatus.CANCELLED
                            bloc.save()
                    else:
                        order.status = OrderStatus.OPEN
                        order.save()

    def instrument_update(self, data):
        self.send(text_data=json.dumps(data, cls=UUIDEncoder))

    def order_update(self, data):
        print("order update from consumer")
        order_update = json.loads(data['order_update'])
        order_type_limit = order_update['type'] == OrderType.LIMIT or OrderType.BEST_LIMIT
        order_status_waiting_for_limit = order_update['status'] == OrderStatus.WAITING_FOR_LIMIT
        if order_type_limit and order_status_waiting_for_limit:
        # if order_type_limit:
            self.send(text_data=json.dumps(data, cls=UUIDEncoder))

    def cancel(self, data):
        print(f"on cancel req: {data}")
        self.send(text_data=json.dumps(data))

    def tick(self, data):
        message = data
        self.send(text_data=json.dumps(message))
    # For future use in frontend ui to update premums on the go
    # Backend admin page anyway reloads on update

    def premium_update(self, data):
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

    def cancel(self, data):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        logger.info(text_data_json)
        type = text_data_json['type']
        if (type == "ticker_request"):
            self.send(json.dumps({
                'instruments': json.dumps(SymbolSerializer(Symbol.objects.filter(vendor_id__user_id=text_data_json['user']), many=True).data, cls=UUIDEncoder),
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
        self.send(text_data=json.dumps(data, cls=UUIDEncoder))

    def premium_update(self, data):
        logger.info(f"Premium has been updated for {data}")
