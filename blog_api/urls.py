# blog_api/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers # <-- Agrega esta línea

router = routers.DefaultRouter() # <-- Agrega esta línea

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')), # <-- Agrega esta línea
]