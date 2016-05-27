# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificationofdegree',
            name='status',
            field=models.CharField(default=b'W', max_length=3, choices=[(b'W', b'waiting for approve'), (b'N', b'normal user'), (b'B', b'baned')]),
        ),
        migrations.AddField(
            model_name='skillcertification',
            name='status',
            field=models.CharField(default=b'W', max_length=3, choices=[(b'W', b'waiting for approve'), (b'N', b'normal user'), (b'B', b'baned')]),
        ),
    ]
