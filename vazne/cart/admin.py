
from django.contrib import admin
from .models import  Cart, DeliveryCost
from accounts.models import CustomUser

#admin.site.register(CustomUser)
admin.site.register(Cart)
admin.site.register(DeliveryCost)
