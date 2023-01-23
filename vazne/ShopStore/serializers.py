from rest_framework import serializers
from .models import Product , Comment
from django.contrib.auth.models import User
from django.utils.timezone import now

# class CategorySerializers(serializers.ModelSerializer):
#     products = serializers.StringRelatedField(many=True, read_only=True)
#     # product = serializers.ReadOnlyField(source='product.product_name')
#     class Meta:
#         model = Category
#         fields = ['name' , 'products']
        
class ProductSerializers(serializers.ModelSerializer):
    images = serializers.ImageField(max_length=None , use_url = True)
    # category = CategorySerializers(many=True)
    comments = serializers.StringRelatedField(many=True, read_only=True)
    # category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    # category = serializers.StringRelatedField()
    # category= serializers.ReadOnlyField(source='Category.name')
    class Meta(object):
        model = Product
        fields = '__all__'
        
    def create(self, validated_data):
        obj = Product.objects.create(**validated_data)
        obj.save()
        return obj
        
    
    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['comments'] = CommentSerializers(instance.Unit_price).data
    #     return rep

class UserSerializers(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # days_since_joined = serializers.SerializerMethodField()
    class Meta(object):
        model = User
        fields =  '__all__' 
        def get_days_since_joined(self, obj):
            return (now() - obj.date_joined).days

class CommentSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # product = serializers.ReadOnlyField(source='product.product_name')
    
    class Meta:
        model = Comment
        fields = '__all__' 
        
    def create(self, validated_data):
        obj = Comment.objects.create(**validated_data)
        obj.save()
        return obj