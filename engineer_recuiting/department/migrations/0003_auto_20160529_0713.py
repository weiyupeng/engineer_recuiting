# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_recruitmentinformation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recruitmentinformation',
            old_name='is_approved',
            new_name='status',
        ),
    ]
