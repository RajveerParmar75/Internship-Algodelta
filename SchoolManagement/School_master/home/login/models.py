from django.db import models
class LoginUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)