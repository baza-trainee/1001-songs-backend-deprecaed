from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.songs.models import SongModel
from apps.songs.serializers import SongSerializer


class SongListCreateView(ListCreateAPIView):
    queryset = SongModel.objects.all()
    serializer_class = SongSerializer


class SongRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = SongModel
    serializer_class = SongSerializer
