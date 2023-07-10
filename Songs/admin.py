from django.contrib import admin
from Songs.models import Songs


class SongsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'category', 'createdAt', 'updatedAt')
    list_filter = ('createdAt', 'updatedAt')
    search_fields = ('title',)


admin.site.register(Songs, SongsAdmin)
