import uuid
from django.db import models
# from django.contrib.gis.db import models
# from django.contrib.gis.geos import Point


class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, unique=True)

    #TODO добавити вибір меж створення
    recording_date = models.DateField(null=True, blank=True)

    country = models.CharField(max_length=100, default='Ukraine')
    region = models.CharField(max_length=100)
    district_center = models.CharField(max_length=100)  # Район.центр для науковців
    administrative_center = models.CharField(max_length=100)  # Адмін. код для науковців
    ethnicity = models.CharField(max_length=100)
    ethnographic_district = models.CharField(max_length=100)
    # TODO доробити геолокацію
    # location = models.PointField(geography=True, default=Point(0.0, 0.0))

    official_name = models.CharField(max_length=100)
    unofficial_name = models.CharField(max_length=100, blank=True)
    recording_location = models.CharField(max_length=100, blank=True)  # Місце запису Науковці

    performers = models.CharField(max_length=200)
    collectors = models.CharField(max_length=200)

    incipit = models.DateField(max_length=100)
    genre_cycle = models.CharField(max_length=100)
    poetic_text_genre = models.CharField(max_length=100)  # Жанр поетичного тексту науковці
    texture = models.CharField(max_length=100, blank=True)

    source = models.CharField(max_length=200)
    # тут добавити поле вибору архів, фонд, джерело
    bibliographic_reference = models.CharField(max_length=200, blank=True)
    researcher_comment = models.TextField(blank=True)

    # Добавити аудіо 2 варіанти, відео, текст, ноти, фото виконавців

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "songs"
        ordering = ['-created_at']
        verbose_name = "Song"
        verbose_name_plural = "Songs"

    def __str__(self) -> str:
        return self.title
