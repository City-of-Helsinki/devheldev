# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apimanager', '0010_auto_20151029_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kongapiconfiguration',
            name='request_host',
            field=models.CharField(unique=True, max_length=150, help_text='Kong requires that API has a unique host name, f.x. name.api.hel.fi -> api.hel.fi/name', verbose_name='Host and domain name'),
        ),
    ]
