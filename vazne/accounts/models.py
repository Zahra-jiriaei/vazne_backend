from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

from .managers import CustomUserManager

class CustomUser(User):
    role_choice=(("Customer"),("Coach"))
    role = models.CharField(max_length=1, choices=role_choice)
    objects = CustomUserManager()

