from django.contrib import admin

from .models import Message_contains


class Message_contains_admin(admin.ModelAdmin):
    list_filter = ("sender", "creation_date", "unread_messages")
    list_display = ("sender", "receiver", "subject")


admin.site.register(Message_contains, Message_contains_admin)
