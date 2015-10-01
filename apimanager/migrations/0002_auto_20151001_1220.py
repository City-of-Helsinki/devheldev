# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('apimanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, to='wagtailcore.Page', serialize=False, parent_link=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('location', models.URLField()),
                ('short_description', models.TextField()),
                ('full_description', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.DeleteModel(
            name='APISettings',
        ),
    ]
