# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('algie', models.CharField(choices=[('', 'Not noted'), ('NONE', 'None'), ('SURFACES', "It's on surfaces"), ('SUSPENDED', "It's in the water")], max_length=12)),
                ('total_dissolved_solids', models.DecimalField(decimal_places=1, max_digits=5, null=True)),
                ('cyuranic_acid', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('free_chlorine', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('total_chlorine', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('ph', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('calcium_hardness', models.DecimalField(decimal_places=1, max_digits=5, null=True)),
                ('phosphate', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('test_type', models.CharField(choices=[('', 'Not noted'), ('REAGENT', 'Chemical reagent kit'), ('STRIP', 'Strip test'), ('PHOTOMETER', 'Tested with measurements taken by a photometer')], max_length=12)),
                ('memo', models.TextField()),
            ],
        ),
    ]