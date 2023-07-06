from rest_framework import serializers
from .models import *

class BlackListTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackListToken
        fields = '__all__'
class RegisterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'
class LoginDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginUser
        fields = '__all__'
class SessionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)
    class Meta:
        model = State
        fields = '__all__'