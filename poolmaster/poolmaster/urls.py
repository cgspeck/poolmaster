"""poolmaster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from datacorder.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^graph/$', GraphView.as_view(), name='graph'),
    url(r'^links/$', LinksView.as_view(), name='links'),
    url(r'observation/add/$', ObservationCreate.as_view(), name='observation-add'),
    url(r'observation/(?P<pk>[0-9]+)$', ObservationDetail.as_view(), name='observation-detail'),
    url(r'observation/(?P<pk>[0-9]+)/update$', ObservationUpdate.as_view(), name='observation-update'),
    url(r'observation/(?P<pk>[0-9]+)/delete$', ObservationDelete.as_view(), name='observation-delete'),
    url(r'pool/(?P<pk>[0-9]+)$', PoolDetail.as_view(), name='pool-detail'),
    url(r'export(?P<format>[.\w]+)$', ExportView.as_view(), name='export'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
