from django.contrib import admin

# Register your models here.

# Register your models here.
from django.contrib import admin
from .models import  *

from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Comment)
