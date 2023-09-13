from django.db.models import Count
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.songs.models import Song
from apps.songs.serializers import SongSerializer


class MapListView(GenericAPIView):
    @staticmethod
    def get(*args, **kwargs):
        result_count = Song.objects.all().values('location__region').annotate(Count('location__region'))
        return Response(result_count)


class MapRegionListView(GenericAPIView):
    queryset = Song.objects.all()

    def get(self, *args, **kwargs):
        params = self.request.query_params.dict()
        if params:
            songs_region = Song.objects.filter(location__region=params['region'])
            serializer = SongSerializer(instance=songs_region, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('Specify the search region', status=status.HTTP_404_NOT_FOUND)

