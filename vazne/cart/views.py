from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import  Cart, DeliveryCost
from accounts.models import CustomUser
from .serializers import  CartSerializer, DeliveryCostSerializer
# from .helpers import CartHelper


#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all().order_by('id')
#   serializer_class = UserSerializer


class CartViewSet(APIView):

    def get(self, request, *args, **kwargs):
        try:
            queryset = Cart.objects.all().order_by('id')
            serializer_class = CartSerializer(queryset)
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'Error': str(e)})

    def post(self,request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        platform = Cart.objects.get(pk=pk)
        serializer = CartSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = Cart.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)