# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 04:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tamales', '0015_auto_20171128_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='user',
            field=models.ForeignKey(default=14, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productos',
            name='user',
            field=models.ForeignKey(default=13, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
