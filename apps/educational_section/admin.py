from django.contrib import admin

from apps.educational_section.models import EducationalSection


@admin.register(EducationalSection)
class EducationalSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'photo',)
    list_filter = ('created_at', 'updated_at',)
    search_fields = ('title',)
