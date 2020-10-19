from profiles.models import Profile
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfilePublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'avatar', 'question_limit', 'account.last_login']

