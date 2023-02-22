from django.urls import path

from users.views import (
    logout_view,
    LoginPage,
    RegistrationPage,
    UserProfilePage,
)

urlpatterns = [
    path("logout", logout_view, name="users-logout"),
    path("login", LoginPage.as_view(), name="users-login"),
    path("registration", RegistrationPage.as_view(), name="users-registration"),
    path("profile", UserProfilePage.as_view(), name="users-profile"),
]
