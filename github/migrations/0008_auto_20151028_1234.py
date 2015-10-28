# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0007_auto_20151028_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='githuborgindexpage',
            name='api_url',
        ),
        migrations.AddField(
            model_name='githuborgindexpage',
            name='github_org_name',
            field=models.CharField(max_length=200, default='City-of-Helsinki'),
        ),
    ]
