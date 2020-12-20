import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from VendorMaster import settings
from VendorMaster.consumers import UUIDEncoder
from admin_interface.models import Theme
from orderManagement.api.serializers import OrderSerializer
from orderManagement.models import Order, LimitOrderPending, OpenOrder, ExecutedOrder, ClosedOrder, OrderStatus, \
    OrderType
from userBase.models import NormalUser
from vendorbase.api.serializers import SymbolSerializer
from vendorbase.models import Symbol, Vendor, VendorDetails, VendorMargin
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
    async_to_sync(channel_layer.group_send)(
        settings.SOCKET_GROUP,
        {
            "type": "order_update",
            "user": instance.user_id.id,
            "order_update": json.dumps(OrderSerializer(instance).data,cls=UUIDEncoder)
        }
    )

@receiver(post_save,sender=Vendor)
def create_vendor_info_objects(sender, instance, created, **kwargs):
    if created:
        VendorDetails.objects.create(vendor=instance)
        Theme.objects.create(vendor=instance,name=instance.name,title=instance.name)
    #if created:
    #   NormalUser.objects.create(user=instance)

@receiver(post_save,sender=NormalUser)
def user_created_updated(sender, instance, created, **kwargs):
    if created:
        for vendor in Vendor.objects.all():
            VendorMargin.objects.create(
                user=instance,vendor=vendor,
                margin=vendor.default_margin,margin_available=vendor.default_margin
            )
