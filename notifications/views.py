from django.shortcuts import render
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
import requests
from notifications.models import NotificationType
from vendorbase.celery import app


@app.task
def notifications(type, userdata, payload, template):
    for t in type:
        if t == NotificationType.MAIL:
            send_email(userdata, payload, template)
        elif t == NotificationType.SMS:
            send_sms(userdata, payload, template)
        elif t == NotificationType.PUSH_NOTIFICATION:
            push_notifications(userdata)


def send_email(user, payload, template_type):
    print(user.email)

    subject = 'Order Confirmed'
    email_from = settings.EMAIL_HOST_USER

    recipient_list = [user.email]
    html_content = render_to_string(
        str(template_type) + '.html', {'name': user.first_name})
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(
        subject, text_content, email_from, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_sms(user, payload, template_type):
    message = "This is my sms test msg"
    numbers = [user.phone_number]
    endpoint = 'https://swiftmediasms.com/api/pushsms.php?username=DeltaCap&password=9712&sender=BLKsMs&message={message}&numbers={number}&unicode=false&flash=false'
    url = endpoint.format(message=message, numbers=numbers)
    headers = {'api_key': settings.SMS_API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:  # SUCCESS
        pass
    else:
        pass


def push_notifications(user, payload, template_type):
    pass
