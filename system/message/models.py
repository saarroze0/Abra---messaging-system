from django.db import models


class Message_contains(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.CharField(max_length=25)
    receiver = models.CharField(max_length=25)
    message = models.TextField()
    subject = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    unread_messages = models.BooleanField(default=True)
