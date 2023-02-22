from django import forms

from users.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
