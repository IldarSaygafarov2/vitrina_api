from rest_framework import serializers
from . import models


class AdvertisementGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdvertisementGallery
        fields = ['id', 'photo']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.District
        fields = ['id', 'name', 'slug']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name', 'slug']


class AdvertisementSerializer(serializers.ModelSerializer):
    # property_type = serializers.SerializerMethodField(method_name='get_property_type_display')
    # repair_type = serializers.SerializerMethodField(method_name='get_repair_type_display')
    gallery = AdvertisementGallerySerializer(many=True, required=False)

    class Meta:
        model = models.Advertisement
        fields = [
            'id',
            'name',
            'description',
            'district',
            'address',
            'property_type',
            'price',
            'rooms_qty_from',
            'rooms_qty_to',
            'quadrature_from',
            'quadrature_to',
            'floor_from',
            'floor_to',
            'repair_type',
            'auction_allowed',
            'category',
            'gallery',
        ]

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
        fields = ['id', 'first_name', 'operation_type', 'object_type', 'phone_number', 'email', 'message']
