# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_projecttag'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectObjectCount',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('object_name', models.CharField(max_length=40)),
                ('description', models.CharField(blank=True, null=True, max_length=200)),
                ('object_count_url', models.URLField()),
                ('project', modelcluster.fields.ParentalKey(related_name='dynamic_kpis', to='projects.ProjectPage')),
            ],
        ),
    ]
