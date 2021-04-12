from rest_framework import serializers

from orderManagement.models import Order, OrderType, OrderStatus
import hashlib

from orderManagement.utils import otp_hash


class OrderSerializer(serializers.ModelSerializer):

    otp=serializers.SerializerMethodField()
    name=serializers.SerializerMethodField()
    def get_name(self,obj):
        if(obj.type==OrderType.BEST_LIMIT):
            return ''
        else:
            return obj.instrument_id.name

    def get_otp(self,obj):
        if obj.status == OrderStatus.EXECUTED:
            return otp_hash(obj.order_id)
        else:
            return None

    class Meta:
        model = Order
        fields=["created_at","modified_at","order_id",
        "instrument_id",'transaction_id',"quantity",
        "user_id","price","type",
        "status","side","otp","name","best_limit_id", "is_rated","comments"]
