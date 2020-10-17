from accounts.models import Account
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class AccountRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        max_length=255,
        min_length=None,
        allow_blank=False,
        validators=[
            UniqueValidator(
                queryset=Account.objects.all(),
                message='A user with that email already exists.')])
    password = serializers.CharField(
        min_length=8, max_length=100, write_only=True, style={
            'input_type': 'password'})

    class Meta:
        model = Account
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # unpack validated data
        return Account.objects.create_user(**validated_data)


class AccountSignInSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, allow_blank=False)
    password = serializers.CharField(required=True, allow_blank=False)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['account_id', 'username', 'email']


class ChangePasswordSerializer(serializers.Serializer):
    model = Account

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
