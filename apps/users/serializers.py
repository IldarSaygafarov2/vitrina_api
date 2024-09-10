from rest_framework import serializers
from .models import User


class IsUserRealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_type']
        read_only_fields = ['user_type']


class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'tg_username', 'phone_number', 'user_type']