from django.urls import re_path
from rest_framework_simplejwt.views import TokenRefreshView

from {{ project_name }}.authentication.views import TokenObtainPairView

urlpatterns = [
    re_path(r'token/obtain/?', TokenObtainPairView.as_view(), name='token_create'),
    re_path(r'token/refresh/?', TokenRefreshView.as_view(), name='token_refresh'),
]
