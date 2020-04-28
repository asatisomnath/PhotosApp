from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    uuid = models.UUIDField(default=uuid4, unique=True, db_index=True, editable=False, help_text='User\'s UUID.')
