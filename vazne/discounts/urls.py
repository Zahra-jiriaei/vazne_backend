from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'campaign', views.CampaignViewSet)
router.register(r'coupon', views.CouponViewSet)

urlpatterns = [
    path('', include((router.urls, 'vazne.discounts'))),
]