from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.songs.models import Song
from apps.songs.serializers import SongSerializer

from django_filters.rest_framework import DjangoFilterBackend


class SongListCreateView(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [
        'location__country',
        'location__region',
        'location__ethnographic_district',
        'details__genre_cycle'
    ]
    search_fields = ['title']
    ordering_fields = ['title', 'recording_date']
    ordering = ['title']


class SongRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Song
    serializer_class = SongSerializer
