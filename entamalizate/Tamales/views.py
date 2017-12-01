# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from .models import Productos, Clientes, Pedido_Productos, Usuarios, Pedidos, Metodo_Pago
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .forms import PedidosProductosModelForm, PedidosModelForm
from django.db.models import Q
from django.urls import reverse_lazy
#from .mixin import FormUserNeededMixin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, get_user_model, login

from registration import signals
from registration.views import RegistrationView as BaseRegistrationView


User = get_user_model()
# Create your views here.

class RegistrationView(BaseRegistrationView):
    """
    Registration via the simplest possible process: a user supplies a
    username, email address and password (the bare minimum for a
    useful account), and is immediately signed up and logged in.
    """
    def register(self, form):
        new_user = form.save()
        new_user = authenticate(
            username=getattr(new_user, User.USERNAME_FIELD),
            password=form.cleaned_data['password1']
        )
        login(self.request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=self.request)
        return new_user

    def get_success_url(self, user):
        return '/'

        # Clases definidas para borrar pedido y producto contenido en un pedido.
class PedidoDeleteView(DeleteView):
    model = Pedidos
    template_name = "Tamales/delete_confirm.html"
    success_url = reverse_lazy("VistaOrdenes")

class Pedido_ProductosDeleteView(DeleteView):
    model = Pedido_Productos
    template_name = "Tamales/delete_confirm.html"
    success_url = reverse_lazy("VistaOrdenes")

        #Clases para agregar un pedido y agregar productos.
class PedidoCreateView(CreateView):
    form_class = PedidosModelForm
    template_name = "Tamales/PedirPedido.html"
    success_url = reverse_lazy("VistaOrdenes")

class Pedido_ProductosCreateView(CreateView):
    form_class = PedidosProductosModelForm
    template_name = "Tamales/PedirPedido.html"
    success_url = reverse_lazy("VistaOrdenes")

        #Clases para actualizar un pedido y productos contenidos en él.
class Pedido_ProductosUpdateView(UpdateView):
    queryset = Pedido_Productos.objects.all()
    form_class = PedidosProductosModelForm
    template_name = "Tamales/update_view.html"
    success_url = reverse_lazy("VistaOrdenes")

        #funciones definidas no se usan
def Registro_orden(request):
    result_set01 = Pedidos.objects.all() #Cliente__ID_Cliente=2 ; filter(Pedido__Cliente=3)
    result_set02 = Pedido_Productos.objects.all()
    context = {
    "Pedidos": result_set01, "Productos_P": result_set02
    }
    return render(request, "Tamales/Ordenes.html", context)

def Hacer_Pedido(request):
    result_set01 = Pedidos.objects.all() #Cliente__ID_Cliente=2 ; filter(Pedido__Cliente=3)
    result_set02 = Pedido_Productos.objects.all()
    context = {
    "Pedidos": result_set01, "Productos_P": result_set02
    }
    return render(request, "Pedidos.html", context)
