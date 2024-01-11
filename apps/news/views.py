from rest_framework.generics import ListAPIView, RetrieveAPIView

from .filters import NewsFilter
from .models import News
from .serializers import NewsSerializer


class NewsListView(ListAPIView):
    """
    Retrieve information about a specific news item.

    Allowed methods:
    - GET: Retrieve information about a news item using its identifier (pk).

    URL:
    - /news

    Parameters:
    - pk: News item identifier (integer).

    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filterser_class = NewsFilter


class NewsByIdView(RetrieveAPIView):
    """
    Retrieve information about a specific news item.

    Allowed methods:
    - GET: Retrieve information about a news item using its identifier (pk).

    URL:
    - /news/<int:pk>

    Parameters:
    - pk: News item identifier (integer).

    Example:
    - /news/1
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
