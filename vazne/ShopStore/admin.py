from django.contrib import admin 
from .models import Product , Comment
from django.contrib.auth.models import Group

admin.site.register(Product)  
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name')

# admin.site.register(Category)
admin.site.register(Comment)
admin.site.unregister(Group)
admin.site.site_header = "Vazne Admin"

