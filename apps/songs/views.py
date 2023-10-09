from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.songs.models import Song
from apps.songs.serializers import SongSerializer

from django_filters.rest_framework import DjangoFilterBackend

from django.db.models import Q
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
    - location: The official city name where the songs were recorded.

    Usage Example:
    GET /songs_by_location/?location=Kyiv
    """
    serializer_class = SongSerializer

    def get_queryset(self, official_name_city):
        try:
            return Song.objects.filter(Q(location__official_name_city__iexact=official_name_city) | Q(location__official_name_city__icontains=official_name_city))
        except Exception as e:
            return None

    def get(self, request, *args, **kwargs):
        location = self.request.query_params.get('location', None)
        if not location:
            return Response({"error": "Location parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        queryset = self.get_queryset(location)
        if queryset is None:
            return Response({"error": "An error occurred while fetching data"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        elif not queryset.exists():
            return Response({"error": "No data found for the specified location"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
