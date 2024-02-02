from django.urls import path
from .views import PaymentView, create_checkout_session, SuccessView, CancelView

app_name = 'payment'

urlpatterns = [
    path("", PaymentView.as_view(), name='payment_detail'),
    path("create-checkout-session/<int:pk>/", create_checkout_session, name="create_checkout_session"),
    path("success/", SuccessView.as_view(), name="success"),
    path("cancel/", CancelView.as_view(), name="cancel"),
]