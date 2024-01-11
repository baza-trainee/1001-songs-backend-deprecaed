from django.contrib import admin

from apps.news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('type_of_news', 'date', 'news_title', 'location')
    list_filter = ('type_of_news', 'date')
    search_fields = ('news_title', 'location')
