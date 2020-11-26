from random import randint
import time

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.management import BaseCommand
from VendorMaster.consumers import TickConsumer


class Command(BaseCommand):
    help = 'Process to send gold ticker data'

    def handle(self, *args, **options):
        while True:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'ticker_group',
                {"type":"tick",
                 "gold_tick":
                {"bid": randint(40000, 60000),
                 "ask": randint(40000, 60000)
                 }
                }
            )
            time.sleep(0.5)

