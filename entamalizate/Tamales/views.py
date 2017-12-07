# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .models import (Productos,
                     Clientes,
                     Pedido_Productos,
                     Usuarios,
                     Pedidos,
                     Metodo_Pago)

from django.views.generic import    (ListView,
                                     CreateView,
                                     DeleteView,
                                     UpdateView,
                                     ListView)

from .forms import PedidosProductosModelForm, PedidosModelForm
from django.db.models import Q
from django.urls import reverse_lazy
from .mixin import FormUserNeededMixin
    #Importaciones del modelo usuario de Django
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, get_user_model, login

User = get_user_model()
# Create your views here.

        # Clases definidas para borrar pedido y producto contenido en un pedido.
class PedidoDeleteView(LoginRequiredMixin, DeleteView):
    model = Pedidos
    template_name = "Tamales/delete_confirm.html"
    success_url = reverse_lazy("pedidos_lista")

class Pedido_ProductosDeleteView(LoginRequiredMixin, DeleteView):
    model = Pedido_Productos
    template_name = "Tamales/delete_confirm.html"
    success_url = reverse_lazy("VistaOrdenes")

        #Clases para agregar un pedido y agregar productos.
class PedidoCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = PedidosModelForm
    template_name = "Tamales/PedirPedido.html"
    success_url = reverse_lazy("VistaOrdenes")

class Pedido_ProductosCreateView(FormUserNeededMixin, CreateView):
    form_class = PedidosProductosModelForm
    template_name = "Tamales/PedirPedido.html"
    success_url = reverse_lazy("VistaOrdenes")

        #Clases para actualizar un pedido y productos contenidos en él.
class Pedido_ProductosUpdateView(FormUserNeededMixin, UpdateView):
    queryset = Pedido_Productos.objects.all()
    form_class = PedidosProductosModelForm
    template_name = "Tamales/update_view.html"
    success_url = reverse_lazy("VistaOrdenes")

        #Clases para mostrar una lista de productos en un pedido
class Pedido_ProductosListView(FormUserNeededMixin, ListView):
    template_name = "PedidosProductosView.html"
    #queryset = Pedido_Productos.objects.all()
    def get_queryset(self, *args, **kwargs):
        qs = Pedido_Productos.objects.all().order_by("-pk")
        print self.request.GET
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                            Q(Producto__icontains=query) |
                            Q(user__username__icontains=query)
                          )
        return qs.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        consulta = super(Pedido_ProductosListView, self).get_context_data(**kwargs)
        consulta['Pedidos'] = Pedidos.objects.filter(user=self.request.user)
        consulta['Productos_P'] = Pedido_Productos.objects.filter(user=self.request.user)
        return consulta


            #Clase para mostrar una lista de pedidos
class PedidosListView(ListView):
    template_name = "PedidosView_Ajax.html"

    def get_queryset(self, *args, **kwargs):
        qs = Pedidos.objects.all().order_by("-pk")
        print self.request.GET
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
            Q(ID_Pedido__icontains=query)|
            Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
         context = super(PedidosListView, self).get_context_data(*args, **kwargs)
         print context
         context['create_form'] = PedidosModelForm()
         context['create_url'] = reverse_lazy("pedidos_create")
         return context
