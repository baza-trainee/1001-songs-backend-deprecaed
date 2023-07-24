from django.urls import path

from apps.staticmap.views import MapListView

urlpatterns = [
    path('', MapListView.as_view(), name='list_map'),
]
