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

from rest_framework.routers import DefaultRouter

# -----------------------------------
# URL CRUD (Template / HTML)
# -----------------------------------

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

# -----------------------------------
# URL API (Router untuk ViewSet)
# -----------------------------------

router = DefaultRouter()
router.register(r'warga-api', WargaViewSet)
router.register(r'pengaduan-api', PengaduanViewSet)

urlpatterns += router.urls

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WargaViewSet, PengaduanViewSet

router = DefaultRouter()
router.register(r'warga', WargaViewSet, basename='warga')
router.register(r'pengaduan', PengaduanViewSet, basename='pengaduan')

urlpatterns = [
    path('', include(router.urls)),
]
