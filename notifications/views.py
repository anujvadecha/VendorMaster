from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


def send_email(user):
    print(user.email)
    print("Hello shuttler")
    subject = 'YOOOOOOO'
    message = f'Hi WimpyCat, thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, email_from, recipient_list)
    print("Hello wimpycat")
