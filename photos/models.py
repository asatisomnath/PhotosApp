from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models

from model_utils.models import SoftDeletableModel
from model_utils.models import StatusModel
from model_utils.models import TimeStampedModel
from model_utils import Choices

from easy_thumbnails.fields import ThumbnailerImageField


def get_photo_upload_path(instance, filename):
    return f'{instance.uuid}/{filename}'


class Photo(StatusModel, SoftDeletableModel, TimeStampedModel):
    STATUS = Choices('draft', 'published')

    uuid = models.UUIDField(default=uuid4, db_index=True, unique=True, editable=False, help_text='This photo UUID.')

    image = ThumbnailerImageField(upload_to=get_photo_upload_path, help_text='Actual photo media file path.')

    uploaded_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='+', help_text='User who uploaded this photo.')
    captions = models.TextField(default='', blank=True, help_text='Additional text description for this photo.')
