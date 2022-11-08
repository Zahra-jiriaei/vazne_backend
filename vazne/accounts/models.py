from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    role_choice=(("Customer"),("Coach"))
    role = models.CharField(max_length=1, choices=role_choice)
    objects = CustomUserManager()

    def __str__(self):
        return self.email
