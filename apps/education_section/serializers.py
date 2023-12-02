from rest_framework.serializers import ModelSerializer

from apps.education_section.models import EducationalSection


class EducationalSectionSerializer(ModelSerializer):
    class Meta:
        model = EducationalSection
        fields = (
            'title', 'description', 'photo',
        )

