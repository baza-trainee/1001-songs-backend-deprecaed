from rest_framework.serializers import ModelSerializer

from .models import Footer


class FooterSerializer(ModelSerializer):
    class Meta:
        model = Footer
        fields = ('id', 'reporting', 'privacy_policy', 'rules_and_terms', 'email', 'facebook', 'youtube',)
