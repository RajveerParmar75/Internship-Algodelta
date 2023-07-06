from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    contact_number = models.CharField( max_length=100)
    address = models.TextField()
    money = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    money = models.IntegerField(default=0)
    is_credited = models.BooleanField(default=True)
