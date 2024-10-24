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
        fields = ['id', 'first_name', 'last_name', 'username', 'tg_username', 'tg_user_id', 'phone_number', 'user_type']


class UserAdvertisementSerializer(serializers.ModelSerializer):
    fullname = serializers.SerializerMethodField(method_name='get_fullname')
    class Meta:
        model = User
        fields  = ['id', 'fullname', 'tg_username', 'phone_number', 'photo']

    @staticmethod
    def get_fullname(obj: User) -> str:
        return obj.get_full_name()


class SimpleUserSerializer(serializers.ModelSerializer):
    fullname = serializers.SerializerMethodField(method_name='get_full_name')

    class Meta:
        model = User
        fields = ['tg_username', 'phone_number', 'fullname', 'photo']

    def get_full_name(self, obj) -> str:
        return obj.get_full_name()
