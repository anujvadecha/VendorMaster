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
    class Meta:
        model=Symbol
        fields=[
            "instrument_id","vendor_id","type","name","delivery_from","delivery_to",
        "quantity","source_symbol","buy_premium","sell_premium","vendor"]
        # exclude=("instrument_id","vendor_id")
class GlobalPremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model=GlobalPremium
        fields="__all__"
