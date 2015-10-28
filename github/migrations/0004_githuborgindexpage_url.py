# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0003_remove_githuborgindexpage_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='githuborgindexpage',
            name='url',
            field=models.URLField(default='https://api.github.com/orgs/City-of-Helsinki/events?per_page=5'),
        ),
    ]
