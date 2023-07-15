from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.auth.serializers import TokenWithUserSerializer
from apps.users.serializers import UserSerializer


class AuthRegisterView(CreateAPIView):
    serializer_class = UserSerializer


class TokenWithUserView(TokenObtainPairView):
    serializer_class = TokenWithUserSerializer


