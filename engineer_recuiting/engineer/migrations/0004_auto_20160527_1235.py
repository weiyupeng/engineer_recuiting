# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0003_auto_20160527_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificationofdegree',
            name='img',
            field=models.FileField(upload_to=b'DegreeImg/'),
        ),
    ]
