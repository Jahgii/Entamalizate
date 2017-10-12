# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Usuarios, Clientes, Pedidos, Productos, Pedido_Productos

# Register your models here.

admin.site.register(Usuarios)
admin.site.register(Clientes)
admin.site.register(Pedidos)
admin.site.register(Productos)
admin.site.register(Pedido_Productos)
