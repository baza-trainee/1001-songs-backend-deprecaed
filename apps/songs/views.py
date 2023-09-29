from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.songs.models import Song
from apps.songs.serializers import SongSerializer

from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import get_list_or_404
from rest_framework import generics, status
from rest_framework.response import Response


class SongListCreateView(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [
        'location__country',
        'location__region',
        'location__ethnographic_district',
        'details__genre_cycle',
    ]
    search_fields = ['title']
    ordering_fields = ['title', 'recording_date']
    ordering = ['title']


class SongRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Song
    serializer_class = SongSerializer

class SongsByLocationView(generics.GenericAPIView):
    """
    Retrieve a list of songs recorded in a specific location.

    Parameters:
    - location: The country where the songs were recorded.

    Usage Example:
    GET /songs_by_location/?location=Ukraine
    """
    serializer_class = SongSerializer

    def get_queryset(self, location):
        try:
            return get_list_or_404(Song, location__country=location)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, *args, **kwargs):
        location = self.request.query_params.get('location', None)
        if not location:
            return Response({"error": "Location parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            queryset = self.get_queryset(location)
        except Exception as e:
            return Response({"error": "An error occurred while fetching data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
