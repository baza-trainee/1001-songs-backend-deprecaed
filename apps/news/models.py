from django.db import models

# Create your models here.
from apps.news.choices import TYPES


class News(models.Model):
    type_of_news = models.CharField(max_length=20, choices=TYPES)
    date = models.DateField()
    news_title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    photo = models.URLField()


class NewsDetail(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    news_title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    photo1 = models.URLField()
    text1 = models.TextField()
    photo2 = models.ImageField()
    text2 = models.TextField()
    author = models.CharField(max_length=200)
    editor = models.CharField(max_length=200)
    photos = models.ManyToManyField(News, blank=True, related_name='related_news_details')


