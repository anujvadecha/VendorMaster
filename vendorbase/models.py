import uuid as uuid
from django.db import models

# Create your models here.
from djchoices import DjangoChoices, ChoiceItem

from base.models import BaseModel


class GlobalPremium(BaseModel):
    buy_premium = models.FloatField(max_length=100)
    sell_premium = models.FloatField(max_length=100)

class SymbolName(DjangoChoices):
    gold_999 = ChoiceItem("gold 999")
    gold_999_1kg = ChoiceItem("gold 999 1kg")
    gold_995 = ChoiceItem("gold 995")
    gold_995_1kg = ChoiceItem("gold 995 1kg")
    gold_999_t_plus_1 = ChoiceItem("gold 999 (T+1)")
    gold_999_1kg_t_plus_1 = ChoiceItem("gold 999 1kg (T+1)")
    gold_995_t_plus_1 = ChoiceItem("gold 995 (T+1)")
    gold_995_1kg_t_plus_1 = ChoiceItem("gold 995 1kg (T+1)")
    gold_999_t_plus_2 = ChoiceItem("gold 999 (T+2)")
    gold_999_1kg_t_plus_2 = ChoiceItem("gold 999 1kg (T+2)")
    gold_995_t_plus_2 = ChoiceItem("gold 995 (T+2)")
    gold_995_1kg_t_plus_2 = ChoiceItem("gold 995 1kg (T+2)")


class SymbolType(DjangoChoices):
    gold_999 = ChoiceItem("gold 999")
    gold_999_1kg = ChoiceItem("gold 999 1kg")
    gold_995 = ChoiceItem("gold 995")
    gold_995_1kg = ChoiceItem("gold 995 1kg")



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

class SourceSymbol(DjangoChoices):
        gold_fut = ChoiceItem("gold_fut")
        gold_bank=ChoiceItem("gold_bank")

class Symbol(BaseModel):
    instrument_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)
    type = models.CharField(max_length=200,  choices=SymbolType.choices, default=SymbolType.gold_999)
    name = models.CharField(max_length=500 , choices=SymbolType)
    delivery_from = models.DateField()
    delivery_to = models.DateField()
    quantity = models.CharField(max_length=200)
    source_symbol = models.CharField(max_length=200,choices=SourceSymbol)
    buy_premium = models.FloatField()
    sell_premium = models.FloatField()


    def get_bid_price_from_tick(self,tick):
        return self.buy_premium+tick["bid"]+GlobalPremium.objects.first().buy_premium

    def get_sell_price_from_tick(self,tick):
        return self.sell_premium + tick["ask"]+GlobalPremium.objects.first().sell_premium

    def __str__(self):
        return self.name.__str__();
