from django.db import models

from .choices import GENRE_CYCLE_CHOICES


class Song(models.Model):
    title = models.CharField(max_length=200, unique=True)
    recording_date = models.DateField()
    performers = models.CharField(max_length=200)
    collectors = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    bibliographic_reference = models.TextField(blank=True)
    researcher_comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = "songs_db"
        ordering = ['-created_at']
        verbose_name = "Song"
        verbose_name_plural = "Songs"

    def __str__(self) -> str:
        return self.title


class SongLocation(models.Model):
    song = models.OneToOneField(Song, on_delete=models.CASCADE, related_name='location')
    country = models.CharField(max_length=100, default='Ukraine')
    region = models.CharField(max_length=100)
    district_center = models.CharField(max_length=100)
    administrative_code = models.CharField(max_length=100)
    ethnos = models.CharField(max_length=100)
    ethnographic_district = models.CharField(max_length=100)
    official_name_city = models.CharField(max_length=100)
    unofficial_name_city = models.CharField(max_length=100)
    recording_location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'location'
        ordering = ['-created_at']
        verbose_name = "Song Location"
        verbose_name_plural = "Songs Locations"

    def __str__(self) -> str:
        return self.song.title


class SongDetail(models.Model):
    song = models.OneToOneField(Song, on_delete=models.CASCADE, related_name='details')
    incipit = models.CharField(max_length=100)
    genre_cycle = models.CharField(max_length=30, choices=GENRE_CYCLE_CHOICES)
    poetic_text_genre = models.CharField(max_length=100)
    texture = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'details'
        ordering = ['-created_at']
        verbose_name = "Song Details"
        verbose_name_plural = "Songs Details"

    def __str__(self) -> str:
        return self.song.title


class SongMedia(models.Model):
    song = models.OneToOneField(Song, on_delete=models.CASCADE, related_name='media')
    stereo_audio = models.FileField(upload_to='audios/stereo/', blank=True)
    multichannel_audio = models.FileField(upload_to='audios/multichannel/', blank=True)
    video_file = models.FileField(upload_to='videos/', blank=True)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'media'
        ordering = ['-created_at']
        verbose_name = "Song Media"
        verbose_name_plural = "Songs Media"

    def __str__(self) -> str:
        return self.song.title
