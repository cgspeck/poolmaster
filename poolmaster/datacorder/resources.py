from import_export import resources
from .models import Observation

class ObservationResource(resources.ModelResource):
    class Meta:
        model = Observation
