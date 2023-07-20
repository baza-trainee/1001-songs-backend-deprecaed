from django.contrib import admin

from apps.songs.models import SongModel, SongLocationModel, SongDetailModel, SongMediaModel


@admin.register(SongModel)
class SongsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'recording_date', 'performers',
                    'collectors', 'source', 'location', 'details', 'media')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title',)


@admin.register(SongLocationModel)
class SongLocationAdmin(admin.ModelAdmin):
    list_display = ('song', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('song',)


@admin.register(SongDetailModel)
class SongDetailsAdmin(admin.ModelAdmin):
    list_display = ('song', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('song',)


@admin.register(SongMediaModel)
class SongMediaAdmin(admin.ModelAdmin):
    list_display = ('song', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('song',)
