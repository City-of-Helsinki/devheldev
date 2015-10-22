# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20151001_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='template_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
