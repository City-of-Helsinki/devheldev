# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apimanager', '0015_apipage_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apipage',
            old_name='location',
            new_name='api_url',
        ),
    ]
