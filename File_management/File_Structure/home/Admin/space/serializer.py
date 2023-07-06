from rest_framework import serializers
from ...models import SpaceModel
class  SpaceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceModel
        fields = '__all__'