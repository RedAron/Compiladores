# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-10 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compilador', '0002_auto_20180510_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(default='i', max_length=40),
        ),
        migrations.AddField(
            model_name='usuario',
            name='ciudad',
            field=models.CharField(default='i', max_length=40),
        ),
        migrations.AddField(
            model_name='usuario',
            name='lenguajePreferencia',
            field=models.CharField(default='i', max_length=15),
        ),
        migrations.AddField(
            model_name='usuario',
            name='pais',
            field=models.CharField(default='i', max_length=40),
        ),
    ]
