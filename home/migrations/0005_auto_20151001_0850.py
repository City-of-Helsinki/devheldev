# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0002_add_verbose_names'),
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('wagtailredirects', '0002_add_verbose_names'),
        ('home', '0004_blogpage_blogpagelisting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='blogpagelisting',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='BlogPage',
        ),
        migrations.DeleteModel(
            name='BlogPageListing',
        ),
    ]
