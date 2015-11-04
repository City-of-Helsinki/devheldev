# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apimanager', '0012_auto_20151103_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apipage',
            name='name',
            field=models.CharField(verbose_name='Short and unique identifier for API', max_length=300, unique=True),
        ),
    ]
