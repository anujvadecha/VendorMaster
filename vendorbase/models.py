import uuid as uuid
from django.db import models

# Create your models here.
from djchoices import DjangoChoices, ChoiceItem

from base.models import BaseModel


class GlobalPremium(BaseModel):
    buy_premium = models.FloatField(max_length=100)
    sell_premium = models.FloatField(max_length=100)

class SymbolType(DjangoChoices):
    gold = ChoiceItem("gold")
    silver = ChoiceItem("silver")
    other = ChoiceItem("other")

class Vendor(BaseModel):
    vendor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    enabled = models.BooleanField(default=True)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    company = models.CharField(max_length=500)
    gst_in = models.CharField(max_length=500)
    zip_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    company_card_image = models.ImageField()
    def __str__(self):
        return self.name.__str__();

class City(BaseModel):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name.__str__()

class Group(BaseModel):
    vendor_id = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    group_buy_premium = models.FloatField(max_length=100)
    group_sell_premium = models.FloatField(max_length=100)
    name = models.CharField(max_length=100)
    cities=models.ManyToManyField(City)
    def __str__(self):
        return self.name.__str__()

class Symbol(BaseModel):
    instrument_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)
    name = models.CharField(max_length=500)
    delivery_from = models.DateField()
    delivery_to = models.DateField()
    quantity = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=SymbolType.choices, default=SymbolType.gold)
    source_symbol = models.CharField(max_length=200)
    buy_premium = models.FloatField()
    sell_premium = models.FloatField()
    def __str__(self):
        return self.name.__str__();
