# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20160610_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplainReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('report_date', models.DateField()),
                ('description', models.TextField()),
                ('complain', models.ForeignKey(to='application.Application')),
            ],
        ),
    ]
