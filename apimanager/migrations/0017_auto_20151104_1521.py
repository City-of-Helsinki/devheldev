# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apimanager', '0016_auto_20151104_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='location',
            new_name='app_url',
        ),
    ]
