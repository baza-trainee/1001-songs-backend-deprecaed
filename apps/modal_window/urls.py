from django.urls import path

from .views import ModalWindowListView

urlpatterns = [
    path('', ModalWindowListView.as_view(), name='list_modal_window'),
]
