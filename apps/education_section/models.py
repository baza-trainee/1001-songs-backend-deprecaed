from django.db import models


class EducationalSection(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

