from django.db import models
import uuid
# Create your models here.
from apps.news.choices import TYPES


class News(models.Model):
    type_of_news = models.CharField(max_length=20, choices=TYPES)
    date = models.DateField()
    news_title = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    photo = models.URLField(blank=True)
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"


class NewsDetail(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    news_title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    photo1 = models.URLField(blank=True)
    text1 = models.TextField(blank=True)
    photo2 = models.URLField(blank=True)
    text2 = models.TextField(blank=True)
    author = models.CharField(max_length=200, blank=True)
    editor = models.CharField(max_length=200, blank=True)
    photos = models.ManyToManyField(News, blank=True, related_name='related_news_details')

    class Meta:
        verbose_name = "News Detail"
        verbose_name_plural = "News Details"


