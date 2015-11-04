# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0008_image_created_at_index'),
        ('apimanager', '0014_auto_20151104_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='apipage',
            name='image',
            field=models.ForeignKey(to='wagtailimages.Image', null=True, related_name='+', blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
