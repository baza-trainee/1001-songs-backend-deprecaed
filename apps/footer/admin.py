from django.contrib import admin

from .models import Footer


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('id', 'reporting', 'privacy_policy', 'rules_and_terms', 'email', 'facebook', 'youtube',)
