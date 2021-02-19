from profiles.models import Profile
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class ProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

