# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0002_auto_20160527_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skillcertification',
            name='owner',
        ),
        migrations.DeleteModel(
            name='SkillCertification',
        ),
    ]
