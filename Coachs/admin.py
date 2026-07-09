from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import  CoachText
from accounts.models import CustomUser

#admin.site.register(CustomUser)
admin.site.register(CoachText)
