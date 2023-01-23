from django.urls import include, path
# from rest_framework import routers
from .views import Coach
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/text/', Coach.as_view(), name='Coach_text'),
    path('delete/<int:pk>/' , Coach.delete, name='delete'),
]