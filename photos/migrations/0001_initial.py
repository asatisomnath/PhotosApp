# Generated by Django 2.2.8 on 2020-04-25 09:38

from django.conf import settings
from django.db import migrations, models
import easy_thumbnails.fields
import django.utils.timezone
import model_utils.fields
import photos.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[('draft', 'draft'), ('published', 'published')], default='draft', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('is_removed', models.BooleanField(default=False)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='This photo UUID.', unique=True)),
                ('image', models.ImageField(help_text='Actual photo media file path.', upload_to=photos.models.get_photo_upload_path)),
                ('captions', models.TextField(blank=True, help_text='Additional text description for this photo.', null=True)),
                ('uploaded_by', models.ForeignKey(help_text='User who uploaded this photo.', on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='photo',
            name='captions',
            field=models.TextField(blank=True, default='', help_text='Additional text description for this photo.'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(help_text='Actual photo media file path.',
                                                               upload_to=photos.models.get_photo_upload_path),
        ),
    ]
