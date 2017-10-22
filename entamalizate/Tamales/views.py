# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Productos, Clientes, Pedido_Productos, Usuarios, Pedidos, Metodo_Pago
from django.views.generic import ListView

# Create your views here.

class ProductosVista(ListView):
    template_name = "Tamales/VistaProductos.html"
    queryset = Productos.objects.all()

class ClientesVista(ListView):
    template_name = "Tamales/VistaClientes.html"
    queryset = Clientes.objects.all()

def Registro_orden(request):
    result_set01 = Pedidos.objects.all() #Cliente__ID_Cliente=2 ; filter(Pedido__Cliente=3)
    result_set02 = Pedido_Productos.objects.all()
    context = {
    "Pedidos": result_set01, "Productos_P": result_set02
    }
    return render(request, "Tamales/Ordenes.html", context)
