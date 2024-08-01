from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def users_api_root(request):
    return Response({'message': 'working'})