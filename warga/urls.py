from django.urls import path
from .views import (
    WargaListView,
    WargaDetailListView,
    WargaCreateView,
    WargaUpdateView,
    WargaDeleteView,
    
    PengaduanListView,
    PengaduanCreateView,
    PengaduanUpdateView,
    PengaduanDeleteView,

    WargaViewSet,
    PengaduanViewSet,
)

# ----------------------------
# URL CRUD (template-based)
# ----------------------------

urlpatterns = [
    # WARGA
    path('', WargaListView.as_view(), name='warga-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),
    path('<int:pk>/', WargaDetailListView.as_view(), name='warga-detail'),
    path('<int:pk>/edit/', WargaUpdateView.as_view(), name='warga-edit'),
    path('<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga-hapus'),

    # PENGADUAN
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
    path('pengaduan/<int:pk>/edit/', PengaduanUpdateView.as_view(), name='pengaduan-edit'),
    path('pengaduan/<int:pk>/hapus/', PengaduanDeleteView.as_view(), name='pengaduan-hapus'),
]

# ----------------------------
# URL API (REST Framework)
# ----------------------------

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'warga-api', WargaViewSet)
router.register(r'pengaduan-api', PengaduanViewSet)

urlpatterns += router.urls
