# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
        ('projects', '0003_auto_20151007_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectKPI',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('value', models.CharField(max_length=200)),
                ('project', modelcluster.fields.ParentalKey(related_name='kpis', to='projects.ProjectPage')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectRole',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('type', models.CharField(max_length=20, choices=[('owner', 'Product owner'), ('tech', 'Tech lead')])),
                ('person', modelcluster.fields.ParentalKey(related_name='roles', to='aboutus.Person')),
                ('project', modelcluster.fields.ParentalKey(related_name='roles', to='projects.ProjectPage')),
            ],
        ),
    ]
