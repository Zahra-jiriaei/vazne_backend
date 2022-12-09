from django.urls import include, path
# from rest_framework import routers
from .views import CartViewSet
from rest_framework_simplejwt import views as jwt_views
#router = routers.DefaultRouter()
#router.register(r'cart', views.CartViewSet)
#router.register(r'delivery-cost', views.DeliveryCostViewSet)


#urlpatterns = [
#    path('', include((router.urls, 'shopping_cart_api.cart'))),
#]

urlpatterns = [
    path('token/' , jwt_views.TokenObtainPairView.as_view() ,  name = 'token_obtain_pair'),
    path('token/refresh/' , jwt_views.TokenRefreshView.as_view() ,  name = 'token_Refresh'),
    path('api/mycart/', CartViewSet.as_view(), name='Cart'),
    path('delete/<int:pk>/' , CartViewSet.delete, name='delete'),
    #path('detail/<int:pk>/' , CartViewSet.detail , name='details'),
]