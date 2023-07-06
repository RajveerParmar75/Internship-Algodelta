from django.core.validators import RegexValidator
from django.db import models
import uuid


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    time = models.TimeField(auto_now=True)
    class Meta:
        abstract = True


class Trade(BaseModel):
    name=models.CharField(max_length=50,null=False,validators=[RegexValidator(r'^[a-zA-Z\s]+$','Only alphabetic characters are allowed.')])
    qnt = models.IntegerField()
    price = models.FloatField()
    action = models.CharField(max_length=4)
    avg = models.FloatField(blank=True,null=True)
    p_l = models.FloatField(blank=True,null=True)



