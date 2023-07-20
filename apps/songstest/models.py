from django.db import models

from Songs.choices import GENRE_CYCLE_CHOICES


class SongsTestModel(models.Model):
    class Meta:
        db_table = 'songstest'

    title = models.CharField(max_length=200, unique=True)
    recording_date = models.DateField()
    performers = models.CharField(max_length=200)
    collectors = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    bibliographic_reference = models.CharField(max_length=200, blank=True)
    researcher_comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class SongTestLocationModel(models.Model):
    song = models.OneToOneField(SongsTestModel, on_delete=models.CASCADE, related_name='location')
    country = models.CharField(max_length=100, default='Ukraine')
    region = models.CharField(max_length=100)
    district_center = models.CharField(max_length=100)
    administrative_center = models.CharField(max_length=100)
    ethnicity = models.CharField(max_length=100)
    ethnographic_district = models.CharField(max_length=100)
    official_name = models.CharField(max_length=100)
    unofficial_name = models.CharField(max_length=100)
    recording_location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SongTestDetailsModel(models.Model):
    song = models.OneToOneField(SongsTestModel, on_delete=models.CASCADE, related_name='details')
    incipit = models.CharField(max_length=100)
    genre_cycle = models.CharField(max_length=30, choices=GENRE_CYCLE_CHOICES)
    poetic_text_genre = models.CharField(max_length=100)
    texture = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SongTestMediaModel(models.Model):
    song = models.OneToOneField(SongsTestModel, on_delete=models.CASCADE, related_name='media')
    stereo_audio = models.FileField(upload_to='audios/stereo/', blank=True)
    multichannel_audio = models.FileField(upload_to='audios/multichannel/', blank=True)
    video_file = models.FileField(upload_to='videos/', blank=True)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
