# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 18:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tamales', '0010_auto_20171012_0721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metodo_Pago',
            fields=[
                ('ID_Metodo', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='pedidos',
            name='Metodo_Pago',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Tamales.Metodo_Pago'),
            preserve_default=False,
        ),
    ]
