# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apimanager', '0004_auto_20151016_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='APICustomer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('enabled', models.BooleanField(default=False)),
                ('account', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='APISubscription',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('consumer_id', models.CharField(max_length=300)),
                ('consumer_kong_id', models.CharField(max_length=300)),
                ('key', models.CharField(max_length=300)),
                ('key_kong_id', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.URLField(blank=True, null=True)),
                ('customer', models.ForeignKey(to='apimanager.APICustomer')),
            ],
        ),
        migrations.CreateModel(
            name='KongAPIConfiguration',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('request_host', models.CharField(help_text='Similar to HTTP virtual hosts; changing this from default is required if user visible API host is publicly different', max_length='150', verbose_name='Hostname for API management platform', default='api.hel.fi')),
                ('kong_api_id', models.CharField(max_length=300, editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='apipage',
            name='api_path',
            field=models.CharField(help_text='User visible path; example usage: api.hel.fi/{path}/', max_length=50, verbose_name='Root path for API Management platform', default=''),
        ),
        migrations.AddField(
            model_name='kongapiconfiguration',
            name='api_page',
            field=models.ForeignKey(to='apimanager.APIPage'),
        ),
        migrations.AddField(
            model_name='application',
            name='subscriptions',
            field=models.ManyToManyField(through='apimanager.APISubscription', to='apimanager.KongAPIConfiguration'),
        ),
        migrations.AddField(
            model_name='apisubscription',
            name='api',
            field=models.ForeignKey(to='apimanager.KongAPIConfiguration'),
        ),
        migrations.AddField(
            model_name='apisubscription',
            name='application',
            field=models.ForeignKey(to='apimanager.Application'),
        ),
    ]
