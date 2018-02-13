# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_mgmt', '0002_auto_20180205_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='smart_number',
            field=models.CharField(default=123, max_length=20),
            preserve_default=False,
        ),
    ]
