# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-10 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compilador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
