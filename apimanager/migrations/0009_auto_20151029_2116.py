# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apimanager', '0008_auto_20151028_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apisubscription',
            name='consumer_id',
            field=models.CharField(max_length=300, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apisubscription',
            name='consumer_kong_id',
            field=models.CharField(max_length=300, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apisubscription',
            name='key',
            field=models.CharField(max_length=300, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apisubscription',
            name='key_kong_id',
            field=models.CharField(max_length=300, blank=True, null=True),
        ),
    ]
