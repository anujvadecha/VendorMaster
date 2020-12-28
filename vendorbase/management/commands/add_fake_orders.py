from random import randint
from django.core.management import BaseCommand
from orderManagement.models import Order, OrderStatus, OrderType
# from order_engine.order_engine import OrderEngine
from userBase.models import NormalUser
from vendorbase.models import Symbol

class Command(BaseCommand):
    user='admin'
    help = 'Process to add fake orders for testing'
    def add_fake_orders(self,count=2000):
        for i in range(0,count):
            order=Order(user_id=NormalUser.objects.filter(username=self.user).first(),
                        instrument_id=Symbol.objects.first(),
                        quantity=randint(1, 200),
                        status=OrderStatus.WAITING_FOR_LIMIT,
                        type=OrderType.LIMIT,
                        price=randint(70000,80000))
            order.save()
            order=Order(user_id=NormalUser.objects.filter(username=self.user).first(),instrument_id=Symbol.objects.first(),quantity=randint(1, 200),status=OrderStatus.OPEN,
                  type=OrderType.LIMIT,price=randint(70000,80000))
            order.save()
            order=Order(user_id=NormalUser.objects.filter(username=self.user).first(),instrument_id=Symbol.objects.first(),quantity=randint(1, 200),status=OrderStatus.EXECUTED,
                  type=OrderType.LIMIT,price=randint(70000,80000))
            order.save()
            order=Order(user_id=NormalUser.objects.filter(username=self.user).first(),instrument_id=Symbol.objects.first(),quantity=randint(1, 200),status=OrderStatus.CLOSED,
                  type=OrderType.LIMIT,price=randint(70000,80000))
            order.save()
            order = Order(user_id=NormalUser.objects.filter(username=self.user).first(),
                          instrument_id = None, quantity=randint(1, 200), status=OrderStatus.WAITING_FOR_LIMIT,
                          type=OrderType.BEST_LIMIT , price=randint(70000, 80000))
            order.save()
    def handle(self, *args, **options):
            self.delete_all_orders()
            self.add_fake_orders(2)

    def delete_all_orders(self):
        Order.objects.all().delete()

