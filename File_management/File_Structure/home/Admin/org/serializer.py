from rest_framework import serializers
from ...models import OrganizationModel
class  OrganizationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationModel
        fields = '__all__'