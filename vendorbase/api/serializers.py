from rest_framework import serializers
from userBase.models import NormalUser
from vendorbase.models import Symbol, GlobalPremium


class NormalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=NormalUser
        fields="__all__"

class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model=Symbol
        fields="__all__"
        # exclude=("instrument_id","vendor_id")
class GlobalPremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model=GlobalPremium
        fields="__all__"
