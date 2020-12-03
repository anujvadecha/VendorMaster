from django.contrib.auth.models import User, AbstractUser
from django.db import models
from djchoices import DjangoChoices, ChoiceItem
from phone_field import PhoneField
from phonenumber_field.formfields import PhoneNumberField
from base.models import BaseModel

class UserType(DjangoChoices):
    user=ChoiceItem("USER")
    vendor=ChoiceItem("VENDOR")

class NormalUser(AbstractUser):
    enabled = models.BooleanField(default=True)
    phone_number = models.CharField(blank=True,max_length=14)
    profile_picture = models.ImageField(blank=True)
    pan_card = models.ImageField(blank=True)
    def get_phone_number(self):
        return self.phone_number

