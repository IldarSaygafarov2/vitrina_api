from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.response import Response
from apps.api.models import Advertisement
from apps.api.serializers import AdvertisementSerializer
from .models import User
from .serializers import IsUserRealtorSerializer, UserIdSerializer, UserSerializer
from drf_spectacular.utils import extend_schema
from apps.api.filters import AdvertisementFilter
from django_filters.rest_framework import DjangoFilterBackend


@extend_schema(tags=['Пользователи'])
class UserListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('user_type',)


class RealtorAdvertisementListView(generics.ListAPIView):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('is_moderated',)

    def get_queryset(self):
        return self.queryset.filter(user=self.kwargs['pk'])

    def get_serializer_context(self):
        return {'request': self.request}


@extend_schema(tags=['Пользователи'])
class UserTypeRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = IsUserRealtorSerializer
    lookup_field = 'tg_username'


@extend_schema(tags=['Пользователи'])
class UserIdRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserIdSerializer
    lookup_field = 'tg_username'
