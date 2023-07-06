from django.db import models
class Grade(models.Model):
    teacher_id=models.IntegerField()
    rank=models.FloatField()