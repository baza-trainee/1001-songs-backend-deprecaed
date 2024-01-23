from rest_framework.generics import ListAPIView

from .models import Footer
from .serializers import FooterSerializer


class FooterListView(ListAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
