from rest_framework import serializers
from ...models import MonitorMobel


class MonitorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorMobel
        fields = '__all__'
