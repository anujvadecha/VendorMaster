from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from vendorbase.api.serializers import SymbolSerializer
from vendorbase.models import Symbol

@receiver(post_save,sender=Symbol)
def create_update_symbol(sender,instance,created,**kwargs):
    channel_layer=get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'ticker_group',
        {
            "type": "premium_update",
            "symbol":SymbolSerializer(instance).data
         }
    )
    # if created:
    #     NormalUser.objects.create(user=instance)
