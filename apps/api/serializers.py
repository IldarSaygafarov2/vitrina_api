import random

from rest_framework import serializers

from apps.users.serializers import UserAdvertisementSerializer
from . import models
from apps.users.models import User


class AdvertisementGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdvertisementGallery
        fields = ['id', 'advertisement', 'photo']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.District
        fields = ['id', 'name', 'slug']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name', 'slug']


class AdvertisementListSerializer(serializers.ModelSerializer):
    preview = serializers.SerializerMethodField(method_name='get_preview')

    class Meta:
        model = models.Advertisement
        fields = ['id', 'name', 'price', 'address', 'rooms_qty_from', 'rooms_qty_to',
                  'quadrature_from', 'quadrature_to', 'floor_from', 'floor_to', 'preview', 'user']

    def get_preview(self, obj) -> str:
        request = self.context.get('request')
        image_url = request.build_absolute_uri(obj.get_preview()) if obj.get_preview() else ""
        return image_url


class AdvertisementSerializer(serializers.ModelSerializer):
    gallery = AdvertisementGallerySerializer(many=True, required=False)
    related_objects = serializers.SerializerMethodField(method_name='get_related_objects')

    class Meta:
        model = models.Advertisement
        fields = [
            'id',
            'name',
            'description',
            'district',
            'address',
            'property_type',
            'operation_type',
            'price',
            'rooms_qty_from',
            'rooms_qty_to',
            'quadrature_from',
            'quadrature_to',
            'house_quadrature_from',
            'house_quadrature_to',
            'floor_from',
            'floor_to',
            'repair_type',
            'auction_allowed',
            'is_studio',
            'creation_year',
            'category',
            'user',
            'is_moderated',
            'gallery',
            'related_objects',
        ]

        read_only_fields = ['related_objects']

    def get_related_objects(self, obj) -> list:
        qs = models.Advertisement.objects.filter(property_type=obj.property_type)
        qs = random.sample(list(qs), len(qs))
        serializer = AdvertisementListSerializer(qs, many=True, context={'request': self.context.get('request')})
        return serializer.data

    @staticmethod
    def get_property_type_display(obj) -> str:
        return obj.get_property_type_display()

    @staticmethod
    def get_repair_type_display(obj) -> str:
        return obj.get_repair_type_display()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        district = models.District.objects.get(id=instance.district.id)
        category = models.Category.objects.get(id=instance.category.id)
        user = User.objects.get(id=instance.user.id)
        district_serializer = DistrictSerializer(district)
        category_serializer = CategorySerializer(category)
        user_serializer = UserAdvertisementSerializer(user)
        data['district'] = district_serializer.data
        data['category'] = category_serializer.data
        data['user'] = user_serializer.data
        data['repair_type'] = instance.get_repair_type_display()
        data['property_type'] = instance.get_property_type_display()
        return data


class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserRequest
        fields = ['id', 'first_name', 'operation_type', 'object_type', 'phone_number', 'message']


class AdvertisementModeratedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdvertisementRequestForModeration
        fields = ['pk', 'user', 'advertisement', 'is_moderated']


class ConsultationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConsultationRequest
        fields = ['id', 'fullname', 'phone_number']


# class AdvertisementModerationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.AdvertisementModeration
#         fields = ['pk', 'realtor', 'advertisement', 'decline_reason']
