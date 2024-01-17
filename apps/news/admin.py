from django.contrib import admin

from apps.news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'type_of_news', 'date', 'location')
    list_filter = ('type_of_news', 'date')
    search_fields = ('news_title', 'location')
