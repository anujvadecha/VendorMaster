from rest_framework import serializers
from userBase.models import NormalUser


class NormalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=NormalUser
        exclude=("is_validated",)
