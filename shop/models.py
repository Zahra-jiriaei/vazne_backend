from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_code = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    describtion = models.TextField()
    slug = models.SlugField(max_length=250)
    data_added = models.DateTimeField()
    num_stars = models.IntegerField()
    existence = models.BooleanField()
    Unit_price = models.DecimalField(max_digits=10, decimal_places=10)
    manufacturer = models.CharField(max_length=250)
    discount = models.DecimalField(max_digits=10, decimal_places=10)
    review = models.TextField()
    color = models.CharField(max_length=250)
    
