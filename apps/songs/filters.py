from django_filters import rest_framework as filters

from .models import Song


class SongFilter(filters.FilterSet):
    class Meta:
        model = Song
        fields = (
            'country', 'region', 'district', 'genre', 'title', 'archive',
        )

    country = filters.CharFilter(field_name='location__country', lookup_expr='icontains')
    region = filters.CharFilter(field_name='location__region', lookup_expr='icontains')
    district = filters.CharFilter(field_name='location__district_center', lookup_expr='icontains')
    genre = filters.CharFilter(field_name='details__genre_cycle', lookup_expr='icontains')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    archive = filters.CharFilter(field_name='archive', lookup_expr='icontains')
