from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Message_contains


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message_contains
        fields = ['sender', 'receiver', 'subject',  'message', 'creation_date']