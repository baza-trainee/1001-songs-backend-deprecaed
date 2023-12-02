from rest_framework.generics import ListAPIView

from apps.education_section.models import EducationalSection
from apps.education_section.serializers import EducationalSectionSerializer


class EducationalSectionListView(ListAPIView):
    """
    List of educational section
    """
    queryset = EducationalSection.objects.all()
    serializer_class = EducationalSectionSerializer
