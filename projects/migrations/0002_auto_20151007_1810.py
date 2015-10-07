# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectpage',
            options={'ordering': ['sort_order']},
        ),
        migrations.RemoveField(
            model_name='projectpage',
            name='project',
        ),
        migrations.AddField(
            model_name='projectpage',
            name='full_description',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='short_description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectpage',
            name='sort_order',
            field=models.IntegerField(editable=False, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='projectlink',
            name='project',
            field=models.ForeignKey(related_name='links', to='projects.ProjectPage'),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
