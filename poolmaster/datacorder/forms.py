from django import forms

from bootstrap3_datetime.widgets import DateTimePicker

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

class CreateEditForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = OBSERVATION_FIELDS
        widgets = {
            'observation_date': DateTimePicker(
                options={
                    "format": "YYYY-MM-DD HH:mm",
                    "pickSeconds": False
                }
            )
        }
