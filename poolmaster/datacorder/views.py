from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from graphos.sources.model import ModelDataSource
from graphos.renderers.morris import LineChart

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

from bootstrap3_datetime.widgets import DateTimePicker

class ObservationCreate(CreateView):
    model = Observation
    fields = OBSERVATION_FIELDS

    def get_form(self):
        form = super(ObservationCreate, self).get_form()
        form.fields['observation_date'].widget = DateTimePicker(options={
            "format": "YYYY-MM-DD HH:mm",
            "pickSeconds": False
            }
        )
        return form

class ObservationUpdate(UpdateView):
    model = Observation
    fields = OBSERVATION_FIELDS

class ObservationDelete(DeleteView):
    model = Observation
    success_url = reverse_lazy('home')
