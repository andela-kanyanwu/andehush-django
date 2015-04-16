from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Message(models.Model):
    listener = models.ForeignKey(User)
    anonymous_user = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
