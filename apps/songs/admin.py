from django.contrib import admin

from apps.songs.models import Song, SongLocation, SongDetail, SongMedia
#

class SongLocationInline(admin.StackedInline):
    model = SongLocation
    extra = 1


class SongDetailInline(admin.StackedInline):
    model = SongDetail
    extra = 1


class SongMediaInline(admin.StackedInline):
    model = SongMedia
    extra = 1


@admin.register(Song)
class SongsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'recording_date', 'performers',
                    'collectors', 'source', 'location', 'details', 'media')
    list_filter = ('created_at', 'updated_at')
    inlines = [SongLocationInline, SongDetailInline, SongMediaInline]
    search_fields = ('title',)


@admin.register(SongLocation)
class SongLocationAdmin(admin.ModelAdmin):
    list_display = ('song', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('song',)


@admin.register(SongDetail)
class SongDetailsAdmin(admin.ModelAdmin):
    list_display = ('song', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('song',)


@admin.register(SongMedia)
class SongMediaAdmin(admin.ModelAdmin):
    list_display = ('song', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('song',)
