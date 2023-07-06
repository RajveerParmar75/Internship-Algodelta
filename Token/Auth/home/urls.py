from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', get, name='get account details'),
    path('post', post, name='post details'),
path('getcity', get_city, name='get city'),
path('api/cities/', create_city, name='create-city'),
]