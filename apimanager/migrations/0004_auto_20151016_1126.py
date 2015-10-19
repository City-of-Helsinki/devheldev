# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '__latest__'),
        ('apimanager', '0003_apipage_documentation'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, primary_key=True, to='wagtailcore.Page', parent_link=True, auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterModelOptions(
            name='apipage',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='apipage',
            name='sort_order',
            field=models.IntegerField(editable=False, null=True, blank=True),
        ),
    ]
