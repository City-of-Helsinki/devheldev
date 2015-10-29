# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0005_auto_20151029_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='personpage',
            name='avatar_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
