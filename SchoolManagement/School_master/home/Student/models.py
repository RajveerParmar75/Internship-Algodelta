from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=50)
    standard = models.IntegerField(default=5)
