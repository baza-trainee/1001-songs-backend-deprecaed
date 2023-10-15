from django.db import models

from .choiсes_types_expedition import TYPE_EXPEDITION_CHOICES

class Expedition(models.Model):
    class Meta:
        db_table = "expeditions"
        ordering = ['-created_at']
        verbose_name = "Expedition"
        verbose_name_plural = "Expeditions"

    title = models.CharField(max_length=50)
    date_event = models.DateField()
    brief_description = models.CharField(max_length=250)
    location = models.CharField(max_length=100)
    type_expedition = models.CharField(max_length=50, choices=TYPE_EXPEDITION_CHOICES)
    coordinates = models.CharField(max_length=30)
    text_1_intro = models.TextField(blank=True)
    video_1 = models.URLField(blank=True)
    text_2 = models.TextField(blank=True)
    text_3_paragraph = models.TextField(blank=True)
    text_4 = models.TextField(blank=True)
    subtitle_1 = models.CharField(max_length=50, blank=True)
    text_5 = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    comment_to_photo = models.CharField(max_length=100, blank=True)
    text_6 = models.TextField(blank=True)
    video_2 = models.URLField(blank=True)
    comment_to_video_2 = models.CharField(max_length=100, blank=True)
    text_7 = models.TextField(blank=True)
    video_3 = models.URLField(blank=True)
    comment_to_video_3 = models.CharField(max_length=100, blank=True)
    subtitle_2 = models.CharField(max_length=50, blank=True)
    text_8 = models.TextField(blank=True)
    video_4 = models.URLField(blank=True)
    comment_to_video_4 = models.CharField(max_length=100, blank=True)
    text_9 = models.TextField(blank=True)
    subtitle_3_sources = models.CharField(max_length=50, blank=True)
    text_10 = models.TextField(blank=True)
    subtitle_4_materials_prepared = models.CharField(max_length=50, blank=True)
    collectors = models.CharField(max_length=200, blank=True)
    editor = models.CharField(max_length=20, blank=True)
    video_inst = models.CharField(max_length=50, blank=True)
    record = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

