# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def make_role_types(apps, schema_editor):
    ProjectRole = apps.get_model('projects', 'ProjectRole')
    field = ProjectRole._meta.get_field_by_name('type')[0]
    types = {x: {'name': name} for x, name in field._choices}

    ProjectRoleType = apps.get_model('projects', 'ProjectRoleType')
    for type_id, t in types.items():
        rt, _ = ProjectRoleType.objects.get_or_create(name=t['name'])
        t['rt'] = rt

    for pr in ProjectRole.objects.all():
        pr.type_fk = types[pr.type]['rt']
        pr.save(update_fields=['type_fk'])


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20151103_1649'),
    ]

    operations = [
        migrations.RunPython(make_role_types)
    ]
