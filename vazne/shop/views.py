from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import ShopForm , ShopUpdateForm

from rest_framework import viewsets , permissions
from django.contrib.auth.models import User
from .models import Product
from .serializers import ProductSerializers , UserSerializers

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAdminUser]


def shop(request):
    all = Product.objects.all()
    return render(request , 'shop.html' , context={'all' : all})
    
def detail(request , shop_id):
    id  = Product.objects.get(id = shop_id)
    return render(request , 'detail.html' , {'id': id})

def delete(request, shop_id):
    Product.objects.get(id = shop_id).delete()
    messages.success(request , 'this item deleted successfully' )
    return redirect('http://127.0.0.1:8000/shop/')

def create(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Product.objects.create(product_name = cd['product_name'] , product_code = cd['product_code'] , category = cd['category'] ,describtion = cd['describtion'] ,slug = cd['slug'] ,data_added = cd['data_added'] ,num_stars = cd['num_stars'] ,existence = cd['existence'] ,Unit_price = cd['Unit_price'] ,manufacturer = cd['manufacturer'] ,discount = cd['discount'] ,review = cd['review'] ,color = cd['color'] )
            messages.success(request , 'Product created successfully' ,'success')
            return redirect('http://127.0.0.1:8000/shop/')
    else:
        form = ShopForm()
    return render(request , 'create.html' , {'form' : form})



def update(request,shop_id):
    product = Product.objects.get(id = shop_id)
    if request.method == 'POST':
        form = ShopUpdateForm(request.POST , instance=product)
        if form.is_valid():
            form.save()
            messages.success(request , 'Product Updated successfully' ,'success')
            return redirect('http://127.0.0.1:8000/shop/',shop_id)
    else:
        form = ShopUpdateForm(instance=product)
    return render(request , 'update.html' , {'form' : form})
    
#----------------ZJ----------------

