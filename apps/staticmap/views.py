from django.db.models import Count
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.songs.models import Song
from apps.songs.serializers import SongSerializer


class MapListView(GenericAPIView):
    """
    List of songs with cities, lists of cities and archives
    """
    queryset = Song.objects.all()

    @staticmethod
    def get(*args, **kwargs):
        list_markers = (Song.objects.values('location__city_ua', 'location__coordinates')
                        .annotate(count=Count('location__city_ua')))
        list_cities = (Song.objects.order_by('location__city_ua').values('location__city_ua', 'location__city_eng')
                       .distinct('location__city_ua'))
        list_archives = (Song.objects.order_by('archive_ua').values('archive_ua', 'archive_eng')
                         .distinct('archive_ua'))
        return Response([
            {'list_markers': list_markers},
            {'list_cities': list_cities},
            {'list_archives': list_archives}
        ])


class MapCityListView(GenericAPIView):
    """
    List of songs in the selected city
    """
    queryset = Song.objects.all()

    def get(self, *args, **kwargs):
        params = self.request.query_params.dict()
        if params:
            songs_city = Song.objects.filter(location__city_ua=params['city_ua'])
            serializer = SongSerializer(instance=songs_city, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('Specify the search city', status=status.HTTP_404_NOT_FOUND)
