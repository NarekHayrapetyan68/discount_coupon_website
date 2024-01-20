from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea())


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email", "password1", "password2")
