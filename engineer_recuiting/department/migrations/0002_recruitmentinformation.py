# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecruitmentInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
                ('salary', models.PositiveIntegerField()),
                ('major_area', models.CharField(max_length=2, choices=[(b'CS', b'computer science'), (b'EE', b'electric engnieer')])),
                ('description', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=2, choices=[(b'BJ', b'BJ'), (b'TJ', b'TJ')])),
                ('city', models.CharField(max_length=2, choices=[(b'HD', b'HD'), (b'BH', b'BH')])),
                ('is_approved', models.CharField(default=b'a', max_length=2, choices=[(b'a', b'approved'), (b'w', b'waiting'), (b'd', b'denied')])),
                ('reason_of_deny', models.TextField(max_length=300, null=True, blank=True)),
                ('department', models.ForeignKey(verbose_name=b'recruitment_infos', to=settings.AUTH_USER_MODEL, help_text=b'your department')),
            ],
        ),
    ]
