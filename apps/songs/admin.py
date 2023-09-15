from django.contrib import admin
from django.urls import path, reverse
from django.utils.html import format_html
from apps.songs.admin_helpers import copy_song
from apps.songs.models import Song, SongLocation, SongDetail, SongMedia


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
                    'collectors', 'source', 'location', 'details', 'media', 'copy_button')  # добавили copy_button
    list_filter = ('created_at', 'updated_at')
    inlines = [SongLocationInline, SongDetailInline, SongMediaInline]
    search_fields = ('title',)

    # form = CopySongForm

    def get_urls(self) -> list:
        """
        Overrides URLs for the Song model in admin.
        Adds custom URL for copying songs
        """
        urls = super().get_urls()
        custom_urls = [
            path('<int:song_id>/copy/', self.admin_site.admin_view(copy_song), name='copy_song'),
        ]
        return custom_urls + urls

    def copy_button(self, obj: Song) -> str:
        """
        Creates a Copy button in the admin interface.
        """
        return format_html('<a class="button" href="{}">Copy</a>', reverse('admin:copy_song', args=[obj.pk]))

    copy_button.short_description = 'Copy Song'
    copy_button.allow_tags = True


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

#
# class CopySongForm(forms.Form):
#     copy_from_song = forms.ModelChoiceField(queryset=Song.objects.all(), label='Copy Data From')
#
# @admin.register(Song)
# class SongsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'recording_date', 'performers',
#                     'collectors', 'source', 'location', 'details', 'media')
#     list_filter = ('created_at', 'updated_at')
#     inlines = [SongLocationInline, SongDetailInline, SongMediaInline]
#     search_fields = ('title',)
#     form = CopySongForm
#
#     def save_model(self, request, obj, form, change):
#         if not obj.id:  # При создании новой записи
#             if form.cleaned_data.get('copy_from_song'):
#                 source_song = form.cleaned_data['copy_from_song']
#                 obj.title = source_song.title
#                 obj.recording_date = source_song.recording_date
#                 obj.performers = source_song.performers
#                 obj.collectors = source_song.collectors
#                 obj.source = source_song.source
#                 obj.location = source_song.location
#                 obj.details = source_song.details
#                 obj.media = source_song.media
#         obj.save()
#
# admin.site.register(Song, SongsAdmin)
# admin.site.register(SongLocation)
# admin.site.register(SongDetail)
# admin.site.register(SongMedia)
#
# @admin.register(SongLocation)
# class SongLocationAdmin(admin.ModelAdmin):
#     list_display = ('song', 'created_at', 'updated_at')
#     list_filter = ('created_at', 'updated_at')
#     search_fields = ('song',)
#
#
# @admin.register(SongDetail)
# class SongDetailsAdmin(admin.ModelAdmin):
#     list_display = ('song', 'created_at', 'updated_at')
#     list_filter = ('created_at', 'updated_at')
#     search_fields = ('song',)
#
#
# @admin.register(SongMedia)
# class SongMediaAdmin(admin.ModelAdmin):
#     list_display = ('song', 'created_at', 'updated_at')
#     list_filter = ('created_at', 'updated_at')
#     search_fields = ('song',)

# from django.contrib import admin, messages
# from django import forms
# from apps.songs.models import Song, SongLocation, SongDetail, SongMedia
# from apps.songs.admin_helpers import copy_song
# class SongLocationInline(admin.StackedInline):
#     model = SongLocation
#     extra = 1
#
# class SongDetailInline(admin.StackedInline):
#     model = SongDetail
#     extra = 1
#
# class SongMediaInline(admin.StackedInline):
#     model = SongMedia
#     extra = 1
#
# class CopySongForm(forms.ModelForm):
#     class Meta:
#         model = Song
#         fields = '__all__'
#         labels = {'id': 'Copy Data From'}
#
# from django.urls import path
# from django.utils.html import format_html
# from django.urls import reverse
#
#
#
# from .models import Song
#
#
#
#
# @admin.register(Song)
# class SongsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'recording_date', 'performers',
#                     'collectors', 'source', 'location', 'details', 'media', 'copy_button')  # добавили copy_button
#     list_filter = ('created_at', 'updated_at')
#     inlines = [SongLocationInline, SongDetailInline, SongMediaInline]
#     search_fields = ('title',)
#     form = CopySongForm
#
#     def get_urls(self):
#         urls = super().get_urls()
#         custom_urls = [
#             path('<int:song_id>/copy/', self.admin_site.admin_view(copy_song), name='copy_song'),
#         ]
#         return custom_urls + urls
#
#     def copy_button(self, obj):
#         return format_html('<a class="button" href="{}">Copy</a>', reverse('admin:copy_song', args=[obj.pk]))
#
#     copy_button.short_description = 'Copy Song'
#     copy_button.allow_tags = True
#
# admin.site.register(SongLocation)
# admin.site.register(SongDetail)
# admin.site.register(SongMedia)
