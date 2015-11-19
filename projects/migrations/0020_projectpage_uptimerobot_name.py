# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_projectpage_piwik_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='uptimerobot_name',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
    ]
