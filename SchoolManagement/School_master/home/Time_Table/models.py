from django.db import models
class Time_table(models.Model):
    class_name = models.IntegerField(default=5)
    subject = models.IntegerField()
    day = models.IntegerField()
    slot = models.IntegerField()
    teacher = models.IntegerField()

    def __str__(self):
        return self.pk
