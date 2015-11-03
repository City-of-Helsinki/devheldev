# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


ALTER_SQL = '''
    ALTER TABLE projects_projectrole ALTER COLUMN type TYPE integer USING type::integer;
    '''


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_merge'),
    ]

    operations = [
        migrations.RunSQL(ALTER_SQL, None, [
            migrations.AlterField(
                model_name='projectrole',
                name='type',
                field=models.IntegerField(),
                preserve_default=True,
            ),
        ]),
        migrations.AlterField(
            model_name='projectrole',
            name='type',
            field=models.ForeignKey(related_name='roles', to='projects.ProjectRoleType'),
        ),
    ]
