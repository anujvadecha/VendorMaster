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
    enabled = models.BooleanField(default=True)
    phone_number = models.CharField(blank=True, max_length=14)
    profile_picture = models.ImageField(blank=True)
    pan_card = models.ImageField(blank=True)

    # is_activated=models.BooleanField(blank=True,default=False)
    def get_phone_number(self):
        return self.phone_number


class Support(BaseModel):
    user_id = models.ForeignKey(NormalUser,on_delete=models.DO_NOTHING, null=True)
    username = models.CharField(max_length=200,null=True,blank=True)
    message = models.TextField(null=True,blank=True)
