# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0003_auto_20151027_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personpage',
            name='description',
            field=models.CharField(null=True, blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='personpage',
            name='photo',
            field=models.ImageField(null=True, upload_to='aboutus_images', blank=True),
        ),
    ]
