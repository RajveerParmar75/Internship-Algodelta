from rest_framework import serializers
from .models import User, Transaction


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TransectionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
