from random import randint
import time
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
        while True:
            tick={
                    "type":"tick",
                    "gold_tick":
                    {
                        "bid": randint(40000, 60000),
                        "ask": randint(40000, 60000)
                    }
                }
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                settings.SOCKET_GROUP,
                tick
            )
            update_high_low.delay(tick)
            time.sleep(1)
