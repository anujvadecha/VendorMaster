import uuid as uuid

from django.core.cache import cache
from django.db import models

# Create your models here.
from django.forms import model_to_dict
from djchoices import DjangoChoices, ChoiceItem

from base.models import BaseModel
from userBase.models import NormalUser


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
    user_id = models.ForeignKey(NormalUser, blank=True, on_delete=models.CASCADE,)
    vendor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    enabled = models.BooleanField(default=True)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    company = models.CharField(max_length=500)
    gst_in = models.CharField(max_length=500)
    zip_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200, blank=True)
    company_card_image = models.ImageField(blank=True)
    company_logo = models.ImageField(blank=True)
    margin_available = models.FloatField(blank=True, max_length=200, default=0)
    pancard_photo = models.ImageField(blank=True)
    promoter_name = models.CharField(max_length=200, blank=True)
    reference_1 = models.CharField(max_length=500, blank=True)
    reference_2 = models.CharField(max_length=500, blank=True)
    # phone_number=models.CharField(max_length=12,blank=True)
    def __str__(self):
        return self.name.__str__();


class VendorDetails(BaseModel):
    vendor=models.ForeignKey(Vendor,on_delete=models.DO_NOTHING,null=True)
    contact_details=models.TextField()
    office_address=models.TextField(blank=True)
    collection_address=models.TextField(blank=True)
    mobile_number_1=models.CharField(max_length=13,blank=True)
    mobile_number_2=models.CharField(max_length=13,blank=True)
    bank_details=models.TextField(blank=True)
    gst_details=models.TextField(blank=True)
    about_us=models.TextField(blank=True)
    messages=models.TextField(blank=True)
    delivery_charges=models.TextField(blank=True)

class BankDetails(BaseModel):
    vendor = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING)
    bank_name = models.CharField(max_length=200)
    account_number = models.CharField(max_length=200)
    ifsc_code = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)

    def __str__(self):
        return self.vendor.name


class City(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name.__str__()


class Group(BaseModel):
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    group_buy_premium = models.FloatField(max_length=100)
    group_sell_premium = models.FloatField(max_length=100)
    name = models.CharField(max_length=100)
    cities = models.ManyToManyField(City)

    def __str__(self):
        return self.name.__str__()


class SourceSymbol(DjangoChoices):
    gold_fut = ChoiceItem("gold_fut")
    gold_bank = ChoiceItem("gold_bank")


class Symbol(BaseModel):
    instrument_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)
    type = models.CharField(max_length=200, choices=SymbolType.choices, default=SymbolType.gold_999)
    name = models.CharField(max_length=500, choices=SymbolName)
    delivery_from = models.DateField()
    delivery_to = models.DateField()
    quantity = models.CharField(max_length=200)
    source_symbol = models.CharField(max_length=200, choices=SourceSymbol)
    buy_premium = models.FloatField()
    sell_premium = models.FloatField()

    # def get_bid_price_from_tick(self,tick):
    #     return self.buy_premium+tick["bid"]+GlobalPremium.objects.first().buy_premium
    #
    # def get_sell_price_from_tick(self,tick):
    #     return self.sell_premium + tick["ask"]+GlobalPremium.objects.first().sell_premium

    def __str__(self):
        return str(self.name)+"_"+str(self.vendor_id);

    @classmethod
    def update_cache(cls):
        print("updating cache for all instruments")
        cache.set("instruments", list(Symbol.objects.all()))
        print("updating cache for each instrument")
        for symbol in Symbol.objects.all():
            to_store = {}
            to_store["high"] = 0
            to_store["low"] = 999999999
            to_store["bid"] = 0
            to_store["ask"] = 0
            cache.set(symbol.instrument_id, to_store)


class Favourite(models.Model):
    user_id = models.ForeignKey(NormalUser, on_delete=models.DO_NOTHING)
    instrument_id = models.ForeignKey(Symbol, on_delete=models.DO_NOTHING)
