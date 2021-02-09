from django.db import models
from djchoices import DjangoChoices, ChoiceItem

# Create your models here.


class NotificationType(DjangoChoices):
    MAIL = ChoiceItem("MAIL")
    SMS = ChoiceItem("SMS")
    PUSH_NOTIFICATION = ChoiceItem("PUSH_NOTIFICATION")


class TemplateType(DjangoChoices):
    ORDER_CANCELLED = ChoiceItem("ORDER_CANCELLED")
    ORDER_OPEN = ChoiceItem("ORDER_OPEN")
    ORDER_EXECUTED = ChoiceItem("ORDER_EXECUTED")
    ORDER_WAITING_FOR_LIMIT = ChoiceItem("ORDER_WAITING_FOR_LIMIT")
