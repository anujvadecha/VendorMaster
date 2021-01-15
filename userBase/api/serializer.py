from rest_framework import serializers
from userBase.models import NormalUser


class ActivateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalUser
        fields='__all__'
        # fields = ['phone_number',
        #           'profile_picture',
        #           'pan_card',
        #           'business_card',
        #           'gst_in_no',
        #           'reference_1_name',
        #           'reference_1_mobile',
        #           'reference_2_name',
        #           'reference_2_mobile']