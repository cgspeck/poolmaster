# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 07:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datacorder', '0002_observation_observation_created'),
    ]

    operations = [
        migrations.RenameField('Observation', 'algie', 'algae'),
    ]
