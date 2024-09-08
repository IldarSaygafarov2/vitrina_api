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
    user_permissions = serializers.StringRelatedField(read_only=True, many=True)
    has_perm_add = serializers.SerializerMethodField(method_name='get_has_perm_add')

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'tg_username', 'phone_number', 'user_permissions',
                  'user_type', 'has_perm_add']
        read_only_fields = ['user_permissions']

    def get_has_perm_add(self, instance: User):
        print(instance.user_permissions.values())