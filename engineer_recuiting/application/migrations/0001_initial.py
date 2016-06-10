# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('department', '0004_auto_20160601_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('state', models.CharField(default=b'a', max_length=3, choices=[(b'a', b'approving'), (b'w', b'waiting'), (b's', b'start'), (b'd', b'denied'), (b'f', b'finishing')])),
                ('applier_message', models.TextField()),
                ('is_engineer_review', models.BooleanField(default=False)),
                ('is_department_review', models.BooleanField(default=False)),
                ('applier', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('recruitment', models.ForeignKey(to='department.RecruitmentInformation')),
            ],
        ),
    ]
