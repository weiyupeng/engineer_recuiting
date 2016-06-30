# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0004_auto_20160527_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificationofdegree',
            name='img',
            field=models.FileField(null=True, upload_to=b'DegreeImg/', blank=True),
        ),
    ]
