from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from . import serializers, models
from .filters import AdvertisementFilter
from django_filters.rest_framework import DjangoFilterBackend


# @extend_schema(tags=['Объявления'])
class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = models.Advertisement.objects.all()
    serializer_class = serializers.AdvertisementSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdvertisementFilter



@extend_schema(tags=['Категории'])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
