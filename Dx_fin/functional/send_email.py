# send_email.py

from django.core.mail import send_mail
from django.conf import settings

def send_registration_email(email):
    subject = 'Добро пожаловать!'
    message = 'Спасибо за регистрацию!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
