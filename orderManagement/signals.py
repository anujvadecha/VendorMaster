import json

from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver
from VendorMaster import settings
from VendorMaster.consumers import UUIDEncoder
from orderManagement.api.serializers import OrderSerializer
from orderManagement.models import Order, OrderStatus, OrderType, LimitOrderPending, OpenOrder, ExecutedOrder, \
    ClosedOrder

# @receiver(post_save,sender=Order)
# def create_order(sender,instance,created,**kwargs):
#     print(" order update received ")
    # if instance.type==OrderType.LIMIT and instance.status==OrderStatus.WAITING_FOR_LIMIT:
    #     OrderEngine.getInstance().add_order(instance)
    # channel_layer=get_channel_layer()
    # async_to_sync(channel_layer.group_send)(
    #     settings.SOCKET_GROUP,
    #     {
    #         "type": "order_update",
    #         "order":OrderSerializer(instance).data
    #      }
    # )
    # if created:
    #     NormalUser.objects.create(user=instance)





