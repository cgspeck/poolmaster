from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Observation

@admin.register(Observation)
class ObservationAdmin(ImportExportModelAdmin):
    pass
