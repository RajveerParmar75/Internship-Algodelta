from django.db import models

class Teacher(models.Model):
    name=models.CharField(max_length=50)
    time=models.IntegerField(default=0)
    money=models.FloatField()
    def __str__(self):
        return self.name
