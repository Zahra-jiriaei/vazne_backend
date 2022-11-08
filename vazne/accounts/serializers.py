from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='get_role_display')
    class Meta:
        model = CustomUser
    fields = [ "id","username","email","password","role"]
    

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(max_length = 20)
    password = serializers.CharField(write_only=True,
                                     required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = CustomUser
        fields = ('username','password','password2', 'email')

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