from django.db import models

class User(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    mobile_number=models.IntegerField(default=0)
    address=models.TextField()
    proof=models.TextField()
    loan_amount=models.IntegerField(default=0)
    outstanding=models.IntegerField(default=0)
    penalty=models.IntegerField(default=0)
    days=models.IntegerField(default=0)
    starting_date=models.DateTimeField()
    ending_date=models.DateTimeField()
class Transaction(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    is_credited=models.BooleanField(default=True)
    amount=models.IntegerField(default=0)