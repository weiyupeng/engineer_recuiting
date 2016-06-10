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
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=1000)),
                ('is_read', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(related_name='my_sending', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(related_name='my_receiver', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
