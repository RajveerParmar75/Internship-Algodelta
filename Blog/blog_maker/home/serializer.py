from .models import Layout, ContentData,Header
from rest_framework import serializers


class MainDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layout
        fields = '__all__'


class ContentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentData
        fields = '__all__'
class HeaderDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'