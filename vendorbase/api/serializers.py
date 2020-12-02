from rest_framework import serializers
from userBase.models import NormalUser
from vendorbase.models import Symbol, GlobalPremium, Vendor


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
    vendor=serializers.StringRelatedField()
    class Meta:
        model=Symbol
        fields="__all__"
        # exclude=("instrument_id","vendor_id")
class GlobalPremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model=GlobalPremium
        fields="__all__"
