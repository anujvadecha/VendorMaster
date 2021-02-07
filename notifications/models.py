from django.db import models
from djchoices import DjangoChoices, ChoiceItem

# Create your models here.


class NotificationType(DjangoChoices):
    MAIL = ChoiceItem("MAIL")
    SMS = ChoiceItem("SMS")
    PUSH_NOTIFICATION = ChoiceItem("PUSH_NOTIFICATION")

class TemplateType(DjangoChoices):
    ORDER_PLACED = ChoiceItem("ORDER_PLACED")
    ORDER_CONFIRMED = ChoiceItem("ORDER_CONFIRMED")
    ORDER_CANCELLED = ChoiceItem("ORDER_CANCELLED")