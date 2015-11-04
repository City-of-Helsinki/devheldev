# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apimanager', '0013_auto_20151103_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='apipage',
            name='use_api_gateway',
            field=models.BooleanField(default=False, help_text='Set to false for APIs not managed by the api.hel.fi API gateway.'),
        ),
        migrations.AlterField(
            model_name='apipage',
            name='api_path',
            field=models.CharField(null=True, blank=True, default='', help_text='Actual public API root endpoint; example usage: api.hel.fi/{path}/', max_length=50, verbose_name='Root path for API Management platform'),
        ),
    ]
