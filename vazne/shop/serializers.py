from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User
from accounts.models import CustomUser

class ProductSerializers(serializers.HyperlinkedModelSerializer):
    images = serializers.ImageField(max_length=None , use_url = True)
    class Meta(object):
        model = Product
        fields = '__all__' 
        
class UserSerializers(serializers.ModelSerializer):
    class Meta(object):
        model = CustomUser
        fields =  '__all__'
        