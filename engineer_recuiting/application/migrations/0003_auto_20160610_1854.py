# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20160602_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(default=b'w', max_length=3, choices=[(b'a', b'approving'), (b'w', b'waiting'), (b's', b'start'), (b'd', b'denied'), (b'f', b'finishing'), (b'c', b'complaining')]),
        ),
    ]
