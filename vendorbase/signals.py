import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from VendorMaster import settings
from VendorMaster.consumers import UUIDEncoder
from orderManagement.api.serializers import OrderSerializer
from orderManagement.models import Order, LimitOrderPending, OpenOrder, ExecutedOrder, ClosedOrder, OrderStatus, \
    OrderType
from vendorbase.api.serializers import SymbolSerializer
from vendorbase.models import Symbol
from django.core.cache import cache

@receiver(post_save,sender=Symbol)
def create_update_symbol(sender,instance,created,**kwargs):
    print("symbol update")
    channel_layer=get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        settings.SOCKET_GROUP,
        {
            "type": "instrument_update",
            "instrument_update":json.dumps(SymbolSerializer(instance).data,cls=UUIDEncoder)
         }
    )

@receiver(post_save, sender=Order)
@receiver(post_save, sender=LimitOrderPending)
@receiver(post_save, sender=OpenOrder)
@receiver(post_save, sender=ExecutedOrder)
@receiver(post_save, sender=ClosedOrder)
def create_update_order(sender, instance, created, **kwargs):
    print("order update received from orderManagement")
    channel_layer = get_channel_layer()
    # if instance.status == OrderStatus.WAITING_FOR_LIMIT and instance.type == OrderType.LIMIT:
    async_to_sync(channel_layer.group_send)(
        settings.SOCKET_GROUP,
        {
            "type": "order_update",
            "user": instance.user_id.id,
            "order_update": json.dumps(OrderSerializer(instance).data,cls=UUIDEncoder)
        }
    )

    # if created:
    #     NormalUser.objects.create(user=instance)
