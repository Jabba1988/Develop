# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartridge',
            name='quality_of_filling',
            field=models.CharField(default=b'satisfactorily', max_length=20, choices=[(b'satisfactorily', b'good'), (b'unsatisfactorily', b'bad')]),
        ),
    ]
