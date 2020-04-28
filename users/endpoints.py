from rest_framework_jwt.views import obtain_jwt_token

from django.urls import path

app_name = 'users'
urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
]
