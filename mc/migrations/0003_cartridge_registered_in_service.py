# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mc', '0002_auto_20151120_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartridge',
            name='registered_in_service',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 20, 8, 18, 49, 324000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
