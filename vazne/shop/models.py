from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db import models

def product_directory_path(instance, filename):
    return 'images/{0}/'.format(filename)

class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_code = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    describtion = models.TextField()
    slug = models.SlugField(max_length=250)
    data_added = models.DateTimeField()
    num_stars = models.IntegerField()
    existence = models.BooleanField()
    Unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    manufacturer = models.CharField(max_length=250)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    review = models.TextField()
    color = models.CharField(max_length=250)
    add_by = models.ForeignKey(User , on_delete=models.CASCADE)
    images = models.ImageField(upload_to='Images/', default = 'Images/None/No-img.jpg')
    
    def __str__(self):
        return self.product_name
    

    