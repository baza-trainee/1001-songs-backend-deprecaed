from django_filters import rest_framework as filters

from .choices import TYPES_NEWS
from .models import News


class NewsFilter(filters.FilterSet):
    class Meta:
        model = News
        fields = ('type',)

    type = filters.MultipleChoiceFilter(field_name='type_of_news', choices=TYPES_NEWS, lookup_expr='exact')
