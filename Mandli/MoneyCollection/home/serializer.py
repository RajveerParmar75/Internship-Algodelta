from rest_framework import serializers
from .models import CustomUser, Register, AdminUser, AgentUser, Saving_account, Saving_Transection, Loan_account, \
    Loan_Transection


class RegisterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class AdminUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = '__all__'


class AgentUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentUser
        fields = '__all__'


class Saving_accountDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving_account
        fields = '__all__'


class Saving_TransectionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving_Transection
        fields = '__all__'


class Loan_TransectionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_Transection
        fields = '__all__'


class Loan_DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_account
        fields = '__all__'
