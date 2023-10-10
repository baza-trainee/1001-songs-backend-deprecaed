from rest_framework import generics
from .models import NewsDetail
from apps.news.serializers import NewsDetailSerializer


class NewsDetailList(generics.ListCreateAPIView):
    queryset = NewsDetail.objects.all()
    serializer_class = NewsDetailSerializer


class NewsDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsDetail.objects.all()
    serializer_class = NewsDetailSerializer
