# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('projects', '0021_projectpage_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPageTag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, verbose_name='Tags', to='taggit.Tag', help_text='A comma-separated list of tags.', through='projects.ProjectPageTag'),
        ),
        migrations.AddField(
            model_name='projectpagetag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(related_name='tagged_items', to='projects.ProjectPage'),
        ),
        migrations.AddField(
            model_name='projectpagetag',
            name='tag',
            field=models.ForeignKey(related_name='projects_projectpagetag_items', to='taggit.Tag'),
        ),
    ]
