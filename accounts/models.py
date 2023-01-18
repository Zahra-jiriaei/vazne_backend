from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _


from .managers import CustomUserManager

class CustomUser(User):
    role_choice=((0,"Customer"),(1,"Coach"))
    role = models.CharField(max_length=1, choices=role_choice)
    objects = CustomUserManager()

class credit(models.Model):
    user = models.ForeignKey(CustomUser, blank=True, on_delete=models.CASCADE)
    amount=models.PositiveIntegerField(default=0,blank=False,null=False)

    """def item_sold(self,count):
        current_amount=self.amount
        current_amount=current_amount-count
        self.amount=current_amount
        self.save()
        return self.amount"""