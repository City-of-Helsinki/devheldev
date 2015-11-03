# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_projectlink_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectRoleType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='projectrole',
            name='type',
            field=models.CharField(max_length=20, choices=[('service_manager', 'Service manager'), ('tech', 'Tech lead')]),
        ),
        migrations.AddField(
            model_name='projectrole',
            name='type_fk',
            field=modelcluster.fields.ParentalKey(to='projects.ProjectRoleType', null=True, related_name='roles'),
        ),
    ]
