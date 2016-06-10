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
            name='CompanyProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=50)),
                ('bussiness_area', models.CharField(max_length=3, choices=[(b'CS', b'computer science'), (b'EE', b'electric engnieer')])),
                ('permit_id', models.CharField(max_length=30)),
                ('website', models.URLField(null=True, blank=True)),
                ('phone', models.CharField(max_length=15)),
                ('contacter', models.CharField(max_length=20)),
                ('permit_img', models.FileField(upload_to=b'permitImg')),
                ('bank_name', models.CharField(max_length=90)),
                ('account', models.IntegerField(default=10000)),
                ('account_bank_name', models.CharField(max_length=200)),
                ('bank_permit_img', models.FileField(upload_to=b'BankImg')),
                ('company_telphone', models.CharField(max_length=16)),
                ('credit', models.IntegerField(default=-1)),
                ('status', models.CharField(default=b'W', max_length=3, choices=[(b'W', b'waiting for approve'), (b'N', b'normal user'), (b'B', b'baned')])),
                ('description', models.TextField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
