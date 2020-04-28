from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('users/', include('users.endpoints', namespace='users')),
    path('photos/', include('photos.endpoints', namespace='photos')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
