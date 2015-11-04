# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20151103_1742'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectroletype',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='projectroletype',
            name='sort_order',
            field=models.IntegerField(null=True, blank=True, editable=False),
        ),
    ]
