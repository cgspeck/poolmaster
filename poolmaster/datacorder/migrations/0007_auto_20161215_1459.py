# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacorder', '0006_auto_20161215_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='air_temperature',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='observation',
            name='water_temperature',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
