# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '__latest__'),
        ('wagtailcore', '__latest__'),
        ('wagtailforms', '__latest__'),
        ('github', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GithubOrgIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, serialize=False, to='wagtailcore.Page', primary_key=True, parent_link=True)),
                ('url', models.URLField(default='https://api.github.com/orgs/City-of-Helsinki/events?per_page=5')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='githubindexpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='GithubIndexPage',
        ),
    ]
