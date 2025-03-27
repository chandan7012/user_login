from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.services import register_user, login_user, access_token

@api_view(['POST'])
def refresh_token(request):
    response, status = access_token(request)
    return Response(data = response, status = status)

@api_view(['POST'])
def register(request):
    response, status = register_user(request.data)
    return Response(data = response, status = status)

@api_view(['POST'])
def login(request):
    response, status = login_user(request.data)
    return Response(data = response, status = status)