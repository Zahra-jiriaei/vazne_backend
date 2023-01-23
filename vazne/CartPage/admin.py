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
admin.site.register(Cart)
admin.site.register(Cartitems)

"""class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(Cartitems)

class CustomUserAdmin(UserAdmin):
    Define admin model for custom User model with no username field.
    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     (_('Personal info'), {'fields': ('first_name', 'last_name')}),
    #     (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
    #                                    'groups', 'user_permissions')}),
    #     (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    # )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(get_user_model(), CustomUserAdmin)"""