from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import User
from .serializers import IsUserRealtorSerializer


@api_view(['GET'])
def users_api_root(request):
    return Response({'message': 'working'})


class UserTypeRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = IsUserRealtorSerializer
    lookup_field = 'tg_username'