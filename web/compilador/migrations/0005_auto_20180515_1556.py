# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-15 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compilador', '0004_auto_20180510_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ciudad',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='edad',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pais',
            field=models.CharField(default='', max_length=40),
        ),
    ]
