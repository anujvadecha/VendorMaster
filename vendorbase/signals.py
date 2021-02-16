import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import logging
from VendorMaster import settings
from VendorMaster.consumers import UUIDEncoder
from admin_interface.models import Theme
from orderManagement.api.serializers import OrderSerializer
from orderManagement.models import Order, LimitOrderPending, OpenOrder, ExecutedOrder, ClosedOrder, OrderStatus, OrderType
from userBase.models import NormalUser
from vendorbase.api.serializers import SymbolSerializer, NormalUserSerializer
from vendorbase.models import Symbol, Vendor, VendorDetails, VendorMargin
from django.core.cache import cache
from notifications.views import notifications
from notifications.models import NotificationType, TemplateType

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Symbol)
def create_update_symbol(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        settings.SOCKET_GROUP,
        {
            "type": "instrument_update",
            "instrument_update": json.dumps(SymbolSerializer(instance).data, cls=UUIDEncoder)
        }
    )


@receiver(post_save, sender=Order)
@receiver(post_save, sender=LimitOrderPending)
@receiver(post_save, sender=OpenOrder)
@receiver(post_save, sender=ExecutedOrder)
@receiver(post_save, sender=ClosedOrder)
def create_update_order(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        settings.SOCKET_GROUP,
        {
            "type": "order_update",
            "user": instance.user_id.id,
            "order_update": json.dumps(OrderSerializer(instance).data, cls=UUIDEncoder)
        }
    )

    user = NormalUser.objects.filter(id=instance.user_id.id).first()
    payload = OrderSerializer(instance).data

    if(instance.status == OrderStatus.CANCELLED):
        notifications.delay([NotificationType.MAIL, NotificationType.SMS], user, payload,
                            TemplateType.ORDER_CANCELLED)
        async_to_sync(channel_layer.group_send)(
            settings.SOCKET_GROUP, {
                "type": "cancel",
                "cancelled": json.dumps(OrderSerializer(instance).data, cls=UUIDEncoder)
            }
        )
    if instance.status == OrderStatus.OPEN:
        notifications.delay([NotificationType.MAIL, NotificationType.SMS], NormalUserSerializer(user).data, payload,
                            TemplateType.ORDER_OPEN)
        instrument = instance.instrument_id
        margin_object = VendorMargin.objects.filter(
            user=instance.user_id, vendor_id=instrument.vendor_id).first()
        if (margin_object == None):
            logger.error('MARGIN FOR THE INSTANCE DOES NOT EXIST')
        if (margin_object.margin_available >= instance.quantity):
            logger.info(
                f"Margin available is {margin_object.margin_available} order quantity {instance.quantity}")
            margin_object.margin_available = margin_object.margin_available - instance.quantity
            margin_object.save()
            return True
        else:
            return False
    if instance.status == OrderStatus.EXECUTED:
        notifications.delay([NotificationType.MAIL, NotificationType.SMS], NormalUserSerializer(user).data, payload,
                            TemplateType.ORDER_EXECUTED)
    if instance.status == OrderStatus.WAITING_FOR_LIMIT:
        notifications.delay([NotificationType.MAIL, NotificationType.SMS], NormalUserSerializer(user).data, payload,
                            TemplateType.ORDER_WAITING_FOR_LIMIT)


@receiver(pre_save, sender=Order)
@receiver(pre_save, sender=LimitOrderPending)
@receiver(pre_save, sender=OpenOrder)
@receiver(pre_save, sender=ExecutedOrder)
@receiver(pre_save, sender=ClosedOrder)
def pre_save_order(sender, instance, *args, **kwargs):
    pass


@receiver(post_save, sender=Vendor)
def create_vendor_info_objects(sender, instance, created, **kwargs):
    if created:
        VendorDetails.objects.create(vendor=instance)
        Theme.objects.create(
            vendor=instance, name=instance.name, title=instance.name)
        for user in NormalUser.objects.all():
            if user.is_activated and not user.is_staff:
                VendorMargin.objects.create(
                    user=user, vendor=instance,
                    margin=instance.default_margin, margin_available=instance.default_margin
                )


@receiver(post_save, sender=NormalUser)
def user_created_updated(sender, instance, created, **kwargs):
    logger.info(f" Updating Normal User ")
    for vendor in Vendor.objects.all():
        if instance.is_activated:
            object = VendorMargin.objects.filter(
                user=instance, vendor=vendor).first()
            if object == None:
                logger.info(
                    f" Creating vendor margin object for {instance} vendor {vendor} ")
                VendorMargin.objects.create(
                    user=instance, vendor=vendor,
                    margin=vendor.default_margin, margin_available=vendor.default_margin
                )
