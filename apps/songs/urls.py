from django.urls import path

from .views import SongAndMarkersListaView, SongRetrieveView

urlpatterns = [
    path('', SongAndMarkersListaView.as_view(), name='list_songs'),
    path('/<uuid:pk>', SongRetrieveView.as_view(), name='retrieve_song'),
]
