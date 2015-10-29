# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20151027_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to='project_images'),
        ),
    ]
