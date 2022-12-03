from django.urls import include, path
# from rest_framework import routers
from .views import CartViewSet

#router = routers.DefaultRouter()
#router.register(r'cart', views.CartViewSet)
#router.register(r'delivery-cost', views.DeliveryCostViewSet)


#urlpatterns = [
#    path('', include((router.urls, 'shopping_cart_api.cart'))),
#]

urlpatterns = [
    path('api/mycart/', CartViewSet.as_view({'get': 'list'}), name='Cart'),
]