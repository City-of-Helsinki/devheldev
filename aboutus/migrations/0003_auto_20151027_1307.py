# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0002_auto_20151027_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personpage',
            name='photo',
            field=models.ImageField(null=True, upload_to='aboutus_images'),
        ),
    ]
