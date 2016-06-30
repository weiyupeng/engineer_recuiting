# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0005_auto_20160623_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificationofdegree',
            name='img',
            field=models.FileField(default=1, upload_to=b'DegreeImg/'),
            preserve_default=False,
        ),
    ]
