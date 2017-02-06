from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from graphos.sources.model import ModelDataSource
from graphos.renderers.morris import LineChart

from .forms import CreateEditForm
from .models import Observation, Pool
from .resources import ObservationResource

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
                              fields=['observation_date_timestamp_mills', 'total_chlorine', 'free_chlorine', 'ph'])
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

class PoolDetail(DetailView):
    model = Pool

    def get_context_data(self, **kwargs):
        context = super(PoolDetail, self).get_context_data(**kwargs)
        context['fields'] = [
            {
                'name': f.name,
                'verbose_name': f.verbose_name,
                'is_choices': len(f.choices ) > 0,
                'name_is_choices': f.name + ',' + '%s'  % (len(f.choices ) > 0)
            } for f in Pool._meta.fields if f.name not in ['id']
        ]
        return context


class ExportView(View):

    def get(self, request, format='.html'):
        ACCEPTED_FORMATS={
            'html': {
                'Content-Type': 'text/html; charset=utf-8',
                'Content-Disposition': 'inline'
            },
            'csv':  {
                'Content-Type': 'text/csv; charset=utf-8',
                'Content-Disposition': 'attachment; filename="export.csv"'
            },
            'json': {
                'Content-Type': 'application/json',
                'Content-Disposition': 'attachment; filename="export.json"'
            },
            'ods': {
                'Content-Type': 'application/vnd.oasis.opendocument.spreadsheet',
                'Content-Disposition': 'attachment; filename="export.ods"'
            },
            'tsv':  {
                'Content-Type': 'text/tsv; charset=utf-8',
                'Content-Disposition': 'attachment; filename="export.tsv"'
            },
            'xls': {
                'Content-Type': 'application/vnd.ms-excel',
                'Content-Disposition': 'attachment; filename="export.xls"'
            }
        }
        requested_format = format.strip('.').lower()

        if requested_format not in ACCEPTED_FORMATS:
            return HttpResponseBadRequest('Unrecognised format')

        o = ObservationResource();
        e = o.export()
        result = getattr(e, requested_format)

        response = HttpResponse(
            result,
            content_type=ACCEPTED_FORMATS[requested_format]['Content-Type'],
        )
        response['Content-Disposition'] = ACCEPTED_FORMATS[requested_format]['Content-Disposition']
        return response
