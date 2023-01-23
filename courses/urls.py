from django.urls import path, include
from . import views
#from django.conf.urls import include,url
from rest_framework_simplejwt import views as jwt_views
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import re_path as url


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    # path('', include(router.urls)),
    # path('v1/' , include(router.urls)),
    path('token/' , jwt_views.TokenObtainPairView.as_view() ,  name = 'token_obtain_pair'),
    path('token/refresh/' , jwt_views.TokenRefreshView.as_view() ,  name = 'token_Refresh'),
    path('list/', views.CourseList.as_view(), name = 'Course_List'),
    path('list/<int:pk>/', views.CourseDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
