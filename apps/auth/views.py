from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .swagger.decorators import response_with_user_swagger, response_refresh_swagger
from apps.auth.serializers import CustomTokenObtainPairSerializer, CustomTokenRefreshSerializers
from apps.users.serializers import UserSerializer


@response_with_user_swagger()
class AuthRegisterView(CreateAPIView):
    """
        Register User
    """
    serializer_class = UserSerializer


@response_with_user_swagger()
class CustomTokenObtainPairView(TokenObtainPairView):
    """
        Login User
    """
    serializer_class = CustomTokenObtainPairSerializer


@response_refresh_swagger()
class CustomTokenRefreshView(TokenRefreshView):
    """
        Refresh
    """
    serializer_class = CustomTokenRefreshSerializers
