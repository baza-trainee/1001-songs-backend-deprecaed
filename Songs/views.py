from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from Songs.models import Song
from Songs.serializers import SongSerializer


class SongsListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class SongsListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = SongsListPagination


class SongsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
