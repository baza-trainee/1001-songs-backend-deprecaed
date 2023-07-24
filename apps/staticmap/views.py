from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.songs.models import Song
from apps.songs.serializers import SongSerializer


# class MapListView(GenericAPIView):
#     def get(self, *args, **kwargs):
#         qs = Song.objects.select_related('region').count()
#         list1 = [a for a in qs.o]
#         serializer = SongSerializer(instance=qs, many=True)
#         print(list1)
#
#         return Response(qs)
