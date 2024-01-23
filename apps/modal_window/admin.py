from django.contrib import admin

from .models import ModalWindow


@admin.register(ModalWindow)
class ModalWindowAdmin(admin.ModelAdmin):
    list_display = ('id', 'info', 'iban', 'coffee', 'patreon', 'qr',)
