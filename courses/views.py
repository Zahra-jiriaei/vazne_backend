from django.shortcuts import render

# Create your views here.
import genericpath
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.viewsets import GenericViewSet, ModelViewSet, ReadOnlyModelViewSet, ViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework.filters import SearchFilter, OrderingFilter
#from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from functools import partial
from pstats import Stats
from requests import Response
from courses.models import Category, Course
from courses.serializers import CoursesSerializers
from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend


class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializers
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializers
    
class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter , django_filters.rest_framework.DjangoFilterBackend ,filters.OrderingFilter]
    filterset_fields = ('category','course_name')
    search_fields = ['course_name']
    ordering_fields = ['data_added']
    
  
    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ('instructor','course')
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]




























"""

class CourseViewSet(ModelViewSet):
    	# queryset = Course.objects.select_related('instructor').all()
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
	#filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	#filterset_fields = ['instructor_id']
	#filterset_class = CourseFilter
	search_fields = ['title']  # space comma seprator
	#ordering_fields = ['price', 'last_update']  # -prince, last_update
	#pagination_class = DefaultPagination  # can be moved to settings
	#permission_classes = [IsInstructorOrReadOnly]

	def create(self, request, *args, **kwargs):
     
		data = request.data.copy()
		serializer = self.get_serializer(data=data)
		serializer.is_valid(raise_exception=True)
		course = serializer.save()

		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, 
				status=status.HTTP_201_CREATED, headers=headers)

	def update(self, request, *args, **kwargs):
		course_old = self.get_object()
		if course_old.is_owner(request.user.instructor):
			data = request.data.copy()
			
			instance = self.get_object()
			serializer = self.get_serializer(instance, data=data, partial=partial)
			serializer.is_valid(raise_exception=True)
			course = serializer.save()

			try:
				self.update_room(course)
			except Exception as e:
				course = course_old
				course.save()
				return Response(status=status.HTTP_400_BAD_REQUEST)

			if getattr(instance, '_prefetched_objects_cache', None):
				instance._prefetched_objects_cache = {}

			return Response(serializer.data, status=status.HTTP_200_OK)

		return Response("your'e not the course owner", status=status.HTTP_403_FORBIDDEN)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		if instance.is_owner(request.user.instructor):
			try:
				instance = self.get_object().delete()
			except Exception as e:
				return Response({'Message':'Something went wrong due to {}'.format(str(e))}, status = status.HTTP_400_BAD_REQUEST)



	
class CategoryViewSet(ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	#permission_classes = [IsAdminOrReadOnly]

	@action(detail=True, url_path="courses")
	def get_courses(self, request, *args, **kwargs):
		category = self.get_object()
		serializer = self.get_serializer(category.courses, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)"""