from .views import *
from django.urls import path

urlpatterns=[
    path('', get, name='alldata'),
    path('post', post, name='alldata'),
]