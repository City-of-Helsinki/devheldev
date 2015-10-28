# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apimanager', '0006_auto_20151028_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kongapiconfiguration',
            name='kong_api_id',
            field=models.CharField(max_length=300, null=True, editable=False),
        ),
    ]
