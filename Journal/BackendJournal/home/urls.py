from django.contrib import admin
from django.urls import path
from .views import UserDataView,TransactionDataView
urlpatterns = [
    path("add",UserDataView().as_view(),name="add user"),
    path("transaction/<int:id>/",TransactionDataView().as_view(),name="transaction")
]