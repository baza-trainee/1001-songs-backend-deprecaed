from rest_framework.serializers import ModelSerializer

from .models import ModalWindow


class ModalWindowSerializer(ModelSerializer):
    class Meta:
        model = ModalWindow
        fields = ('id', 'info', 'iban', 'coffee', 'patreon', 'qr',)
