from django.contrib.auth.models import User
from django.db import models
from djchoices import DjangoChoices, ChoiceItem
from phone_field import PhoneField
from phonenumber_field.formfields import PhoneNumberField

from base.models import BaseModel

class UserType(DjangoChoices):
    user=ChoiceItem("USER")
    vendor=ChoiceItem("VENDOR")

class NormalUser(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=User.objects.first())
    enabled=models.BooleanField(default=True)
    phone_number=models.CharField(blank=True,max_length=14)
    profile_picture=models.ImageField(blank=True)
    def __str__(self):
        return self.user.username
