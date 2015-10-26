# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_projectpage_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectrole',
            name='person',
            field=modelcluster.fields.ParentalKey(related_name='roles', to='aboutus.PersonPage'),
        ),
    ]
