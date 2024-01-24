from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth.views import LoginView as Login
from django.contrib.auth.views import LogoutView as Logout
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
    template_name = "core/user_form.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        subject = "Authenticate your Profile"
        user = self.object
        user.is_active = False
        user.save()
        token = account_activation_token.make_token(user)
        current_site = get_current_site(self.request)
        message = render_to_string("core/authentication.html",
                                   {"user": user,
                                    "domain": current_site.domain,
                                    "token": token})
        email = EmailMessage(subject=subject, body=message,
                             from_email=settings.EMAIL_HOST_USER,
                             to=[user.email])
        email.send(fail_silently=False)

        return response


class ValidateUserLink(TemplateView):

    def get(self, request, *args, **kwargs):
        token = kwargs.get("token")
        pk = kwargs.get("pk")
        user = User.objects.get(pk=pk)
        if account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect("core:login")
        return HttpResponse("Your token is invalid")


class LoginView(Login):
    template_name = 'user/login.html'


class LogoutView(Logout):
    pass

