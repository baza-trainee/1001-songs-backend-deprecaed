from django.db.models import Count
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.songs.models import Song
from apps.songs.serializers import SongSerializer


class MapListView(GenericAPIView):
    """
    List of songs by city
    """
    @staticmethod
    def get(*args, **kwargs):
        # не работает на версии джанго под рендер
        result_count = (Song.objects.all().values('location__official_name_city', 'location__coordinates')
                        .annotate(count=Count('location__official_name_city')))
        return Response(result_count)


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