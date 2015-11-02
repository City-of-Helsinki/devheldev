# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_projectpage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectpage',
            name='image',
        ),
    ]
