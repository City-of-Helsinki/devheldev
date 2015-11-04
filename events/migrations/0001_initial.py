# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0021_auto_20151026_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='wagtailcore.Page', auto_created=True, serialize=False)),
                ('facebook_page_id', models.CharField(default='1415745085336451', max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
