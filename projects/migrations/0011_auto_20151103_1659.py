# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_projectlink_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectrole',
            name='type',
            field=models.CharField(max_length=20, choices=[('service_manager', 'Service manager'), ('tech', 'Tech lead')]),
        ),
    ]
