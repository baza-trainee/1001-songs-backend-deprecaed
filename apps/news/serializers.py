from rest_framework.serializers import ModelSerializer
from apps.news.models import News


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = (
            'news_title', 'type_of_news', 'date', 'location', 'photo_1', 'text_1', 'photo_2', 'text_2', 'author',
            'editor', 'svitliny',
        )
