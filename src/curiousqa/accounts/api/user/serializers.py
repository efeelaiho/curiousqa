from accounts.models import Account
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class AccountUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ChangeEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255,min_length=None)

