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
    @staticmethod
    def get(*args, **kwargs):
        result_count = (Song.objects.all().values('location__official_name_city', 'location__coordinates')
                        .annotate(count=Count('location__official_name_city')))
        archives = Song.objects.all().values('archive')
        cities = Song.objects.all().values('location__official_name_city')
        list_of_archives = {i for j in archives for i in j.values()}
        list_of_cities = {i for j in cities for i in j.values()}
        return Response([result_count, f'list_of_archives: {list_of_archives}, list_of_cities: {list_of_cities}'])


class MapCityListView(GenericAPIView):
    """
    List of songs in the selected city
    """
    queryset = Song.objects.all()

    def get(self, *args, **kwargs):
        params = self.request.query_params.dict()
        print(params)
        if params:
            songs_city = Song.objects.filter(location__official_name_city=params['official_name_city'])
            serializer = SongSerializer(instance=songs_city, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('Specify the search city', status=status.HTTP_404_NOT_FOUND)
