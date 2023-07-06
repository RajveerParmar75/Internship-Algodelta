from rest_framework import serializers
from .models import Hod


class HodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hod
        fields = '__all__'