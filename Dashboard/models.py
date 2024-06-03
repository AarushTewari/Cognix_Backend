from django.db import models
import uuid
from django.contrib.auth.models import User

class AppUser(models.Model):
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'app_user')
    static_id = models.UUIDField(max_length=36, unique=True, default=uuid.uuid4, editable=False)


chat_status = [
    ("Accepted", "Accepted"),
    ("Declined", "Declined"),
    ("Pending", "Pending")
]
class ChatRequest(models.Model):
    static_id = models.UUIDField(max_length=36, unique=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="sender")
    reciever = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="reciever")
    status = models.CharField(max_length=40, choices=chat_status, default="Pending")