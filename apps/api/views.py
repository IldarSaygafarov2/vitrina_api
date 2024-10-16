from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, generics
from rest_framework.pagination import LimitOffsetPagination

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
    queryset = models.Advertisement.objects.all()
    serializer_class = serializers.AdvertisementSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdvertisementFilter

    # filterset_fields = ['is_studio', 'category', 'operation_type', 'district', 'repair_type']

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.AdvertisementListSerializer
        return serializers.AdvertisementSerializer

    def get_serializer_context(self):
        return {'request': self.request}


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


@extend_schema(tags=['Галлерея'])
class AdvertisementGalleryView(viewsets.ModelViewSet):
    queryset = models.AdvertisementGallery.objects.all()
    serializer_class = serializers.AdvertisementGallerySerializer

    def get_queryset(self):
        return self.queryset.filter(advertisement_id=self.kwargs['advertisement_pk'])


@extend_schema(tags=['Заявки на косультацию'])
class ConsultationRequestCreateView(generics.CreateAPIView):
    serializer_class = serializers.ConsultationRequestSerializer
    queryset = models.ConsultationRequest.objects.all()


# @extend_schema(tags=['Модерация объявлений'])
# class AdvertisementModerationView(viewsets.ModelViewSet):
#     queryset = models.AdvertisementModeration.objects.all()
#     serializer_class = serializers.AdvertisementModerationSerializer

