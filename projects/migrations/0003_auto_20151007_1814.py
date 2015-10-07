# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20151007_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectlink',
            name='project',
            field=modelcluster.fields.ParentalKey(to='projects.ProjectPage', related_name='links'),
        ),
    ]
