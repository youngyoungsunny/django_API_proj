from django.contrib import admin
from django.urls import path, include
from rest_framework import urls
from django.conf import settings
from django.conf.urls.static import static
from mystorage import urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mystorage.urls')),
    path('api-auth/', include('rest_framework.urls')),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)