from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from .models import Message_contains
from .serializers import MessageSerializer
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST'])
@renderer_classes([JSONRenderer])
def sendMessage(request):
    current_user = request.user
    newMessage = Message_contains(
        sender=current_user,
        receiver=request.data["receiver"],
        message=request.data["message"],
        subject=request.data["subject"],
    )
    newMessage.save()
    return Response("New message send", status=status.HTTP_200_OK)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def inbox(request):
    current_user = request.user
    receiver_messages = Message_contains.objects.filter(receiver=current_user)
    serializer = MessageSerializer(receiver_messages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def unread_inbox(request):
    current_user = request.user
    receiver_messages = Message_contains.objects.filter(
        receiver=current_user, unread_messages=True)
    if receiver_messages.values('unread_messages') == 0:
        return Response("No more messages available")

    serializer = MessageSerializer(receiver_messages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def readMessage(request, id):
    try:
        current_user = request.user
        receiver_message = Message_contains.objects.get(pk=(id),receiver=current_user)
        if receiver_message.unread_messages != False:
        # if str(receiver_message.receiver) == str(current_user) and (receiver_message.unread_messages != False):
            receiver_message.unread_messages = False
            receiver_message.save()
        serializer = MessageSerializer(receiver_message)
        return Response(serializer.data, status=status.HTTP_200_OK)

            # return Response("There are no unread messages")
    except ObjectDoesNotExist:
        return Response("There are no such messages")


@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
def deleteMessage(request, id):
    current_user = request.user
    delete_message = Message_contains.objects.filter(
        Q(sender=current_user, id=id) | Q(receiver=current_user, id=id))
    if not delete_message:
        return Response("Wrong user name or id")
    else:
        delete_message.delete()
        return Response("The message deleted successfully", status=status.HTTP_200_OK)

# @api_view(['POST'])
# @renderer_classes([JSONRenderer])
# def csrf_failure(request, reason=""):
#     ctx = {'message': 'some custom messages'}
#     return Response("You have successfully registered", status=status.HTTP_200_OK)