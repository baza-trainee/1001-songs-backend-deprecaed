from django.urls import path

from .views import SongAndMarkersListaView

urlpatterns = [
    path('', SongAndMarkersListaView.as_view(), name='list_songs'),
]
