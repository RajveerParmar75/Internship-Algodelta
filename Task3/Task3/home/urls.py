# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceViewSet

router = DefaultRouter()
router.register(r'devices', DeviceViewSet, basename='devices')

urlpatterns = [
    path('', include(router.urls)),
]
