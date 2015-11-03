# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apimanager', '0011_auto_20151030_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apipage',
            name='api_path',
            field=models.CharField(max_length=50, help_text='Actual public API root endpoint; example usage: api.hel.fi/{path}/', default='', verbose_name='Root path for API Management platform'),
        ),
    ]
