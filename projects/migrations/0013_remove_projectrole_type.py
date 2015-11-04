# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


def remove_broken_revisions(apps, schema_editor):
    PageRevision = apps.get_model('wagtailcore', 'PageRevision')
    PageRevision.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20151103_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectrole',
            name='type',
        ),
        migrations.RenameField(
            model_name='projectrole',
            old_name='type_fk', new_name='type'
        ),
        migrations.AlterField(
            model_name='projectrole',
            name='type',
            field=modelcluster.fields.ParentalKey(to='projects.ProjectRoleType', related_name='roles'),
            preserve_default=False,
        ),
        migrations.RunPython(remove_broken_revisions),
    ]
