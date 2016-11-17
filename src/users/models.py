from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    session_token = models.CharField('Session token', max_length=255, null=True, blank=True)
