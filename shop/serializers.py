from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User


class ProductSerializers(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = Product
        fields = '__all__' 
        
class UserSerializers(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields =  '__all__'
        
        
            
    