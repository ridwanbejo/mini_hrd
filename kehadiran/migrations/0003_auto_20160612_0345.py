# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-12 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kehadiran', '0002_izin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='izin',
            name='disetujui',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='izin',
            name='jenis_kehadiran',
            field=models.CharField(choices=[('izin', 'Izin'), ('cuti', 'Cuti')], max_length=20),
        ),
    ]