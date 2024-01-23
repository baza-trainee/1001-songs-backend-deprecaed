from rest_framework.generics import ListAPIView

from .models import ModalWindow
from .serializers import ModalWindowSerializer


class ModalWindowListView(ListAPIView):
    queryset = ModalWindow.objects.all()
    serializer_class = ModalWindowSerializer
    