from rest_framework import serializers
from apps.users.serializers import SimpleUserSerializer
from . import models
import random


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
        fields = ['id', 'price', 'address', 'rooms_qty_from', 'rooms_qty_to',
                  'quadrature_from', 'quadrature_to', 'floor_from', 'floor_to', 'preview']

    def get_preview(self, obj) -> str:
        return obj.get_preview()


class AdvertisementSerializer(serializers.ModelSerializer):
    gallery = AdvertisementGallerySerializer(many=True, required=False)
    user = SimpleUserSerializer(read_only=True, many=False)
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
            'floor_from',
            'floor_to',
            'repair_type',
            'auction_allowed',
            'is_studio',
            'creation_year',
            'category',
            'user',
            'gallery',
            'related_objects',
        ]

    def get_related_objects(self, obj) -> list:
        qs = models.Advertisement.objects.filter(property_type=obj.property_type)
        qs = random.sample(list(qs), 3)
        serializer = AdvertisementListSerializer(qs, many=True)
        return serializer.data

    def get_property_type_display(self, obj) -> str:
        return obj.get_property_type_display()

    def get_repair_type_display(self, obj) -> str:
        return obj.get_repair_type_display()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        district = models.District.objects.get(id=instance.district.id)
        category = models.Category.objects.get(id=instance.category.id)
        district_serializer = DistrictSerializer(district)
        category_serializer = CategorySerializer(category)
        data['district'] = district_serializer.data
        data['category'] = category_serializer.data
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
