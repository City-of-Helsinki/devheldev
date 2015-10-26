# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '__latest__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, primary_key=True, to='wagtailcore.Page', parent_link=True, auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('contact', models.URLField()),
                ('photo', models.ImageField(upload_to='aboutus_images')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('listed', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
