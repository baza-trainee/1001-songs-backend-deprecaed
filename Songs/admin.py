from django.contrib import admin
from Songs.models import Song, SongLocation, SongDetails, SongMedia


class SongsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title',)


class SongLocationAdmin(admin.ModelAdmin):
    list_display = ('song', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('song',)


class SongDetailsAdmin(admin.ModelAdmin):
    list_display = ('song', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('song',)


class SongMediaAdmin(admin.ModelAdmin):
    list_display = ('song', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('song',)


admin.site.register(Song, SongsAdmin)
admin.site.register(SongLocation, SongLocationAdmin)
admin.site.register(SongDetails, SongDetailsAdmin)
admin.site.register(SongMedia, SongMediaAdmin)
