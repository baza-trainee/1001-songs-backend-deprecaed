from django.urls import path

from apps.staticmap.views import MapListView, MapRegionListView

urlpatterns = [
    path('', MapListView.as_view(), name='list_map'),
    path('/city', MapRegionListView.as_view(), name='region_list_map'),
]
