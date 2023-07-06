from rest_framework import serializers
from .models import User, Transaction

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name',"contact_number","address","money","id"]


class TransactionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['user_id','date','money','is_credited']
