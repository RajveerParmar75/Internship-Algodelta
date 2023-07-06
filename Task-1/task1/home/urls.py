from .views import *
from django.urls import path
urlpatterns=[
    path('order', Trade_view().as_view(), name='REST'),
]


