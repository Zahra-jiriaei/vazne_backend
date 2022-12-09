from django.db import models

# Create your models here.
from django.db import models
from accounts.models import CustomUser

class CoachText(models.Model):
    #coach_name=models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.CharField(max_length=50)
    text = models.CharField(max_length=250)
    add_by = models.ForeignKey(CustomUser , on_delete=models.CASCADE)

    
    def __str__(self):
        return "{}\n{}".format(self.subject,self.text)