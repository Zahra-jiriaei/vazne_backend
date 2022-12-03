from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import credit

from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, RegisterSerializer, creditSerializer
import json
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
class RegisterAPI(APIView):
    
    def get(self,request):
        return Response({'Message':'This is get method of signup API'},status=status.HTTP_200_OK)

    def post(self,request):
        try:
            obj =  RegisterSerializer(data =  request.data)
            if obj.is_valid():
                obj.save()
                return Response({'Message':'Successfully Signed up'},status = status.HTTP_200_OK)
            return Response(obj.errors,status = status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'Message':'Something Failed due to {}'.format(str(e))}, status = status.HTTP_400_BAD_REQUEST)
 
        
from django.contrib.auth import login

from rest_framework import permissions

  
class LoginAPI(APIView):
    
    def get(self,request):
        return Response({'Message':'This is get method of Login API'},status =  status.HTTP_200_OK)

    def post(self, request):
        try:
            input_data =  request.data
            username =  input_data.get('username')
            password =  input_data.get('password')

            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)

                url =  'http://localhost:8000'+reverse('token_obtain_pair')
                data = {'username':username,'password':password}
                tokens =  requests.post(url,data=data)

                return Response({'Tokens':json.loads(tokens.content)},status = status.HTTP_200_OK)
            else:   
                return Response({'Message':'Invalid username and password combination'}, status =  status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'Message':'Something went wrong due to {}'.format(str(e))}, status = status.HTTP_400_BAD_REQUEST)
        
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
# ------------Cart----------------
class credit(APIView):
    
    def get(self,request):
        try:
            Credit = creditSerializer('amount')
            return JsonResponse(Credit.data)
        
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'Error': str(e)})
        

    def post(self,request):
        try:
            obj =  creditSerializer(data = request.data)
            if obj.is_valid():
                obj.save()
                return Response({'Message':'Successfully done!'},status = status.HTTP_200_OK)
            return Response(obj.errors,status = status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'Message':'Something went wrong due to {}'.format(str(e))}, status = status.HTTP_400_BAD_REQUEST)
 