# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_projectpage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectlink',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
