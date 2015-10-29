# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0004_auto_20151027_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personpage',
            name='photo',
        ),
        migrations.AddField(
            model_name='personpage',
            name='github_user',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
    ]
