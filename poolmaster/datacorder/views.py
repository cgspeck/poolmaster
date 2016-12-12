from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Observation

OBSERVATION_FIELDS = [
    'observation_date',
    'test_type',
    'algae',
    'free_chlorine',
    'total_chlorine',
    'ph',
    'cyuranic_acid',
    'phosphate',
    'total_dissolved_solids',
    'calcium_hardness',
    'memo',
]
# Create your views here.
class IndexView(ListView):
    model = Observation

    def get_queryset(self):
        return Observation.objects.order_by('-observation_date')[:100]

class GraphView(TemplateView):
    template_name = "datacorder/graph.html"

class LinksView(TemplateView):
    template_name = "datacorder/links.html"

class ObservationDetail(DetailView):
    model = Observation

class ObservationCreate(CreateView):
    model = Observation
    fields = OBSERVATION_FIELDS

class ObservationUpdate(UpdateView):
    model = Observation
    fields = OBSERVATION_FIELDS

class ObservationDelete(DeleteView):
    model = Observation
    success_url = reverse_lazy('home')
