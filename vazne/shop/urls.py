from django.urls import path
from . import views
from django.conf.urls import include
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('' , views.ProductView)
router.register('user' , views.UserView)
 


urlpatterns = [
    path('v1/' , include(router.urls)),
    path('token/' , jwt_views.TokenObtainPairView.as_view() ,  name = 'token_obtain_pair'),
    path('token/refresh/' , jwt_views.TokenRefreshView.as_view() ,  name = 'token_Refresh'),
    path('', views.shop),
    path('detail/<int:shop_id>/' , views.detail , name='details'),
    path('delete/<int:shop_id>/' , views.delete, name='delete'),
    #path('update/<int:shop_id>/' , views.update, name='update'),
    #path('create/' , views.create , name='create'),
]


