from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from accounts.models import CustomUser

class CoachText(models.Model):
    #if CustomUser.role==1:
    #add_by=models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='coach_name')
    add_by = models.ForeignKey(CustomUser, blank=True,null=True,on_delete=models.SET_NULL, related_name='Coach')
    subject = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    

    def __str__(self):
        return "{}\n{}".format(self.subject,self.text)