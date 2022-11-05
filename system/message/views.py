from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Message_contains

# write message


@api_view(['POST'])  # @@@@@@@@@@@ need to understand
@renderer_classes([JSONRenderer])  # @@@@@@@@@@@ need to understand
def sendMessage(request):
    newMessage = Message_contains(
        sender=request.data["sender"],
        receiver=request.data["receiver"],
        message=request.data["message"],
        subject=request.data["subject"],
    )
    newMessage.save()

    return Response(status=status.HTTP_200_OK)
# end write message
