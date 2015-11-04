# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0006_personpage_avatar_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personpage',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
