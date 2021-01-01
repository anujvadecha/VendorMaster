from django.contrib.auth.models import User, AbstractUser
from django.db import models
from djchoices import DjangoChoices, ChoiceItem
from phone_field import PhoneField
from phonenumber_field.formfields import PhoneNumberField
from base.models import BaseModel

class UserType(DjangoChoices):
    user = ChoiceItem("USER")
    vendor = ChoiceItem("VENDOR")


class NormalUser(AbstractUser):
    requested_registration = models.BooleanField(default = False)
    phone_number = models.CharField( blank=True , max_length=14 )
    profile_picture = models.ImageField( blank=True )
    pan_card = models.ImageField( blank=True )
    business_card = models.ImageField( blank=True )
    is_activated = models.BooleanField(default=False)
    gst_in_no = models.CharField(max_length=200, blank=True)
    reference_1_name = models.CharField(max_length=200, blank=True,help_text="Please input name and number of any reference we can verify")
    reference_1_mobile = models.CharField(max_length=200, blank=True)
    reference_2_name = models.CharField(max_length=200, blank=True,help_text="Please input name and number of any reference we can verify")
    reference_2_mobile = models.CharField(max_length=200, blank=True)


class Support(BaseModel):
    user_id = models.ForeignKey(NormalUser, on_delete=models.DO_NOTHING, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
