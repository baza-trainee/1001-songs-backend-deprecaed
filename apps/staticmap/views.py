from django.db.models import Count
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.songs.models import Song


class MapListView(GenericAPIView):
    def get(self, *args, **kwargs):
        params = self.request.query_params.dict()
        if params:
            result_count = Song.objects.all().filter(location__region=params['region']).count()
            return Response(result_count)
        else:
            result_count = Song.objects.all().values('location__region').annotate(Count('location__region'))
            return Response(result_count)
