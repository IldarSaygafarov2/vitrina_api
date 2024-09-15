from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import MultiPartParser, JSONParser

from . import serializers, models
from .filters import AdvertisementFilter


@extend_schema(tags=['Районы'])
class DisrtrictViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DistrictSerializer
    queryset = models.District.objects.all()
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


@extend_schema(tags=['Объявления'])
class AdvertisementViewSet(viewsets.ModelViewSet):
    # parser_classes = (MultiPartParser, JSONParser)
    queryset = models.Advertisement.objects.all()
    serializer_class = serializers.AdvertisementSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdvertisementFilter
    pagination_class = LimitOffsetPagination



@extend_schema(tags=['Категории'])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'


@extend_schema(tags=['Заявки пользователей'])
class UserRequestCreateView(generics.CreateAPIView):
    serializer_class = serializers.UserRequestSerializer
    queryset = models.UserRequest.objects.all()


class AdvertisementGalleryView(viewsets.ModelViewSet):
    queryset = models.AdvertisementGallery.objects.all()
    serializer_class = serializers.AdvertisementGallerySerializer
