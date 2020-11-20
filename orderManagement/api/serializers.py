from rest_framework import serializers

from orderManagement.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        exclude=("order_id",)