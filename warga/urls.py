from django.urls import path
from .views import WargaListView, WargaDetailListView

urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('<int:pk>/', WargaDetailListView.as_view(), name='warga-detail'),
]