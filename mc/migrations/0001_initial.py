# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartridge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Manufacturer', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('serial_number', models.CharField(max_length=20)),
                ('printed_pages', models.CharField(max_length=20)),
                ('quality_of_filling', models.CharField(default=b'satisfactorily', max_length=2, choices=[(b'satisfactorily', b'good'), (b'unsatisfactorily', b'bad')])),
                ('symptom_victim_services', models.CharField(default=b'none', max_length=300)),
                ('internal_number', models.CharField(max_length=30)),
                ('date_of_filling', models.DateField()),
                ('install_cartridge_date', models.DateField()),
                ('uninstall_cartridge_date', models.DateField()),
                ('install_cartridge_page_count', models.CharField(max_length=20)),
                ('uninstall_cartridge_page_count', models.CharField(max_length=20)),
            ],
        ),
    ]
