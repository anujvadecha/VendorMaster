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
    # user = models.OneToOneField(User,on_delete=models.CASCADE,default=User.objects.first())
    # phone_number=models.CharField(blank=True,max_length=14)
    # profile_picture=models.ImageField(blank=True)
    # is_validated=models.BooleanField(default=False)
    # pan_card=models.ImageField(blank=True)


