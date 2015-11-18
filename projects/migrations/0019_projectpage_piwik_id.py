# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20151105_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='piwik_id',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
