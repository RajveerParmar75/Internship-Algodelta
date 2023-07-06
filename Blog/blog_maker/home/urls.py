from django.urls import path
from .views import MainDataView,HeaderView,ContentView

urlpatterns = [
    path('add', MainDataView().as_view(),name="for adding HTML data"),
    path('header', HeaderView().as_view(), name="header"),
    path('content', ContentView().as_view(), name="add content"),
]
