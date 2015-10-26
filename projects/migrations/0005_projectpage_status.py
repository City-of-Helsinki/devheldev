# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_projectkpi_projectrole'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='status',
            field=models.CharField(choices=[('discovery', 'Discovery'), ('alpha', 'Alpha'), ('beta', 'Beta'), ('live', 'LIVE')], max_length=20, default='discovery'),
        ),
    ]
