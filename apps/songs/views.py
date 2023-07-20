from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.songs.models import Song
from apps.songs.serializers import SongSerializer


class SongListCreateView(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Song
    serializer_class = SongSerializer
