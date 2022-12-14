from rest_framework import  permissions
from django.contrib.auth.models import User 
from .models import Product , Category , Comment
from .serializers import  ProductSerializers , UserSerializers , CategorySerializers , CommentSerializers
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class Productsearch(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ProductSerializers
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [ReviewListThrottle, AnonRateThrottle]

    # def get_queryset(self):
    #     username = self.kwargs['username']
    #     return Review.objects.filter(review_user__username=username)

    def get_queryset(self):
        product_name = self.request.query_params.get('product_name', None)
        return Product.objects.filter(product_name)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter , django_filters.rest_framework.DjangoFilterBackend ,filters.OrderingFilter]
    filterset_fields = ('category','product_name')
    search_fields = ['product_name']
    ordering_fields = ['Unit_price', 'data_added']
    
    # def get_queryset(self):
    #     product_name = self.request.user
    #     return Product.objects.filter(product_name = product_name)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ('owner','product')
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]