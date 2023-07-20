from rest_framework.generics import ListCreateAPIView

from apps.songstest.models import SongsTestModel
from apps.songstest.serializers import SongsTestSerializers


class SongsTestListCreateView(ListCreateAPIView):
    queryset = SongsTestModel.objects.all()
    serializer_class = SongsTestSerializers
