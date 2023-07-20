from django.db.transaction import atomic
from rest_framework.serializers import ModelSerializer

from apps.songs.models import SongModel, SongLocationModel, SongDetailModel, SongMediaModel


class SongLocationSerializer(ModelSerializer):
    class Meta:
        model = SongLocationModel
        fields = ('id', 'country', 'region', 'district_center', 'administrative_center', 'ethnicity',
                  'ethnographic_district', 'official_name', 'unofficial_name', 'recording_location',
                  )


class SongDetailSerializer(ModelSerializer):
    class Meta:
        model = SongDetailModel
        fields = ('id', 'incipit', 'genre_cycle', 'poetic_text_genre', 'texture')


class SongMediaSerializer(ModelSerializer):
    class Meta:
        model = SongMediaModel
        fields = ('id', 'stereo_audio', 'multichannel_audio', 'video_file', 'text', 'image')


class SongSerializer(ModelSerializer):
    location = SongLocationSerializer()
    details = SongDetailSerializer()
    media = SongMediaSerializer()

    class Meta:
        model = SongModel
        fields = ('id', 'title', 'recording_date', 'performers', 'collectors', 'source', 'location', 'details', 'media')

    @atomic
    def create(self, validated_data):
        location = validated_data.pop('location')
        details = validated_data.pop('details')
        media = validated_data.pop('media')
        song = SongModel.objects.create(**validated_data)
        SongLocationModel.objects.create(**location, song=song)
        SongDetailModel.objects.create(**details, song=song)
        SongMediaModel.objects.create(**media, song=song)
        return song
