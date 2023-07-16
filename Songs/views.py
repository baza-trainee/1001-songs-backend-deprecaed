from rest_framework import generics

from Songs.models import Song
from Songs.serializers import SongSerializer
from core import BasicPagePaginator


class SongsListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = BasicPagePaginator


class SongsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
