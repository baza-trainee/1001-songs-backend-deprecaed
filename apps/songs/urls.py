from django.urls import path

from .views import SongListView, SongRetrieveView, SongsByLocationView

urlpatterns = [
    path('', SongListView.as_view(), name='list_songs'),
    path('/<uuid:pk>', SongRetrieveView.as_view(), name='retrieve_song'),
    path('_location/', SongsByLocationView.as_view(), name='songs-by-location'),
]
