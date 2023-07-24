from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.songs.models import Song


class MapListView(GenericAPIView):
    def get(self, *args, **kwargs):
        params = self.request.query_params.dict()
        result_count = Song.objects.filter(location__region__in=params['region']).count()
        return Response(result_count)
