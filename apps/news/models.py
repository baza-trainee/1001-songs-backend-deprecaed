from django.db import models

from .choices import TYPES_NEWS


class News(models.Model):
    class Meta:
        db_table = 'news'
        ordering = ['-created_at']
        verbose_name = "News"
        verbose_name_plural = "News"

    news_title = models.CharField(max_length=200)
    type_of_news = models.CharField(max_length=40, choices=TYPES_NEWS)
    date = models.DateField()
    location = models.CharField(max_length=200)
    photo_1 = models.ImageField(blank=True)
    text_1 = models.TextField(blank=True)
    photo_2 = models.ImageField(blank=True)
    text_2 = models.TextField(blank=True)
    author = models.CharField(max_length=100, blank=True)
    editor = models.CharField(max_length=100, blank=True)
    svitliny = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
