import django
from django.db import models
from django.db.models.fields.related import ManyToManyField

from django.utils import timezone
from django.utils.dateformat import DateFormat
from django.urls import reverse

class InstrumentedModel(models.Model):
    class Meta:
        abstract=True

    def to_dict(self):
        opts = self._meta
        data = {}
        for f in opts.concrete_fields + opts.many_to_many:
            if isinstance(f, ManyToManyField):
                if self.pk is None:
                    data[f.name] = []
                else:
                    data[f.name] = list(f.value_from_object(self).values_list('pk', flat=True))
            else:
                data[f.name] = f.value_from_object(self)
        return data

    def __repr__(self):
        res = ''
        for k, v in self.to_dict().items():
            res += " {key}={value}".format(key=k, value=v)
        return '<{name}{data}>'.format(name=self.__class__.__name__, data=res)

    def filled_values(self):
        res = {}
        for k, v in self.to_dict().items():
            if isinstance(v, str):
                if len(v) > 0:
                    res[k] = v
            elif v is not None:
                res[k] = v
        return res

    def __str__(self):
        return ' '.join(['%s=%s' % (k, v) for k, v in self.filled_values().items()])

# Create your models here.
class Observation(InstrumentedModel):
    ALGAE_CHOICES = (
        ('', 'Not noted'),
        ('NONE', 'None'),
        ('SURFACES', 'It\'s on surfaces'),
        ('SUSPENDED', 'It\'s in the water')
    )
    TEST_CHOICES = (
        ('', 'Not noted'),
        ('REAGENT', 'Chemical reagent kit'),
        ('STRIP', 'Strip test'),
        ('PHOTOMETER', 'Reagent + Photometer'),
    )
    algae = models.CharField(
        max_length=12,
        choices=ALGAE_CHOICES,
        blank=True,
    )
    total_dissolved_solids = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    cyuranic_acid = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    free_chlorine = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    total_chlorine = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    ph = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    calcium_hardness = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    phosphate = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    test_type = models.CharField(
        max_length=12,
        choices=TEST_CHOICES,
        blank=True,
    )
    memo = models.TextField(blank=True)
    observation_created = models.DateTimeField(auto_now_add=True)
    observation_updated = models.DateTimeField(auto_now=True)
    observation_date = models.DateTimeField(default=django.utils.timezone.now)
    water_temperature = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    air_temperature = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    total_alkalinity = models.IntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('observation-detail', kwargs={'pk': self.pk})

    @property
    def observation_date_timestamp(self):
        return int(DateFormat(self.observation_date).format('U'))

    @property
    def observation_date_timestamp_mills(self):
        return self.observation_date_timestamp * 1000
