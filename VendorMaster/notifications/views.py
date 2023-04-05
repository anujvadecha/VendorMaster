from django.shortcuts import render
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
import requests
from notifications.models import NotificationType, TemplateType
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

    subject = str(template_type)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user['email']]
    html_content = render_to_string(
        'email/' + str(template_type) + '.html', {'name': user['first_name'], 't_id': str(payload["transaction_id"]), 'otp': str(payload["otp"])})
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(
        subject, text_content, email_from, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_sms(user, payload, template_type):

    html_content = render_to_string(
        'sms/' + str(template_type) + '.html',
        {'name': user['first_name'], 't_id': str(payload["transaction_id"]), 'otp': str(payload["otp"]),'quantity':str(payload['quantity']),'price':str(payload['price'])})
    text_content = strip_tags(html_content)
    message = text_content
    numbers = [user['phone_number']]
    endpoint = 'https://swiftmediasms.com/api/pushsms.php?username=DeltaCap&password=9712&sender=BTIITI&message={message}&numbers={numbers}&unicode=false&flash=false'
    url = endpoint.format(message=message, numbers=numbers)
    response = requests.get(url)
    # if response.status_code == 200:  # SUCCESS
    #     pass
    # else:
    #     pass


def push_notifications(user, payload, template_type):
    pass
