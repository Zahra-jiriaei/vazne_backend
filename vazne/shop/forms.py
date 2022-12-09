"""
from django import forms
from .models import Product


class ShopForm(forms.Form):
    product_name = forms.CharField(max_length=250)
    product_code = forms.CharField(max_length=250)
    category = forms.CharField(max_length=250)
    describtion = forms.CharField()
    slug = forms.SlugField(max_length=250)
    data_added = forms.DateTimeField()
    num_stars = forms.IntegerField()
    existence = forms.BooleanField()
    existence = forms.BooleanField()
    num_existence=forms.IntegerField()
    Unit_price = forms.DecimalField(max_digits=10, decimal_places=2)
    manufacturer = forms.CharField(max_length=250)
    discount = forms.DecimalField(max_digits=5, decimal_places=2)
    review = forms.CharField()
    color = forms.CharField(max_length=250)
    
class ShopUpdateForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = ('product_name' , 'product_code', 'category', 'describtion', 'slug', 'data_added' ,'num_stars' , 'existence' , 'Unit_price', 'manufacturer' , 'discount' , 'review' , 'color')
            """