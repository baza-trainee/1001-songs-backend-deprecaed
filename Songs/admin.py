from django.contrib import admin
from Songs.models import Song


class SongsAdmin(admin.ModelAdmin):
    list_display = ('title','created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title',)


admin.site.register(Song, SongsAdmin)
