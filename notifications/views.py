from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags


def send_email(user):
    print(user.email)

    '''
    subject = 'YOOOOOOO'
    message = f'Hi WimpyCat, your order has been confirmed.'
    html_content = render_to_string('templates/order_update.html')
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, email_from,
              recipient_list, html_message=html_content)
    '''
    subject = 'Order Confirmed'
    email_from = settings.EMAIL_HOST_USER

    recipient_list = [user.email]
    #text_content = 'This is an important message.'
    html_content = render_to_string('order_update.html', {'name': 'Hriim'})
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(
        subject, text_content, email_from, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
