import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from {{ project_name }}.profiles.models import User


@pytest.fixture
def api_client():
    user = User.objects.create_user(username='fulano', password='django123')
    client = APIClient()
    client.login(username='fulano', password='django123')
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    authorization = str(refresh.access_token)

    return {
        "client": client,
        "Authorization": authorization
    }
