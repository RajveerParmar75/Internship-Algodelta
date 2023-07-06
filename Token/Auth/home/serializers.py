from rest_framework import serializers
from .models import User
from .models import City, State

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



from rest_framework import serializers
from .models import City, State

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('id', 'name')

class CitySerializer(serializers.ModelSerializer):
    state = StateSerializer()  # Nested serializer for the state field

    class Meta:
        model = City
        fields = ('id', 'name', 'state')