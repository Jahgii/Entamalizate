# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 07:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tamales', '0017_pedido_productos_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='Usuario',
        ),
        migrations.RemoveField(
            model_name='productos',
            name='user',
        ),
    ]
