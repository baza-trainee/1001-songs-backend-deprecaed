

from django.urls import path

from .views import NewsDetailView,   NewsDetailView,  NewsListDetailView

urlpatterns = [
    path('', NewsDetailView.as_view(), name='list_create_news'),
    path('<int:pk>/', NewsDetailView.as_view(), name='list_create_news'),
    path('_detail/', NewsListDetailView.as_view(), name='news_list_create_view'),
    path('_detail/<int:pk>/', NewsDetailView.as_view(), name='news_retrieve_view')
]

