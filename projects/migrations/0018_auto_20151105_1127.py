# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20151104_1228'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectrole',
            options={'ordering': ('type',)},
        ),
    ]
