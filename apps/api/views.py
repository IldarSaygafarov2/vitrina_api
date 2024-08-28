from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, generics
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from . import serializers, models
from .filters import AdvertisementFilter
from .models import UserRequest


class DisrtrictViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DistrictSerializer
    queryset = models.District.objects.all()
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


# @extend_schema(tags=['Объявления'])
class AdvertisementViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, )
    queryset = models.Advertisement.objects.all()
    serializer_class = serializers.AdvertisementSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdvertisementFilter

    def create(self, request, *args, **kwargs):
        print(request.data, request.FILES, args, kwargs)
        return super().create(request, *args, **kwargs)


class DistrictListView(generics.ListAPIView):
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer


@extend_schema(tags=['Категории'])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'


class UserRequestCreateView(generics.CreateAPIView):
    serializer_class = serializers.UserRequestSerializer
    queryset = UserRequest.objects.all()
