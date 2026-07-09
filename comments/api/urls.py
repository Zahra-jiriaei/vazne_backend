from django.urls import re_path as url
from django.contrib import admin

from .views import (CommentListAPIView , CommentDetailAPIView)

urlpatterns = [
    url(r'^$' , CommentListAPIView.as_view() ,name='list'),
    #url(r'^(?p<id>/d+)/$' , CommentDetailAPIView.as_view() ,name='thread'),
]
 