from rest_framework import serializers
from ..models import User_TypeModel
class User_TypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_TypeModel
        fields = '__all__'