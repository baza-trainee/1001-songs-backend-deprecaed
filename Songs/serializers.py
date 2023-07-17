from rest_framework import serializers
from Songs.models import Song, SongLocation, SongDetails, SongMedia


class SongLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongLocation
        fields = '__all__'
        read_only_fields = ('song',)


class SongDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongDetails
        fields = '__all__'
        read_only_fields = ('song',)


class SongMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongMedia
        fields = '__all__'
        read_only_fields = ('song',)


class SongSerializer(serializers.ModelSerializer):
    location = SongLocationSerializer()
    details = SongDetailsSerializer()
    media = SongMediaSerializer()

    class Meta:
        model = Song
        fields = '__all__'
