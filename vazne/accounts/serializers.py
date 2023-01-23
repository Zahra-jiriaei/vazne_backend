from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser
from .models import credit
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
    fields = [ "id","username","email","password"]
    

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    # validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(max_length = 20)
    password = serializers.CharField(write_only=True,
                                     required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustomUser
        fields = ('email','username','password','password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        else:
            return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
        username=validated_data['username'],
        email=validated_data['email'],)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
#------------Credit-------------
class creditSerializer(serializers.ModelSerializer):
    # model = credit
    # credit_amount = serializers.CharField(write_only=True,
    #                                  required=True)
    
    class Meta(object):
        model = credit
        fields = '__all__' 
    
    def create(self, validated_data):
        obj = credit.objects.create(**validated_data)
        obj.save()
        return obj