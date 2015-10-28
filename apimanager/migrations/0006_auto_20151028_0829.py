# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apimanager', '0005_auto_20151022_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apicustomer',
            name='account',
        ),
        migrations.RemoveField(
            model_name='application',
            name='customer',
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=None),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='APICustomer',
        ),
    ]
