# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apimanager', '0002_auto_20151001_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='apipage',
            name='documentation',
            field=models.URLField(blank=True),
        ),
    ]
