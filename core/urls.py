from django.urls import path
from .views import EmailView, LoginView, RegistrationView

app_name = "core"
urlpatterns = [
    path("send-simple-email/", EmailView.as_view(), name="simple_email"),
    path("login/", LoginView.as_view(), name="login"),
    path("registration/", RegistrationView.as_view(), name="registration")
]
