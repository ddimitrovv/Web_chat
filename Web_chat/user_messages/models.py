from django.db import models

from Web_chat.users.models import CustomUser


class CustomMessage(models.Model):
    MESSAGE_MAX_LEN = 250

    sender = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        on_update=models.CASCADE,
        related_name='sent_messages'
    )
    recipient = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        on_update=models.CASCADE,
        related_name='received_messages'
    )
    content = models.TextField(max_length=MESSAGE_MAX_LEN)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    # Set to true when the message is seen by the recipient.
    def mark_as_seen(self):
        self.is_seen = True
        self.save()

    # Mark the message as deleted instead of deleting the message.
    def mark_as_deleted(self):
        self.is_deleted = True
        self.save()

    def __str__(self):
        return f"From: {self.sender} | To: {self.recipient} | {self.content[:50]}"
