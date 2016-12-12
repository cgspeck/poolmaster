from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Observation

# Create your views here.
class IndexView(ListView):
    model = Observation

    def get_queryset(self):
        return Observation.objects.order_by('-observation_created')[:100]

class GraphView(TemplateView):
    template_name = "datacorder/graph.html"

class LinksView(TemplateView):
    template_name = "datacorder/links.html"

class ObservationDetail(DetailView):
    model = Observation

class ObservationCreate(CreateView):
    model = Observation
    fields = [
        'algae', 'total_dissolved_solids', 'cyuranic_acid', 'free_chlorine', 'total_chlorine', 'ph', 'calcium_hardness', 'phosphate', 'test_type', 'memo',
    ]

class ObservationUpdate(UpdateView):
    model = Observation
    fields = [
        'algae', 'total_dissolved_solids', 'cyuranic_acid', 'free_chlorine', 'total_chlorine', 'ph', 'calcium_hardness', 'phosphate', 'test_type', 'memo',
    ]

class ObservationDelete(DeleteView):
    model = Observation
    success_url = reverse_lazy('home')
