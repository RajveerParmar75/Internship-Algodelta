from rest_framework import serializers
from ..models import State
class StateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'