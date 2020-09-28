from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=None, allow_blank=False, 
        validators=[UniqueValidator(queryset=User.objects.all())], message='Email is already in use.')
    password = serializers.CharField(min_legth=8, max_length=100, write_only=True, allow_blank=False)
    first_name = serializers.CharField(min_legth=2, max_length=100, allow_blank=False)
    last_name = serializers.CharField(min_legth=2, max_length=100, allow_blank=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        return User.objects.create_user(validated_data)