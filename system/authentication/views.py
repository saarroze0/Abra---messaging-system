
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST']) 
@renderer_classes([JSONRenderer]) 
def signup(request):
    username=request.data['username']
    password=request.data['password']

    User.objects.create_user(username=username, password=password)
    
    return redirect('signin')

def signin(request):
    pass




def signout(request):
    pass