from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from Songs.models import Songs
from Songs.serializers import SongsSerializer


class SongsListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class SongsListCreateView(generics.ListCreateAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    pagination_class = SongsListPagination


class SongsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
