from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from .models import Message_contains
from .serializers import MessageSerializer
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


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

    return Response("New message send", status=status.HTTP_200_OK)
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
    if receiver_messages.unread_messages == 0:
        return Response("No more messages available")
    # @@@@@@@@@@@ need to understand
    serializer = MessageSerializer(receiver_messages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
# end all messages for a specific user


@api_view(['GET'])  # @@@@@@@@@@@ need to understand
@renderer_classes([JSONRenderer])  # @@@@@@@@@@@ need to understand
def readMessage(request, id):
    try:
        receiver_message = Message_contains.objects.get(pk=(id))
        # @@@@@@@@@@@ need to understand
        receiver_message.unread_messages = False
        receiver_message.save()
        # receiver = Message_contains.objects.all()[id-1]
        serializer = MessageSerializer(receiver_message)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response("Wrong ID")

# end all messages for a specific user


@ api_view(['DELETE'])  # @@@@@@@@@@@ need to understand
@ renderer_classes([JSONRenderer])  # @@@@@@@@@@@ need to understand
def deleteMessage(request, user, id):
    delete_message = Message_contains.objects.filter(
        Q(sender=user, id=id) | Q(receiver=user, id=id))
    if not delete_message:
        return Response("Wrong user name or id")
    else:
        delete_message.delete()
        return Response("The message deleted successfully", status=status.HTTP_200_OK)
