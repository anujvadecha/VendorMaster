import uuid

from django.db import models
from djchoices import DjangoChoices, ChoiceItem
from base.models import BaseModel
from userBase.models import NormalUser
from vendorbase.models import Vendor, Symbol

class OrderType(DjangoChoices):
    MARKET = ChoiceItem("MARKET")
    LIMIT = ChoiceItem("LIMIT")

class OrderStatus(DjangoChoices):
    OPEN=ChoiceItem("OPEN")
    EXECUTED=ChoiceItem("EXECUTED")
    CLOSED=ChoiceItem("CLOSED")
    CANCELLED=ChoiceItem("CANCELLED")

class OrderSide(DjangoChoices):
    BUY=ChoiceItem("BUY")
    SELL=ChoiceItem("SELL")

class Order(BaseModel):
    order_id  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    instrument_id = models.ForeignKey(Symbol,on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    user_id = models.ForeignKey(NormalUser,on_delete=models.DO_NOTHING,blank=True)
    price = models.FloatField(max_length=200)
    type = models.CharField(max_length=200, choices=OrderType, default=OrderType.MARKET)
    status  =   models.CharField(max_length=100,choices=OrderStatus,default=OrderStatus.OPEN)
    side = models.CharField( default=OrderSide.BUY,max_length=200 ,choices=OrderSide)
    def __str__(self):
        return self.user_id.__str__();


class OpenOrder(Order):
    class Meta:
        proxy = True

class ClosedOrder(Order):
    class Meta:
        proxy=True

class ExecutedOrder(Order):
    class Meta:
        proxy=True