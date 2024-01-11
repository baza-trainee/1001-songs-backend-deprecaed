from django.contrib import admin

from .models import SongES, SongESMedia, SongESDetails


class SongESDetailsInline(admin.StackedInline):
    model = SongESDetails
    extra = 1


class SongESMediaInline(admin.StackedInline):
    model = SongESMedia
    extra = 1


@admin.register(SongES)
class SongsAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'details', 'media',)
    list_filter = ('created_at', 'updated_at')
    inlines = [SongESMediaInline, SongESDetailsInline]
    search_fields = ('title',)
