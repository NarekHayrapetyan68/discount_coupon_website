from django.urls import path
from .views import EmailView, LoginView, RegistrationView, ValidateUserLink, LogoutView

app_name = "core"
urlpatterns = [
    path("send-simple-email/", EmailView.as_view(), name="simple_email"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("<int:pk>/<str:token>/", ValidateUserLink.as_view(), name="verify"),
]
