from django.shortcuts import render

# Create your views here.
from pyexpat.errors import messages
from django.shortcuts import redirect, render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import  CoachText

from .serializers import  CoachSerializer
# from .helpers import CartHelper
from rest_framework.views import APIView


class Coach(APIView):
    
    def get(self, request, *args, **kwargs):
        try:
            coach_ = CoachText.objects.all()
            serializer_class = CoachSerializer(coach_, many=True)
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'Error': str(e)})

    def post(self,request):
        
        serializer = CoachSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        platform = CoachText.objects.get(pk=pk)
        serializer = CoachSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            platform = CoachText.objects.get(pk=pk)
            platform.delete()
            messages.success(request , 'this item deleted successfully' )
            return redirect('http://127.0.0.1:8000/coach/')
        except CoachText.DoesNotExist:
            return None
       
"""def detail(request , pk):
    try:
        coach__ = CoachText.objects.get(id=pk)
        serializer_class = CoachSerializer(coach__)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND,
                    data={'Error': str(e)})"""