from django.db.models import Count

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Song
from .serializers import SongSerializer
from .filters import SongFilter


class SongAndMarkersListaView(GenericAPIView):
    """
    List of songs and markers
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filterset_class = SongFilter

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        list_markers = (queryset.values('location__official_name_city', 'location__coordinates')
                        .annotate(count=Count('location__official_name_city')))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response([f'list_songs', serializer.data, f'list_markers', list_markers])
