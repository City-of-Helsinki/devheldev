# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0004_githuborgindexpage_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='githuborgindexpage',
            name='url',
            field=models.URLField(),
        ),
    ]
