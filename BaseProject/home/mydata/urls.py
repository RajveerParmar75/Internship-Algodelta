from django.urls import path
from .views import obtain_token

urlpatterns = [
    path('api/token/', obtain_token, name='token_obtain'),
]
