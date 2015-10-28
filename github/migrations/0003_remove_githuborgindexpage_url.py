# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0002_auto_20151028_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='githuborgindexpage',
            name='url',
        ),
    ]
