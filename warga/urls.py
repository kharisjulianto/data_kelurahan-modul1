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

from .views import WargaListView, WargaDetailListView, PengaduanListView, WargaCreateView
path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),
urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),
    path('<int:pk>/', WargaDetailListView.as_view(), name='warga-detail'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
]

from .views import WargaListView, WargaDetailListView, PengaduanListView, WargaCreateView, PengaduanCreateView
path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
from django.urls import path
from .views import (
    WargaListView,
    WargaDetailListView,
    PengaduanListView,
    WargaCreateView,
    PengaduanCreateView
)

urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('<int:pk>/', WargaDetailListView.as_view(), name='warga-detail'),
]
