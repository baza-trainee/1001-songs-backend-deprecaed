from django.db.transaction import atomic
from rest_framework.serializers import ModelSerializer

from apps.songstest.models import SongsTestModel, SongTestLocationModel, SongTestDetailsModel, SongTestMediaModel


class SongsTestLocationSerializer(ModelSerializer):
    class Meta:
        model = SongTestLocationModel
        fields = ('id', 'country', 'region', 'district_center', 'administrative_center', 'ethnicity',
                  'ethnographic_district', 'official_name', 'unofficial_name', 'recording_location',
                  )


class SongTestDetailsSerializer(ModelSerializer):
    class Meta:
        model = SongTestDetailsModel
        fields = ('id', 'incipit', 'genre_cycle', 'poetic_text_genre', 'texture')


class SongTestMediaSerializer(ModelSerializer):
    class Meta:
        model = SongTestMediaModel
        fields = ('id', 'stereo_audio', 'multichannel_audio', 'video_file', 'text', 'image')


class SongsTestSerializers(ModelSerializer):
    location = SongsTestLocationSerializer()
    details = SongTestDetailsSerializer()
    media = SongTestMediaSerializer()

    class Meta:
        model = SongsTestModel
        fields = ('id', 'title', 'recording_date', 'performers', 'collectors', 'source', 'location', 'details', 'media')

    @atomic
    def create(self, validated_data):
        print(validated_data)
        location = validated_data.pop('location')
        details = validated_data.pop('details')
        media = validated_data.pop('media')
        song = SongsTestModel.objects.create(**validated_data)
        SongTestLocationModel.objects.create(**location, song=song)
        SongTestDetailsModel.objects.create(**details, song=song)
        SongTestMediaModel.objects.create(**media, song=song)
        return song
