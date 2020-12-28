from rest_framework import serializers
from userBase.models import NormalUser

class ActivateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalUser
        fields = "__all__"
