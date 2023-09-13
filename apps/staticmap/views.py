from django.db.models import Count
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.songs.models import Song


class MapListView(GenericAPIView):
    @staticmethod
    def get(*args, **kwargs):
        result_count = Song.objects.all().values('location__region').annotate(Count('location__region'))
        return Response(result_count)
