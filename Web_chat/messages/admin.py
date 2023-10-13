from django.contrib import admin

from Web_chat.messages.models import CustomMessage


@admin.register(CustomMessage)
class CustomMessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'recipient', 'content', 'timestamp']
