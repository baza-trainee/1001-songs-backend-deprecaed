from django.db import models


class ModalWindow(models.Model):

    info = models.CharField(max_length=250, blank=True)
    iban = models.CharField(max_length=250, blank=True)
    coffee = models.URLField(blank=True)
    patreon = models.URLField(blank=True)
    qr = models.ImageField(blank=True)
    