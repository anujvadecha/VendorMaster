import json
from uuid import UUID
from django.core.cache import cache
from rest_framework import serializers
from admin_interface.models import Theme
from userBase.models import NormalUser, Support
from vendorbase.models import Symbol, GlobalPremium, Vendor, Favourite, VendorDetails, VendorMargin, VendorRatingText, \
    UserRating


# NormalUserSerializer
class NormalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalUser
        exclude = ('password',)


# class VendorRelatedField(serializers.RelatedField):
#     def to_representation(self, value):
#         if isinstance(value,Vendor):
#             serializer=VendorSerializer(value)
#         return serializer.data
class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = "__all__"


class VendorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorDetails
        fields = "__all__"


class VendorRatingTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorRatingText
        fields = "__all__"


class UserRatingTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRating
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    theme = serializers.SerializerMethodField()
    vendor_details = serializers.SerializerMethodField()

    def get_theme(self, obj):
        return json.dumps(ThemeSerializer(Theme.objects.filter(vendor=obj), many=True).data, cls=UUIDEncoder)

    def get_vendor_details(self, obj):
        return json.dumps(VendorDetailsSerializer(VendorDetails.objects.filter(vendor=obj), many=True).data,
                          cls=UUIDEncoder)

    class Meta:
        model = Vendor
        fields = [
            "user_id",
            "vendor_id",
            "enabled",
            "name",
            "address",
            "email",
            "company",
            "gst_in",
            "zip_code",
            "city",
            "company_card_image",
            "company_logo",
            "margin_available",
            "pancard_photo",
            "promoter_name",
            "reference_1",
            "reference_2",
            "theme",
            "vendor_details"
        ]


class SymbolSerializer(serializers.ModelSerializer):
    vendor = serializers.CharField(source="vendor_id.name")
    high = serializers.SerializerMethodField()
    low = serializers.SerializerMethodField()
    bid = serializers.SerializerMethodField()
    ask = serializers.SerializerMethodField()

    def get_high(self, obj):
        if (cache.get(obj.instrument_id) == None):
            return 0
        return cache.get(obj.instrument_id).get("high")

    def get_low(self, obj):
        if (cache.get(obj.instrument_id) == None):
            return 9999999
        return cache.get(obj.instrument_id).get("low")

    def get_bid(self, obj):
        if (cache.get(obj.instrument_id) == None):
            return 0
        return cache.get(obj.instrument_id).get("bid")

    def get_ask(self, obj):
        if (cache.get(obj.instrument_id) == None):
            return 0
        return cache.get(obj.instrument_id).get("ask")

    class Meta:
        model = Symbol
        fields = [
            "instrument_id", "vendor_id", "type", "name", "delivery_from", "delivery_to",
            "quantity", "source_symbol", "buy_premium", "sell_premium", "vendor", "high", "low", "bid", "ask",
            "enabled"]
        # exclude=("instrument_id","vendor_id")


class GlobalPremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalPremium
        fields = "__all__"


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = "__all__"


class UserMarginsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorMargin
        fields = "__all__"


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = "__all__"
