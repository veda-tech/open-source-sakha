from django.contrib.auth.models import AbstractUser

from core.models import AbstractModel


class User(AbstractModel, AbstractUser):
    pass
