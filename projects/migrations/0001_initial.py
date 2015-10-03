# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0020_auto_20151001_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.TextField()),
                ('full_description', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='wagtailcore.Page', parent_link=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProjectLink',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('type', models.CharField(choices=[('main', 'Main'), ('github', 'GitHub')], max_length=20)),
                ('description', models.CharField(max_length=200, blank=True, null=True)),
                ('url', models.URLField()),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='wagtailcore.Page', parent_link=True, serialize=False)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.SET_NULL, to='projects.Project', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
