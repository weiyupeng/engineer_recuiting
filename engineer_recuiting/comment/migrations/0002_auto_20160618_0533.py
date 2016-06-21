# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DepartmentComment',
        ),
        migrations.DeleteModel(
            name='EngieerComment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='department_review',
            field=models.CharField(max_length=b'300', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='engineer_review',
            field=models.CharField(max_length=b'300', null=True, blank=True),
        ),
    ]
