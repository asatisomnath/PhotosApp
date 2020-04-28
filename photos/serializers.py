from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.SlugRelatedField(slug_field='uuid', required=False, queryset=get_user_model().objects.all(), help_text='UUID of the user who uploaded the photo.')
    image = serializers.ImageField(required=False, write_only=True, help_text='Photo image file.')
    thumbnail = serializers.SerializerMethodField(help_text='Photo thumbnail.')

    class Meta:
        model = Photo
        fields = ['uuid', 'thumbnail', 'uploaded_by', 'status', 'image', 'captions', 'status_changed']
        read_only_fields = ['uuid', 'thumbnail', 'uploaded_by']

    def get_thumbnail(self, obj):
        return self.context['request'].build_absolute_uri(obj.image['thumbnail'].url)

    def validate_image(self, value):
        if self.instance:
            raise ValidationError('Can\'t change already uploaded image file.')
        return value

    def validate_status(self, value):
        if self.instance and value == 'draft':
            raise ValidationError('Can\'t make already published photo a draft.')
        return value

    def validate(self, attrs):
        if not self.instance and not attrs.get('image'):
            raise ValidationError('No image was submitted.')
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data['uploaded_by'] = self.context['request'].user
        return super().create(validated_data)

