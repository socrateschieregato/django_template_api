
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from {{ project_name }}.authentication.serializers import CustomTokenObtainPairSerializer


class TokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email

        return token


class TokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
