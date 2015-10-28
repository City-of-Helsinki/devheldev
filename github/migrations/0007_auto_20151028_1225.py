# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0006_auto_20151028_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='githuborgindexpage',
            name='api_url',
            field=models.URLField(default='https://api.github.com/orgs/City-of-Helsinki/events?per_page=5'),
        ),
    ]
