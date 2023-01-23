
from .views import LogoutView, RegisterAPI , LoginAPI, credit
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from accounts import views


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    # path('api/credit/', credit.as_view(), name='monetary_credit'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('credit/', views.CreditList.as_view()),
    path('credit/<int:pk>/', views.CreditDetail.as_view()),
]