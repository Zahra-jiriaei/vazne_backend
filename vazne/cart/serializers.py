from .models import  Cart, DeliveryCost
from rest_framework import serializers



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id',"user", 'item', 'quantity']


class DeliveryCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCost
        fields = ['id', 'status', 'cost_per_delivery', 'cost_per_product', 'fixed_cost']
