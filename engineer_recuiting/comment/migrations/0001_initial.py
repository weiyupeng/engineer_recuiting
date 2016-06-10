# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20160610_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('engineer_starts', models.IntegerField(default=3, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('department_starts', models.IntegerField(default=3, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('engineer_review', models.CharField(default=True, max_length=b'300', null=True)),
                ('department_review', models.CharField(default=True, max_length=b'300', null=True)),
                ('application', models.OneToOneField(to='application.Application')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='EngieerComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
    ]
