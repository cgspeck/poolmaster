from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from graphos.sources.model import ModelDataSource
from graphos.renderers.morris import LineChart

from .models import Observation
from .forms import CreateEditForm

# Create your views here.
class IndexView(ListView):
    model = Observation

    def get_queryset(self):
        return Observation.objects.order_by('-observation_date')[:100]

class GraphView(TemplateView):
    template_name = "datacorder/graph.html"

    def get_context_data(self, **kwargs):
        context = super(GraphView, self).get_context_data(**kwargs)
        queryset = Observation.objects.order_by('-observation_date')[:100]

        chlorine_data_source = ModelDataSource(queryset,
                              fields=['normalised_observation_date', 'free_chlorine', 'total_chlorine'])
        chlorine_chart = LineChart(chlorine_data_source)
        context['chlorine_chart'] = chlorine_chart
        return context

class LinksView(TemplateView):
    template_name = "datacorder/links.html"

class ObservationDetail(DetailView):
    model = Observation

class ObservationCreate(CreateView):
    model = Observation
    form_class = CreateEditForm

class ObservationUpdate(UpdateView):
    model = Observation
    form_class = CreateEditForm

class ObservationDelete(DeleteView):
    model = Observation
    success_url = reverse_lazy('home')
