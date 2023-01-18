#from numpy import _DatetimeScalar
from rest_framework import request, serializers
from rest_framework.viewsets import ModelViewSet
from .models import *
from decimal import Decimal
from accounts.models import CustomUser
#from djoser.serializers import UserSerializer as BaseUserSerializer
from accounts.serializers import CustomUser
from datetime import date, datetime, time, timedelta
import base64
import os
from rest_framework.exceptions import ValidationError
import jdatetime
from django.utils.timezone import now

class CategorySerializer(serializers.ModelSerializer):
    courses = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['title', 'courses']


class CoursesSerializers(serializers.ModelSerializer):
    #images = serializers.ImageField(max_length=None , use_url = True)
    category = CategorySerializer(many=True)
    comments = serializers.StringRelatedField(many=True, read_only=True)
    # category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    # category = serializers.StringRelatedField()
    # comments = serializers.StringRelatedField()
    # category= serializers.ReadOnlyField(source='Category.name')
    class Meta(object):
        model = Course
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # days_since_joined = serializers.SerializerMethodField()
    class Meta(object):
        model = CustomUser
        fields =  '__all__' 
        def get_days_since_joined(self, obj):
            return (now() - obj.date_joined).days

class CommentSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='Course.instructor.username')
    course = serializers.ReadOnlyField(source='Course.course_name')
    class Meta:
        model = Comment
        fields = '__all__' 










"""

class CourseTitleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ['id', 'title']
        
class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username']


class ReplySerializer(serializers.ModelSerializer):
    user = UserCommentSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'created_date', 'text', 'user']
        read_only_fields = ['id', 'created_date', 'user']
        
    def create(self, validated_data):
        request = self.context.get("request")
        validated_data['course_id'] = self.context.get("course")
        validated_data['parent_id'] = self.context.get("parent")
        #validated_data['created_date'] = _DatetimeScalar.datetime.now().__str__()
        validated_data['user'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['created_date'] = jdatetime.datetime.now().__str__()
        return super().update(instance, validated_data)

class CommentSerializer(serializers.ModelSerializer):
    reply = ReplySerializer(read_only=True)
    user = UserCommentSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'created_date', 'text', 'user', 'reply']
        read_only_fields = ['id', 'created_date']

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data['course_id'] = self.context.get("course")
        validated_data['created_date'] = jdatetime.datetime.now().__str__()
        validated_data['user'] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['created_date'] = jdatetime.datetime.now().__str__()
        return super().update(instance, validated_data)


class InstructorCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title','start_date',
                  'end_date', 'max_students']

class CourseSerializer(serializers.ModelSerializer):
    instructor = UserSerializer(read_only=True)
    # comments = CommentSerializer(many=True, read_only=True))
    # instructor = serializers.HyperlinkedRelatedField(
    #     queryset=Instructor.objects.all(), view_name='instructor-detail')
    class Meta:
        model = Course
        fields = ('id', 'created_at', 'categories', 'instructor',
                  'title',"capacity", 'description','min_students', 'max_students')
        read_only_fields = ('id', 'created_at', 'instructor')
    

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data['instructor'] = request.user.instructor
        validated_data['capacity'] = validated_data['max_students']
        return super().create(validated_data)

    def update(self, instance, validated_data):
        capacity = instance.capacity + \
            validated_data.get(
                'max_students', instance.max_students) - instance.max_students
        if capacity < 0:
            self.fail("course remaining capacity should not be negative")
        validated_data['capacity'] = capacity
        return super().update(instance, validated_data)
"""

        
        