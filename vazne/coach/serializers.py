from .models import  CoachText
from rest_framework import serializers



class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoachText
        fields = '__all__' 