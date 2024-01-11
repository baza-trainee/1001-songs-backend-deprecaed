from django.urls import path

from .views import NewsListView, NewsByIdView

urlpatterns = [
    path('', NewsListView.as_view(), name='list_news'),
    path('/<int:pk>', NewsByIdView.as_view(), name='by_id_news'),
]
