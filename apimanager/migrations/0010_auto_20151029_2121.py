# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apimanager', '0009_auto_20151029_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kongapiconfiguration',
            name='api_page',
            field=models.OneToOneField(to='apimanager.APIPage'),
        ),
    ]
