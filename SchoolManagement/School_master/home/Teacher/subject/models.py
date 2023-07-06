from django.db import models
class Subject(models.Model):
    teacher_id=models.IntegerField(default=0)
    subject_name = models.CharField(max_length=50)
    def __str__(self):
        return self.subject_name