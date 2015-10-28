# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0005_auto_20151028_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='githuborgindexpage',
            old_name='url',
            new_name='api_url',
        ),
    ]
