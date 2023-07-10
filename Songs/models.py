import uuid
from django.db import models


class Songs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(max_length=600, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "songs"
        ordering = ['-createdAt']
        verbose_name = "Song"
        verbose_name_plural = "Songs"

    def __str__(self) -> str:
        return self.title
