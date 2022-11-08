from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def logout_user(request):
    logout(request)
    return Response("logout", status=status.HTTP_200_OK)


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def login_user(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response("You login",status=status.HTTP_200_OK)
    else:
        return Response("You did not connect, try again")


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def register_user(request):
    username = request.data['username']
    password = request.data['password']
    User.objects.create_user(username=username, password=password)
    return Response("You have successfully registered", status=status.HTTP_200_OK)

