from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_email_task(subject, body, email):
    print('---------------------------------------')
    send_mail(subject, body, from_email=settings.EMAIL_HOST_USER, recipient_list=[email])
    print('---------------------------------------')
