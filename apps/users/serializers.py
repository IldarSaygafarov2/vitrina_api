from rest_framework import serializers
from .models import User


class IsUserRealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_type']
        read_only_fields = ['user_type']

