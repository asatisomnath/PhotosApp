from django.urls import path

from .views import PhotoView

app_name = 'photos'
urlpatterns = [
    path('', PhotoView.as_view({'get': 'list', 'post': 'create'})),
    path('<uuid>', PhotoView.as_view({'put': 'update', 'delete': 'destroy'})),
]
