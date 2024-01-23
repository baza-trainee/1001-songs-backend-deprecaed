from django.db import models


class Footer(models.Model):

    reporting = models.FileField(blank=True)
    privacy_policy = models.FileField(blank=True)
    rules_and_terms = models.FileField(blank=True)
    email = models.URLField(max_length=250, blank=True)
    facebook = models.URLField(max_length=250, blank=True)
    youtube = models.URLField(max_length=250, blank=True)
