from rest_framework import serializers
from .models import Register, Document, Organization
from .models import CustomUser


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class RegisterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'


class UploadDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class OrganizationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
