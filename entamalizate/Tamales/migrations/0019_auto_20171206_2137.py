# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 21:37
from __future__ import unicode_literals

import Tamales.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tamales', '0018_auto_20171206_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='Fecha_Final',
            field=Tamales.models.ConvertingDateTimeField(),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='Fecha_Inicio',
            field=Tamales.models.ConvertingDateTimeField(),
        ),
    ]
