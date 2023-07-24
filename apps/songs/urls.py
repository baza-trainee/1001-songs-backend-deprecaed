from django.urls import path

from .views import SongListCreateView, SongRetrieveUpdateDestroyView

urlpatterns = [
    path('', SongListCreateView.as_view(), name='list_crate_song'),
    path('/<int:pk>', SongRetrieveUpdateDestroyView.as_view(), name='songs_retrieve_update_destroy_view'),
]
