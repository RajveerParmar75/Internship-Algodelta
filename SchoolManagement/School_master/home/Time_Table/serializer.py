from rest_framework import serializers
from .models import Time_table


class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time_table
        fields = '__all__'
