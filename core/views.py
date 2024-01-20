from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth.views import LoginView as Login
from django.conf import settings
from .forms import EmailForm, RegistrationForm
from django.contrib.auth import get_user_model

from .generate_token import account_activation_token

User = get_user_model()


class EmailView(FormView):
    template_name = "core/send_simple_email.html"
    form_class = EmailForm
    success_url = "/"

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        body = form.cleaned_data['body']
        send_mail(subject, body, from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[email])
        return response


class RegistrationView(CreateView):
    form_class = RegistrationForm
    model = User
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        subject = "Authenticate your Profile"
        user = self.object
        user.is_active = False
        user.save()
        token = account_activation_token.make_token(user)
        message = render_to_string("core/authentication.html",
                                   {"user": user,
                                    "domain": get_current_site(self.request),
                                    "token": token})
        email = EmailMessage(subject=subject, body=message,
                             from_email=settings.EMAIL_HOST_USER,
                             to=[user.email])
        email.send(fail_silently=False)

        return response


class LoginView(Login):
    pass
