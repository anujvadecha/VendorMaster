from rest_framework import serializers

from orderManagement.models import Order, OrderType, OrderStatus
import hashlib

from orderManagement.utils import otp_hash


class OrderSerializer(serializers.ModelSerializer):
    otp=serializers.SerializerMethodField()
    def get_otp(self,obj):
        if obj.status==OrderStatus.EXECUTED:
            return otp_hash(obj.order_id)
        else:
            return None
    class Meta:
        model=Order
        fields=[
        "order_id",
        "instrument_id",
        "quantity",
        "user_id",
        "price",
        "type",
        "status",
        "side",
        "otp"
        ]