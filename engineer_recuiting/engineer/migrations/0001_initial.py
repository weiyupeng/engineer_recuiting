# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificationOfDegree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('university', models.CharField(max_length=20)),
                ('degree', models.CharField(max_length=1, choices=[(b'H', b'Highschool'), (b'B', b'Banchler'), (b'M', b'Master'), (b'P', b'PHD')])),
                ('img', models.FileField(upload_to=b'/DegreeImg/')),
                ('owner', models.ForeignKey(related_name='degree_certifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EngineerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('ssn', models.CharField(max_length=20)),
                ('status', models.CharField(default=b'W', max_length=3, choices=[(b'W', b'waiting for approve'), (b'N', b'normal user'), (b'B', b'baned')])),
                ('review_score', models.IntegerField(default=-1)),
                ('description', models.CharField(max_length=b'200')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SkillCertification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=b'/SkillImg/')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(related_name='skill_certifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
