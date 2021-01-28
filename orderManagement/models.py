import uuid
from django.db import models
from djchoices import DjangoChoices, ChoiceItem
from base.models import BaseModel
from orderManagement.utils import unique_transaction_id_generator
from userBase.models import NormalUser
from vendorbase.models import Vendor, Symbol


class OrderType(DjangoChoices):
    MARKET = ChoiceItem("MARKET")
    LIMIT = ChoiceItem("LIMIT")
    BEST_LIMIT = ChoiceItem("BEST_LIMIT")


class OrderStatus(DjangoChoices):
    OPEN = ChoiceItem("OPEN")
    EXECUTED = ChoiceItem("EXECUTED")
    CLOSED = ChoiceItem("CLOSED")
    CANCELLED = ChoiceItem("CANCELLED")
    WAITING_FOR_LIMIT = ChoiceItem("WAITING_FOR_LIMIT")
    BEST_LIMIT = ChoiceItem("BEST_LIMIT")


class OrderSide(DjangoChoices):
    BUY = ChoiceItem("BUY")
    SELL = ChoiceItem("SELL")


class BestLimitUserMapping(BaseModel):
    user = models.ForeignKey(NormalUser, on_delete=models.DO_NOTHING)
    best_limit_id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.user.username


class Order(BaseModel):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction_id = models.CharField(max_length=120, default=unique_transaction_id_generator, blank=True,
                                      editable=False)
    instrument_id = models.ForeignKey(Symbol, null=True, on_delete=models.DO_NOTHING, blank=True)
    quantity = models.IntegerField()
    user_id = models.ForeignKey(NormalUser, on_delete=models.DO_NOTHING, blank=True)
    price = models.FloatField(max_length=200)
    type = models.CharField(max_length=200, choices=OrderType, default=OrderType.MARKET)
    status = models.CharField(max_length=100, choices=OrderStatus, default=OrderStatus.OPEN)
    side = models.CharField(default=OrderSide.BUY, max_length=200, choices=OrderSide)
    best_limit_id = models.ForeignKey(BestLimitUserMapping, on_delete=models.DO_NOTHING,null=True,blank=True)
    is_rated = models.BooleanField(default=False)

    def vendor(self):
        return self.instrument_id.vendor_id

    def __str__(self):
        return self.user_id.__str__();

    class Meta:
        indexes = [
            models.Index(fields=['user_id']),
            models.Index(fields=['status']),
            models.Index(fields=['user_id','status']),
            models.Index(fields=['status','type']),
        ]


class OpenOrder(Order):
    class Meta:
        proxy = True


class ClosedOrder(Order):
    class Meta:
        proxy = True


class ExecutedOrder(Order):
    class Meta:
        proxy = True


class LimitOrderPending(Order):
    class Meta:
        proxy = True


class BestLimitOrder(Order):
    class Meta:
        proxy = True
