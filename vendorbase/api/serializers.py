from django.core.cache import cache
from rest_framework import serializers
from userBase.models import NormalUser
from vendorbase.models import Symbol, GlobalPremium, Vendor

#NormalUserSerializer
class NormalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=NormalUser
        fields="__all__"

class VendorRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value,Vendor):
            serializer=VendorSerializer(value)
        return serializer.data

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields="__all__"

class SymbolSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(source="vendor_id")
    high = serializers.SerializerMethodField()
    low = serializers.SerializerMethodField()
    bid = serializers.SerializerMethodField()
    ask = serializers.SerializerMethodField()
    def get_high(self,obj):
        return cache.get(obj.instrument_id).get("high")
    def get_low(self,obj):
        return cache.get(obj.instrument_id).get("low")
    def get_bid(self,obj):
        return cache.get(obj.instrument_id).get("bid")
    def get_ask(self, obj):
        return cache.get(obj.instrument_id).get("ask")
    class Meta:
        model=Symbol
        fields=[
            "instrument_id","vendor_id","type","name","delivery_from","delivery_to",
        "quantity","source_symbol","buy_premium","sell_premium","vendor","high","low","bid","ask"]
        # exclude=("instrument_id","vendor_id")
class GlobalPremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model=GlobalPremium
        fields="__all__"
