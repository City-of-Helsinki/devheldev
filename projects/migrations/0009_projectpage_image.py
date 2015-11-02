# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0008_image_created_at_index'),
        ('projects', '0008_remove_projectpage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, related_name='+', to='wagtailimages.Image', blank=True),
        ),
    ]
