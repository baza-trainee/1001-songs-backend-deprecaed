from django_filters import rest_framework as filters

from .models import Song


class SongFilter(filters.FilterSet):
    class Meta:
        model = Song
        fields = (
            'country', 'region', 'city', 'genre', 'title', 'archive',
        )

    country = filters.CharFilter(field_name='location__country', lookup_expr='icontains')
    region = filters.CharFilter(field_name='location__region', lookup_expr='icontains')
    city = filters.CharFilter(field_name='location__official_name_city', lookup_expr='icontains')
    genre = filters.CharFilter(field_name='details__genre_cycle', lookup_expr='icontains')
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    archive = filters.CharFilter(field_name='archive', lookup_expr='icontains')
