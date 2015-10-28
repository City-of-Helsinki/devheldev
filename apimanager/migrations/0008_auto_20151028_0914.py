# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apimanager', '0007_auto_20151028_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kongapiconfiguration',
            name='request_host',
            field=models.CharField(verbose_name='Hostname for API management platform', max_length=150, help_text='Similar to HTTP virtual hosts; changing this from default is required if user visible API host is publicly different', default='api.hel.fi'),
        ),
    ]
