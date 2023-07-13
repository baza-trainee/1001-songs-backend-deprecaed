from rest_framework.generics import CreateAPIView

from apps.users.serializers import UserSerializer


class AuthRegisterView(CreateAPIView):
    serializer_class = UserSerializer
