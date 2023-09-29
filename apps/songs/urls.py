from django.urls import path

from .views import SongListCreateView, SongRetrieveUpdateDestroyView , SongsByLocationView

urlpatterns = [
    path('', SongListCreateView.as_view(), name='list_crate_song'),
    path('/<uuid:pk>', SongRetrieveUpdateDestroyView.as_view(), name='songs_retrieve_update_destroy_view'),
    path('_location/', SongsByLocationView.as_view(), name='songs-by-location'),
]
