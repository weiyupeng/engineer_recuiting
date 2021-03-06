# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0004_auto_20160601_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitmentinformation',
            name='status',
            field=models.CharField(default=b'w', max_length=2, choices=[(b'a', b'approved'), (b'w', b'waiting'), (b'd', b'denied'), (b'e', b'ending')]),
        ),
    ]
