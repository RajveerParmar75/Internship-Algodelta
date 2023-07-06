import uuid as uuid
from django.db import models

class User(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mac = models.CharField(max_length=17,null=True)

    def __str__(self):
        return self.username
