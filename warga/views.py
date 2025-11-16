from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Warga, Pengaduan


class WargaListView(ListView):
    model = Warga


class WargaDetailListView(DetailView):
    model = Warga


class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import WargaForm

class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')

from django.views.generic import CreateView
from .forms import WargaForm, PengaduanForm
class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')
