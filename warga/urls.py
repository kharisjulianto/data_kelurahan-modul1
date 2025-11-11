from django.urls import path
from .views import WargaListView, WargaDetailListView

urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('<int:pk>/', WargaDetailListView.as_view(), name='warga-detail'),
]

from .views import WargaListView, WargaDetailListView, PengaduanListView

urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('<int:pk>/', WargaDetailListView.as_view(), name='warga-detail'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
]
