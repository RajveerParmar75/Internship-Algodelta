from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import *
urlpatterns = [
    path('', RegisterView().as_view(), name='token_obtain_pair'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('loginUser', LoginUserView().as_view(), name='token_refresh'),
    path('Session', SessionView().as_view(), name='token_refresh'),
    path('states/', StateListAPIView().as_view(), name='state-list'),
    path('city/', CityListAPIView().as_view(), name='state-list'),
]