from django_filters import rest_framework as filters

from .models import Song


class SongFilter(filters.FilterSet):
    class Meta:
        model = Song
        fields = (
            'title', 'country', 'region', 'city', 'genre', 'archive', 'coordinates',
        )
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    country = filters.BaseInFilter(field_name='location__country', lookup_expr='in')
    region = filters.BaseInFilter(field_name='location__region', lookup_expr='in')
    city = filters.BaseInFilter(field_name='location__official_name_city', lookup_expr='in')
    genre = filters.BaseInFilter(field_name='details__genre_cycle', lookup_expr='in')
    archive = filters.BaseInFilter(field_name='archive', lookup_expr='in')
    coordinates = filters.CharFilter(field_name='location__coordinates', lookup_expr='exact')
