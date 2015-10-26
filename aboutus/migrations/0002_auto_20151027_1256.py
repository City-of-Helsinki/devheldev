# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '__latest__'),
        ('projects', '0006_auto_20151027_1256'),
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, to='wagtailcore.Page', auto_created=True)),
                ('sort_order', models.IntegerField(editable=False, null=True, blank=True)),
                ('name', models.CharField(max_length=200)),
                ('contact', models.URLField()),
                ('photo', models.ImageField(upload_to='aboutus_images')),
                ('job_title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('listed', models.BooleanField()),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
