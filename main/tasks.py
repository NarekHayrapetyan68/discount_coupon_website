from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from core.models import User
from .models import CartItem
from django.conf import settings

@shared_task
def send_cart_item_added_email(user_id, cart_item_id):
    user = User.objects.get(id=user_id)
    cart_item = CartItem.objects.get(id=cart_item_id)

    subject = 'Item added to your cart'
    body = render_to_string('cart/send_claim_email.html.html', {'user': user, 'cart_item': cart_item})
    from_email = settings.settings.EMAIL_HOST_USER
    to_email = [user.email]
    send_mail(subject, body, from_email, recipient_list=[to_email])

@shared_task
def send_cart_item_added_email(user_id):
    user = User.objects.get(id=user_id)

    subject = 'Item removed to from cart'
    body = render_to_string('cart/send_unclaim_email.html.html', {'user': user})
    from_email = settings.settings.EMAIL_HOST_USER
    to_email = [user.email]
    send_mail(subject, body, from_email, recipient_list=[to_email])
