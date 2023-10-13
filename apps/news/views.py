from rest_framework import generics
from .models import News, NewsDetail
from .serializers import NewsSerializer, NewsDetailsSerializer


class NewsDetailView(generics.RetrieveAPIView):
    """
    Retrieve information about a specific news item.

    Allowed methods:
    - GET: Retrieve information about a news item using its identifier (pk).

    URL:
    - /news/<int:pk>/

    Parameters:
    - pk: News item identifier (integer).

    Example:
    - /news/1/
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    http_method_names = ['get']


class NewsListDetailView(generics.ListCreateAPIView):
    """
    Get a list of news details and create new news details.

    Allowed methods:
    - GET: Retrieve a list of news details.
    - POST: Create a new news detail.

    URL:
    - /news/_detail/

    Example:
    - /news/_detail/
    """
    queryset = NewsDetail.objects.all()
    serializer_class = NewsDetailsSerializer
    http_method_names = ['get']


class NewsDetailView(generics.RetrieveAPIView):
    """
    Retrieve information about a specific news detail.

    Allowed methods:
    - GET: Retrieve information about a news detail using its identifier (pk).

    URL:
    - /news/_detail/<int:pk>/

    Parameters:
    - pk: News detail identifier (integer).

    Example:
    - /news/_detail/1/
    """
    queryset = NewsDetail.objects.all()
    serializer_class = NewsDetailsSerializer
    http_method_names = ['get']
