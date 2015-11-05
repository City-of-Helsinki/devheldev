# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aboutus', '0007_auto_20151104_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='personpage',
            name='user',
            field=models.OneToOneField(null=True, related_name='person', blank=True, to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
