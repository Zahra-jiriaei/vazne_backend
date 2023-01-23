from django.db import models
from django.contrib.auth.models import User
from django.db import models

def product_directory_path(instance, filename):
    return 'images/{0}/'.format(filename)

# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     product = models.ManyToManyField('Product', related_name='categories', blank=True)
#     class Meta:
#         verbose_name_plural = 'categories'
#     def __str__(self):
#         return self.name
    
class Product(models.Model):
    product_name = models.CharField(max_length=250)
    product_code = models.CharField(max_length=250)
    field_choice=(("football","football"),("basketball","basketball"),("swim","swim"))
    fields = models.CharField(max_length=100, choices=field_choice)
    # category = models.ManyToManyField(Category, related_name='products' , blank=False, default='category')
    describtion = models.TextField()
    slug = models.SlugField(max_length=250)
    data_added = models.DateTimeField()
    num_stars = models.IntegerField()
    existence = models.BooleanField()
    num_existence = models.IntegerField()
    Unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    manufacturer = models.CharField(max_length=250)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    review = models.TextField()
    color = models.CharField(max_length=250)
    add_by = models.ForeignKey(User , on_delete=models.CASCADE)
    images = models.ImageField(upload_to='Images/', default = 'Images/None/No-img.jpg')
    
    class Meta:
        ordering = ['-data_added']   
    def __str__(self):
        return self.product_name
    
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=False)
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    def __str__(self):
        return self.title