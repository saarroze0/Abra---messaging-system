from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from .models import Message_contains
from .serializers import MessageSerializer

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


# Get all messages for a specific user


@api_view(['GET'])  # @@@@@@@@@@@ need to understand
@renderer_classes([JSONRenderer])  # @@@@@@@@@@@ need to understand
def inbox(request, user):
    receiver_messages = Message_contains.objects.filter(receiver=user)
    # @@@@@@@@@@@ need to understand
    serializer = MessageSerializer(receiver_messages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
# end all messages for a specific user


@api_view(['GET'])  # @@@@@@@@@@@ need to understand
@renderer_classes([JSONRenderer])  # @@@@@@@@@@@ need to understand
def unread_inbox(request, user):
    receiver_messages = Message_contains.objects.filter(
        receiver=user, unread_messages=True)
    # @@@@@@@@@@@ need to understand
    serializer = MessageSerializer(receiver_messages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
# end all messages for a specific user


@api_view(['GET'])  # @@@@@@@@@@@ need to understand
@renderer_classes([JSONRenderer])  # @@@@@@@@@@@ need to understand
def readMessage(request, id):
    receiver_message = Message_contains.objects.all()[id-1]
    # @@@@@@@@@@@ need to understand
    receiver_message.unread_messages = False
    receiver_message.save()
    # receiver = Message_contains.objects.all()[id-1]
    serializer = MessageSerializer(receiver_message)
    return Response(serializer.data, status=status.HTTP_200_OK)
# end all messages for a specific user


@api_view(['DELETE'])  # @@@@@@@@@@@ need to understand
@renderer_classes([JSONRenderer])  # @@@@@@@@@@@ need to understand
def deleteMessage(request, id):
    delete_message = Message_contains.objects.filter(id=id)
    delete_message.delete()
    return Response(id, status=status.HTTP_200_OK)
