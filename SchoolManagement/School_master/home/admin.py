from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .Token.models import CustomUser

admin.site.register(CustomUser, UserAdmin)
