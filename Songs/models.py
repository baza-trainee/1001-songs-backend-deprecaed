import uuid
from Songs.choices import GENRE_CYCLE_CHOICES
from django.db import models


class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, unique=True)
    recording_date = models.DateField(null=True, blank=True)
    performers = models.CharField(max_length=200)
    collectors = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    bibliographic_reference = models.CharField(max_length=200, blank=True)
    researcher_comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "songs"
        ordering = ['-created_at']
        verbose_name = "Song"
        verbose_name_plural = "Songs"

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SongLocation.objects.get_or_create(song=self)
        SongDetails.objects.get_or_create(song=self)
        SongMedia.objects.get_or_create(song=self)


class SongLocation(models.Model):
    song = models.OneToOneField(Song, on_delete=models.CASCADE, primary_key=True)
    country = models.CharField(max_length=100, default='Ukraine')
    region = models.CharField(max_length=100)
    district_center = models.CharField(max_length=100)
    administrative_center = models.CharField(max_length=100)
    ethnicity = models.CharField(max_length=100)
    ethnographic_district = models.CharField(max_length=100)
    official_name = models.CharField(max_length=100)
    unofficial_name = models.CharField(max_length=100, blank=True)
    recording_location = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Song Location"
        verbose_name_plural = "Songs Locations"

    def __str__(self) -> str:
        return self.song.title


class SongDetails(models.Model):
    song = models.OneToOneField(Song, on_delete=models.CASCADE, primary_key=True)
    incipit = models.CharField(max_length=100)
    genre_cycle = models.CharField(max_length=30, choices=GENRE_CYCLE_CHOICES)
    poetic_text_genre = models.CharField(max_length=100)
    texture = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Song Details"
        verbose_name_plural = "Songs Details"

    def __str__(self) -> str:
        return self.song.title


class SongMedia(models.Model):
    song = models.OneToOneField(Song, on_delete=models.CASCADE, primary_key=True)
    stereo_audio = models.FileField(upload_to='audios/stereo/')
    multichannel_audio = models.FileField(upload_to='audios/multichannel/', blank=True)
    video_file = models.FileField(upload_to='videos/', blank=True)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Song Media"
        verbose_name_plural = "Songs Media"

    def __str__(self) -> str:
        return self.song.title
