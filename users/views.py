from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import FormView, DetailView

from users.forms import RegistrationForm, LoginForm
from users.models import User


def logout_view(request):
    logout(request)
    return redirect("/")


class LoginPage(FormView):
    form_class = LoginForm
    template_name = "users/login.html"

    def form_valid(self, form):
        user = User.objects.filter(username=form.cleaned_data["username"]).first()
        if user is None:
            return super().get(self.request)
        if user.check_password(form.cleaned_data["password"]):
            login(self.request, user)
            return redirect("/")
        else:
            return super().get(self.request)


class RegistrationPage(FormView):
    form_class = RegistrationForm
    template_name = "users/registration.html"

    def get_success_url(self):
        return "/"

    def form_valid(self, form):
        username, password = (
            form.cleaned_data["username"].lower(),
            form.cleaned_data["username"],
        )
        if User.objects.filter(username=username).exists():
            form.add_error("username", "Такой пользователь уже существует")
            return super().form_invalid(form)
        user = User(username=username)
        user.set_password(password)
        user.save()
        return super().form_valid(form)


class UserProfilePage(LoginRequiredMixin, DetailView):
    template_name = "users/profile.html"

    def get_object(self, queryset=None):
        return self.request.user
