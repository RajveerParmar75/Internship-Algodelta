from django.db import models
class Hod(models.Model):
    name=models.CharField(max_length=50)
    income=models.IntegerField(default=1000)
