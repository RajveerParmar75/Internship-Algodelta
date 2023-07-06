from rest_framework import serializers
from ..models import CityModel
class CityDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = '__all__'