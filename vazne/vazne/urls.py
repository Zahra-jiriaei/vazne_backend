
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path as url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("accounts.urls")),
    #path('',include("discounts.urls")),
    path('',include("cart.urls")),
    path('shop/', include('shop.urls')),
    path('api/' , include('shop.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/comments/', include(('comments.api.urls' , 'comments') , namespace = 'comments-api')),
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

