# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-02 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packet',
            name='context',
            field=models.BinaryField(),
        ),
    ]