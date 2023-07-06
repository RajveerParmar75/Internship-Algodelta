from rest_framework import serializers
from .models import Register
from ..Token.models import CustomUser
class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
class RegisterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'