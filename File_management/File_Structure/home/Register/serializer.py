from rest_framework import serializers
from ..models import Register,CustomUser
class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
class RegisterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'